# PRO Ecosystem 9.8 — regression checks

- Unified navigation brand updated to 9.6.
- Cash interface now accurately states that NBRB rates are fetched online, can be manually overridden, and require checking the last update date.
- Added `qa/regression.js`: validates denominations for eight currencies, integer minor-unit totals, NBRB cross-rate direction, and presence of persistence/freshness mechanisms.
- Re-ran HTML link and JavaScript syntax checks on 22 HTML files.
- Offline service-worker cache version bumped to 9.6.

## Limitations
Automated tests are unit/static checks, **not** full end-to-end browser verification. Real NBRB API connectivity, IndexedDB restore round-trip, and material catalog behavior after reload still need manual or browser automation tests. No user data is intentionally reset by this update.
