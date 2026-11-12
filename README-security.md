# London Architecture Map — deployment notes

This folder is prepared for Cloudflare Pages. Configure Cloudflare Access for the project's `*.pages.dev` hostname and allow only the owner's email before uploading or publishing `index.html`.

## Privacy and security

- The site is a static map. It has no login form, database, analytics, API keys, tokens, or user-submitted data.
- Keep the source project private. Do not publish it through GitHub Pages: ordinary GitHub Pages sites are public even when their repository is private.
- Cloudflare Access must be enabled for the production `pages.dev` hostname before the HTML is deployed. Enter only the allowed email address for one-time PIN login.
- Keep `_headers` in this folder when deploying. It sets browser security headers and permits map tiles from OpenStreetMap plus photo search and image results from Wikimedia Commons.
- OpenStreetMap receives tile requests when a user views or moves the map. Wikimedia Commons receives a search request when a user opens the photo panel. These services can receive request metadata such as IP address, browser headers, and the site's referrer.
- Photo results link to their Commons file pages, where the license and credit can be checked. Search results should be reviewed to confirm they depict the intended building.

## Files

- `index.html` — static map, ready to serve over HTTPS.
- `_headers` — Cloudflare Pages security headers.
