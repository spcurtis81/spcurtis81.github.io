# Review and publication decisions

## Confirmed
- Developer/seller Stephen Curtis, Apple Individual enrollment.
- Contact stephencurtisapps@gmail.com; no residential address was read, copied or included.
- User selected deletion of routine support correspondence within 12 months of resolution. Confirm operational mailbox deletion including Trash; provider backups may persist.
- Authenticated account spcurtis81. The user subsequently created the public repository spcurtis81/spcurtis81.github.io. Before integration it had no refs, size 0 and has_pages=false; Pages endpoint returned 404. Source push is authorised after disclosure/validation checks; website publication is not. No existing contents overwritten.
- Static, dependency-free website. No JS, forms, trackers, cookies, external fonts/media or automatic third-party resources. Links to provider policies load only on user action.

## Resolve before publication
1. Approve final legal copy and publication explicitly. Draft markers and proposed language must not ship as an effective policy.
2. Confirm legitimate-interests basis for routine support with an appropriate assessment; this is proposed, not a legal conclusion. Assess controller role for local calendar processing and any sensitive information voluntarily sent. OS permission alone is not a universal UK GDPR consent analysis.
3. Verify Gmail account/service terms, processor/controller roles, international transfers and applicable safeguards. Do not imply consumer Gmail has Workspace contractual guarantees. Google privacy policy: https://policies.google.com/privacy . GitHub service roles/transfer terms likewise need review; do not invent retention or locations.
4. EU trader status: free/non-monetised is relevant but not decisive. Apple requires self-assessment; hobbyist intent may support non-trader status. Individual enrolment is separate. If trader, Apple requires public address, phone and email; its guidance allows alternate PO Box subject to verification. No status selected. https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements
5. Postal address: ICO guidance calls for identity and contact details; it does not establish from these facts that a residential address must be published. Other obligations may apply depending on actual business/trader status. Resolve proportionately; no residential or invented correspondence address included.
6. Distribution audit: verify archive manifest, entitlements/frameworks, runtime networking, Apple viewer actions and diagnostics access; maintain provisional Data Not Collected assessment. No archive or new build requested here.
7. Check actual support mailbox receipt and deletion practice. No test email sent (no messaging authorisation).
8. Confirm public availability wording when App Store release happens. Current overview accurately says preparing for first public release; no fake download link.

## Review evidence
Privacy audit source commit 0a2ce00bc545850d65c0b5af7aaa3aeca9a4b34d. EventKitCalendarClient.swift:17,29,149; CalendarConfiguration.swift:11; CalendarConfigurationStore.swift:7; PrivacyInfo.xcprivacy; AboutBoardingTimeView.swift:30; debug-only export in DateLineDiagnosticsControls.swift. Preparation is not legal clearance or App Store acceptance.

GitHub Pages IP logging: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
ICO transparency guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/

## Separate future app task
Once Pages is approved, published and HTTPS verified, add support/privacy links on a new appropriate app branch and validate via normal workflow. Do not alter accepted iOS baseline during website preparation.


## Automatic Pages activation exception

On the first authorised source push, GitHub automatically enabled legacy main/root Pages and started run 40677403418. The agent had not enabled Pages or added a workflow. The run was cancelled (completed/cancelled) and the deployment list was empty. GitHub rejected Pages deletion with HTTP 422, stating deactivation is not allowed for this repository. To prevent further automatic branch publication, publishing mode was changed to workflow-only with no deployment workflow installed. Pages remains configured (`has_pages=true`), so do not describe it as disabled. The API still reported a building status after cancellation; no successful deployment was recorded. Publication remains unapproved. Account-site automatic activation must be considered before future changes.
