# Local validation — 28 October 2026

- Four HTML pages served successfully over a local HTTP server and visited in the browser.
- Internal file links and fragment targets checked; one H1 per page, unique IDs, no scripts, forms or frames.
- Desktop landing page visually reviewed at 1280px; privacy and overview reviewed at 390px. All four pages checked at 320px: document width equals viewport width (no horizontal page overflow).
- Support FAQ toggled open with Enter. Accessible navigation names, skip link, native disclosure controls and visible focus styling provided. This is not a complete screen-reader or WCAG certification audit.
- Automatic page dependencies consist only of same-site CSS. No external CSS imports, fonts, images, scripts or embeds. External legal links and mailto links require user action. Runtime host-provider behaviour cannot be verified before deployment.
- Screenshots saved locally under validation/ (ignored by Git): desktop.jpg, privacy-mobile.jpg, overview-mobile.jpg.
- No residential address or private address source was accessed or copied. Only supplied public developer identity and support email included. No credentials or tokens included.
- GitHub login confirmed through connected GitHub tool. Proposed repository lookup returned 404. No remote repository, Pages deployment or public legal-content publication performed.
- No email sent; mailbox deliverability not tested. No remote formal HTML validator used; source structural checks do not equal full standards validation.
- App baseline inspected read-only; no changes to Boarding Time repository, release configuration or TestFlight.


## GitHub source integration — 28 October 2026

- Target public repository verified empty (no branches/tags, size 0). Pages disabled; no workflow or Pages configuration added.
- Historical source tree inspected: only approved public developer name and support email. No residential address, unexpected email in file contents, credentials, private keys, tokens, local filesystem paths or tracking dependencies found.
- Original commit contained a different email in Git metadata. With explicit user approval, replaced its author/committer email with the public support email. Original and replacement source tree IDs match. Only sanitised main ancestry is eligible for push; no backup refs or tags are pushed.
- Four-page source content and CSS retained unchanged. README now documents architecture, development/checks, approval-gated dist-only Pages deployment and future apps. REVIEW.md reflects the new repository.
- Integration browser rerun: all four directory-style URLs return their intended pages at 390px with no horizontal overflow. Desktop landing page checked at 1280px; support FAQ toggled with Enter. New desktop/mobile captures remain ignored local evidence. No full assistive-technology certification or live Pages verification claimed.
- `python3 scripts/check_site.py` and `git diff --check` passed. Public-source push does not enable Pages or remove legal draft markers.
