# Approved academic redesign

## Functional baseline

The site follows the author-approved editorial specification supplied on 22 October 2026. Existing URLs, content safeguards and the pinned al-folio runtime are retained.

Local overrides of `al_folio_core` are intentional and supported for this personal site (see [Architecture](ARCHITECTURE.md#local-overrides-your-site-vs-this-repo)):

- `_includes/header.liquid`: a single home/brand link on every page and a skip-to-content link; menu data attributes remain upstream-compatible.
- `_layouts/default.liquid`: shared site CSS and a focusable main-content anchor; all feature includes remain intact.
- `assets/js/nav-toggle.js`: return focus to the appropriate toggle when Escape closes a menu containing keyboard focus.

The site header is sticky as a whole on desktop, rather than fixing its child inside a short wrapper. Below 960px it uses normal document flow so that expanded navigation pushes content down and remains reachable in short landscape viewports. The footer is in flow. A scoped `padding-top` reset neutralises the fixed-navbar offset applied unconditionally by the upstream `common.js`. `assets/css/site.css` owns these scoped repairs and A4 print rules; meaningful Research header/footer content is preserved.

## Repeatable captures

PR #9 is merged. Its existing capture names and default published-site behaviour remain supported by `scripts/capture_visual_review.py`. Environment variables allow local PR builds: `REVIEW_BASE_URL`, `REVIEW_OUT`, `REVIEW_COMMIT`; `REVIEW_FULL=1` adds all six pages in both themes at 320, 390, 719, 720, 721, 768, 959, 960, 961 and 1440px, expanded navigation, and Research/Publications/Experience print PDFs in both themes with backgrounds enabled and disabled.

The Actions capture workflow builds the PR base and proposed site, preserving before/after evidence without deploying the PR. Artefacts contain the capture manifest, PNGs, PDFs and rendered print pages. Optional `REVIEW_PROXY` and `REVIEW_IGNORE_HTTPS_ERRORS=1` support a trusted inspection proxy; neither is used by CI. The manifest also records H1 counts, horizontal overflow and loaded font faces. A generated capture is evidence for inspection, not an automatic assertion that visual review passed.
