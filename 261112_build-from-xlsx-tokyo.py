#!/usr/bin/env python3
"""261112_buildings_Tokyo.xlsx -> buildings.json（東京建築マップ用）
使い方: python3 261112_build-from-xlsx-tokyo.py 261112_buildings_Tokyo.xlsx buildings.json
"""
import sys,json,re
from openpyxl import load_workbook
KEYS=['n','a','y','u','s','addr','lat','lon','period','d','src','k',
 't','c','yr','sz','dm','da','ed','se','me','hc','pc','pm','qs','mc','ps','u_en','s_en','d_en','r','rn','rn_en']
PROJ=['t','c','yr','sz','dm','da','ed','se','me','hc','pc','pm','qs','mc']
PERIODS={'中世以前','16–18世紀','19世紀','20世紀','21世紀'}
def s(v):return v.strip() if isinstance(v,str) else v
def load(path):
    ws=load_workbook(path,data_only=True)['物件データ']
    out=[];errs=[];warns=[]
    for i,r in enumerate(ws.iter_rows(min_row=2,values_only=True),start=2):
        if all(v is None or str(v).strip()=='' for v in r[:12]):continue
        b={k:s(v) for k,v in zip(KEYS,r)}
        if not b.get('a') and str(b.get('da') or '').startswith('Unknown'):
            b['a']=b['da'];warns.append(f'行{i} {b["n"]}: 建築家が空のため Design Architect 欄の「{b["da"]}」を使用')
        e=lambda m:errs.append(f'行{i} {b.get("n")}: {m}')
        for k in ['n','a','y','u','s','addr','lat','lon','period','d','src']:
            if b.get(k) in (None,''):e(f'{k} が空です')
        try:b['y']=int(b['y'])
        except Exception:e('完成年が整数ではありません')
        try:
            b['lat']=float(b['lat']);b['lon']=float(b['lon'])
            if not(35.4<=b['lat']<=35.9 and 139.0<=b['lon']<=140.1):e('座標が東京周辺の範囲外です')
        except Exception:e('緯度・経度が数値ではありません')
        if b.get('period') not in PERIODS:e('年代の値が不正です')
        if not str(b.get('src') or '').startswith('https://'):e('出典URLが https:// で始まっていません')
        for k in ['u_en','s_en','d_en']:
            if not b.get(k):warns.append(f'行{i} {b["n"]}: {k} が空です')
        d={k:b[k] for k in ['n','a','y','u','s','addr','lat','lon','period','d','src','u_en','s_en','d_en'] if b.get(k) not in (None,'')}
        p={k:str(b[k]) for k in PROJ if b.get(k) not in (None,'')}
        if p:
            d['p']=p
            ps=[u for u in re.split(r'[\s]+',str(b.get('ps') or '')) if u]
            bad=[u for u in ps if not u.startswith('https://')]
            if bad:e(f'プロジェクト情報の出典URLが不正: {bad}')
            if not ps:e('プロジェクト情報はあるが出典URLがありません')
            if ps:d['ps']=ps
        if b.get('r'):d['r']=1
        if b.get('rn'):d['rn']=b['rn']
        if b.get('rn_en'):d['rn_en']=b['rn_en']
        if b.get('k'):d['k']=b['k']
        out.append(d)
    names=[d['n'] for d in out]
    for n in {x for x in names if names.count(x)>1}:errs.append(f'建物名が重複: {n}')
    return out,errs,warns
if __name__=='__main__':
    x,o=sys.argv[1:3]
    rows,errs,warns=load(x)
    for w in warns:print('警告:',w)
    if errs:
        print('エラー:');[print(' ',e) for e in errs];sys.exit(1)
    json.dump(rows,open(o,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    print(f'{len(rows)}件を出力しました ->',o)
