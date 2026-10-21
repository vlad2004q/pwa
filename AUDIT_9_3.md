# PRO Ecosystem 9.3 — audit and changes

- 118 files in source ZIP, including 20+ app pages. Original apps preserved.
- Navigation: updated branding, focus states, mobile menu and redundant home links handling.
- Materials: seed catalog + imported PDF data already merged with local records; existing data is not cleared. The material hub still requires interactive browser testing.
- Currency: reviewed NBRB conversion formula: quote is BYN per unit of foreign currency; rate[target:source] = quote(source)/quote(target). Formula in 9.2 was correct and retained. NBRB API requires internet. Minor units are currently 2 decimal places for eight supported currencies; not all world currencies are supported.
- Animation: removed finance fullscreen animation assets from the finance HTML entrypoint.
- Storage: new export/import of pro-* localStorage keys plus PROWorkspace IndexedDB records when available. No automatic destructive migration. Backup is a JSON file containing sensitive user data.
- Cache: service worker version incremented.
- Caveat: browser end-to-end testing has not been performed; back up data before deployment.
