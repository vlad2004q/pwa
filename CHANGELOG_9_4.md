# PRO Ecosystem 9.4 — incremental stabilization

- Navigation version 9.4, safer back navigation, removal of duplicate header home link, better mobile menu scrolling.
- Cash: show the date of last successful NBRB rate update and stale warning if over 24 hours old. Saved rates remain available offline.
- Materials: visible diagnostic if the catalog is empty after loading; existing records are never cleared automatically.
- Motion: ensure decorative full-screen overlays do not intercept input; reduced-motion accessibility fallback.
- PWA: new service worker cache key.

## Limitations
- Browser end-to-end tests have not been run.
- Existing supported currencies use two decimal places. Full ISO-4217 minor-unit coverage is not implemented.
- Materials cannot be restored if the underlying source files or stored user records are actually absent.
- Always export a backup before deploying.
