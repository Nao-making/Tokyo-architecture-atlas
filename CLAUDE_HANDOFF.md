# Claudeへの引き継ぎメモ

このフォルダーは「Tokyo Architecture Atlas（東京建築マップ）」の編集用一式です。ロンドン版（london-architecture-atlas）をベースに作成しました。公開や外部へのアップロードは、依頼がない限り行わないでください。

## 構成

- `index.html`：地図・一覧・絞り込み・日英切替などをまとめた静的ページ。建物データは含まず、起動時に `buildings.json` を読み込みます。
- `buildings.json`：建物データ（491件）。`261112_buildings_Tokyo-v4.xlsx` から生成します。
- `261112_build-from-xlsx-tokyo.py`：Excel → `buildings.json` の変換・検証スクリプト。
  `python3 261112_build-from-xlsx-tokyo.py 261112_buildings_Tokyo-v3.xlsx buildings.json`
- `_headers`：Cloudflare Pages向けヘッダー設定（現在の公開先はGitHub Pagesのため未使用）。
- `tokyo-architecture-atlas-icon*`、`tokyo-architecture-map.webmanifest`：アイコンとmanifest。

## データの扱い

- 項目：名称 `n`、建築家 `a`、年 `y`、用途 `u`、様式 `s`、住所 `addr`、緯度 `lat`、経度 `lon`、年代 `period`、概要 `d`、出典URL `src`、英語 `u_en`/`s_en`/`d_en`、プロジェクト情報 `p`/`ps`、リノベ `r`/`rn`/`rn_en`、検索キーワード `k`。
- 固有名詞（建物名・建築家名）は英語表記、説明やUIは日本語（EN切替で英語）。
- 建築家が空欄の2件（Tokyo Metropolitan Teien Art Museum Main Building、Tokyo Metropolitan Museum of Contemporary Art）は、変換スクリプトがDesign Architect欄の「Unknown (not stated in cited source)」を使います。
- 出典URLを確認できない場合は推測で埋めず、既存の値を保持するか、確認が必要な点として示してください。
- 建物名を変えると、お気に入り・訪問済みの印（localStorage `tokyoAtlasMarks1`）が消えます。

## 公開

- 公開先：GitHub `Nao-making/Tokyo-architecture-atlas`（GitHub Pages）。
- 地図タイルはOpenStreetMap、写真と建築家概要はWikimedia Commons／Wikipediaから取得します（インターネット接続が必要）。
- 追加しないもの：APIキー、パスワード、個人情報。
- Excel（`261112_buildings_Tokyo-v3.xlsx`）はリポジトリに含めません。

## 依頼文の例

「`CLAUDE_HANDOFF.md` を読み、`index.html` と `buildings.json` の現在の動作とデータ形式を保ったまま、◯◯を修正してください。公開はしないでください。」
