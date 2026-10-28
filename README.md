# Stephen Curtis — Apps

Source repository: https://github.com/spcurtis81/spcurtis81.github.io

A small static developer website with Boarding Time overview, support and privacy pages. The developer approved the policy release candidate, legitimate-interests basis, personal Gmail support, 12-month manual deletion arrangements, provider suitability and public publication on 28 October 2026. Publication uses the manually triggered GitHub Pages workflow; only `dist/` is deployed. Historical review material remains in the public source repository but outside the website artifact. See [REVIEW.md](REVIEW.md).

## Architecture

- `dist/index.html` — developer landing page.
- `dist/boarding-time/index.html` — app overview.
- `dist/boarding-time/support/index.html` — FAQ and approved email contact.
- `dist/boarding-time/privacy/index.html` — privacy policy.
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

## GitHub Pages deployment

Pages uses GitHub Actions, not legacy main/root publishing. `.github/workflows/pages.yml` is manual-only (`workflow_dispatch`) and limited to main. It validates source, packages only `dist/`, and deploys the artifact to the `github-pages` environment. Official Actions are pinned to revisions. Build has contents-read only; deployment has Pages-write and OIDC-token permissions. There is no automatic push deployment.

```sh
gh workflow run pages.yml --ref main
gh run list --workflow pages.yml
```

Review future changes before manual deployment. Do not switch to main/root branch publishing: that could expose review documents as website pages. Verify the resulting HTTPS pages after each release. No build compilation is needed.

Public URLs:
- https://spcurtis81.github.io/
- https://spcurtis81.github.io/boarding-time/
- https://spcurtis81.github.io/boarding-time/support/
- https://spcurtis81.github.io/boarding-time/privacy/

GitHub guidance: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Adding future apps

Add `dist/<app-slug>/index.html`, plus `support/index.html` and `privacy/index.html` as appropriate. Reuse shared styling; adjust relative paths for directory depth. Add a developer landing-page entry and accurate app-specific support/privacy wording. Keep user data, internal materials and credentials out of the repository. Re-run checks and review each app's legal content before publication.

## History and public-data boundary

The original local draft was commit `31478d9`. With explicit user approval, its author/committer email was changed to the approved public support address before the first push; its source tree is identical and its replacement commit is `a3f50c7`. The original commit is not part of main's published ancestry. Public identity: Stephen Curtis; support/privacy contact: stephencurtisapps@gmail.com. No residential address is included. Do not push backup refs or use `--mirror`/`--all`.

This website is separate from the Boarding Time iOS repository. Its accepted app baseline remains 0a2ce00 / 0.1.0 (41); website work does not modify that repository.
