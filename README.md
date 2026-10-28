# Stephen Curtis — Apps

Source repository: https://github.com/spcurtis81/spcurtis81.github.io

A small, static developer website with Boarding Time overview, support and draft privacy pages. **Source is public; no Pages deployment is recorded.** GitHub automatically enabled legacy Pages on the first push. Its build was cancelled, and Pages was switched to workflow-only mode with no deployment workflow installed. GitHub refused the deactivation request. Pushing source does not approve the draft policy or authorise website publication. Read [REVIEW.md](REVIEW.md) before release.

## Architecture

- `dist/index.html` — developer landing page.
- `dist/boarding-time/index.html` — app overview.
- `dist/boarding-time/support/index.html` — FAQ and approved email contact.
- `dist/boarding-time/privacy/index.html` — policy review draft.
- `dist/assets/styles.css` — shared responsive styles and system fonts.
- `dist/.nojekyll` — direct static hosting marker.
- `scripts/check_site.py` — local structural/link checks.
- `REVIEW.md`, `VALIDATION.md` — repository review records; not visitor-facing deployment files.

No build system, JavaScript, package manager, backend, cookies, forms, analytics or external rendering dependencies. Native HTML disclosure elements provide the FAQ. Relative file links work locally and under the account-level Pages URL. Each directory has an index, supporting the eventual URLs `/`, `/boarding-time/`, `/boarding-time/support/` and `/boarding-time/privacy/`.

## Local development

Requires Python 3.9+ for checks and serving (no packages). From the repository root:

```sh
python3 -m http.server 8876 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8876/ . Stop with Ctrl-C. Edit HTML/CSS directly and reload. No application data or API credentials are needed.

## Building and testing

`dist/` is already the deployment output; no compilation is required.

```sh
python3 scripts/check_site.py
git diff --check
```

The checker validates nesting, local links/fragments, page landmarks, unique IDs, mailto destination, resource origins and basic hosting structure. It does not replace a full HTML validator or accessibility audit. Also review desktop/mobile layouts, keyboard focus and FAQ interaction. Verify content against the app audit when behaviour changes. Screenshots in local `validation/` are ignored by Git.

## GitHub Pages deployment — approval required

**Do not enable Pages or deploy until publication and final legal content are explicitly approved. No deployment workflow is installed.** Do not select main/root as a branch publishing source: the website is under `dist/`, while the repository root contains review documentation.

After approval:

1. Resolve REVIEW.md, approve policy copy, set the actual effective date, and remove draft banners, review-only notes and noindex metadata. Do not backdate the policy.
2. Re-run checks, browser validation and the public-history disclosure audit.
3. In repository Settings → Pages, confirm GitHub Actions is the publishing mode. Add a separately reviewed, manually triggered (`workflow_dispatch`) workflow; no automatic push trigger is needed initially.
4. Follow GitHub's current custom Pages workflow: checkout, validate with Python, configure Pages, upload **only `dist/`** using `actions/upload-pages-artifact`, then deploy with `actions/deploy-pages`. Review current action versions and pin reviewed revisions. The deploy job needs `pages: write`, `id-token: write` and the `github-pages` environment. Never upload the entire repository as the site artifact.
5. Run the approved workflow, then verify HTTPS, navigation, accessibility and unauthenticated policy access at all four URLs. Only then supply URLs to App Store Connect or a separate iOS integration task.

Official workflow guidance: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

Expected URLs (not confirmed live):
- https://spcurtis81.github.io/
- https://spcurtis81.github.io/boarding-time/
- https://spcurtis81.github.io/boarding-time/support/
- https://spcurtis81.github.io/boarding-time/privacy/

## Adding future apps

Add `dist/<app-slug>/index.html`, plus `support/index.html` and `privacy/index.html` as appropriate. Reuse shared styling; adjust relative paths for directory depth. Add a developer landing-page entry and accurate app-specific support/privacy wording. Keep user data, internal materials and credentials out of the repository. Re-run checks and review each app's legal content before publication.

## History and public-data boundary

The original local draft was commit `31478d9`. With explicit user approval, its author/committer email was changed to the approved public support address before the first push; its source tree is identical and its replacement commit is `a3f50c7`. The original commit is not part of main's published ancestry. Public identity: Stephen Curtis; support/privacy contact: stephencurtisapps@gmail.com. No residential address is included. Do not push backup refs or use `--mirror`/`--all`.

This website is separate from the Boarding Time iOS repository. Its accepted app baseline remains 0a2ce00 / 0.1.0 (41); website work does not modify that repository.
