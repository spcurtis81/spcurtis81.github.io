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

## Final privacy and support audit — 28 October 2026

This dated record supersedes earlier unresolved facts where explicitly confirmed below. It is an evidence-based audit and a proposed assessment for developer review, not approval of policy wording, legal certification or App Store submission clearance. Only this documentation file changes; public HTML/CSS, navigation and accepted app implementation remain unchanged.

### Confirmed developer instructions

Stephen Curtis describes Boarding Time as a free, non-commercial hobby app, with no ads, subscriptions, purchases or planned monetisation. Stephen will personally monitor and manage stephencurtisapps@gmail.com. Routine support correspondence is to be deleted within 12 months of issue resolution, including relevant Sent, archived and Trash copies. This is an operational commitment supplied by the developer, not an observed mailbox audit. Non-trader is the intended EU DSA self-assessment based on hobbyist/non-commercial circumstances, not a certification. No App Store Connect status was inspected or changed. No residential address is included or inferred.

### Proposed support legitimate-interests assessment (LIA)

- Purpose: answer voluntary support requests, reproduce and resolve reported defects, follow up with the requester and maintain continuity on the issue. This benefits both the user and hobby developer. No marketing, profiling, sale or newsletter use is proposed.
- Necessity: a reply address, relevant message and limited device/app-version information are proportionate for email support. Real name, full calendar exports, unredacted screenshots, health information and unrelated correspondence are not routinely necessary. Ask for a minimal reproduction first. Retaining resolved threads can support follow-up, but 12 months is a maximum, not a reason to retain every attachment for the full period; remove unnecessary content earlier. FAQ-only support cannot resolve every individual problem, while a ticketing platform would introduce more processing.
- Balancing: someone emailing support can reasonably expect a personal reply and limited troubleshooting. Optional contact, no effect on app access, no marketing, direct management and bounded retention reduce impact. Risks remain: sensitive calendar content, third-party information in screenshots, children/vulnerable users, mailbox compromise, unexpected provider processing and international handling. Proposed mitigations: request redaction, avoid sensitive submissions, restrict access, secure the mailbox/device, do not forward to unrelated recipients, do not paste correspondence into AI services without a separate assessment, and apply deletion reliably.
- Rights: explain access/correction, erasure/restriction and the right to object to legitimate-interests processing; assess requests individually rather than promising unconditional erasure. Portability is not generally a right for processing based solely on legitimate interests. ICO complaints remain available. A support email is not blanket consent or permission for unrelated use.
- Proposed outcome: legitimate interests is a plausible basis for ordinary, expected support if these measures are implemented and the developer adopts this assessment. It is not silently adopted by this audit. No contractual basis is inferred solely from an app download. Special-category data may require a separate Article 9 condition where applicable; unsolicited sensitive content should be minimised/deleted, not treated as automatically covered by the ordinary LIA. The developer's role and legal obligations concerning entirely local calendar processing are not resolved solely by the iOS permission or hobby status.

ICO guidance requires a context-specific purpose, necessity and balancing assessment; non-commercial interests can qualify. This record supplies a proposed assessment, not a conclusive determination of legal applicability.
Source: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/legitimate-interests/

### Google Gmail and GitHub Pages

Google processes message contents/attachments and service information to deliver, protect and operate Gmail. It describes assistive features, encryption in transit/at rest and international handling. These statements do not mean end-to-end encryption, UK-only storage, no automated processing, instant deletion of every backup, or access solely by Stephen. No actual Gmail settings, forwarding, connected apps, offline copies or account security were inspected. Consumer Gmail must not be described as having a verified Workspace processor agreement, enterprise retention controls or guaranteed regional storage. Its use is not automatically unlawful, but the applicable account terms, controller/processor roles and any developer transfer responsibilities need a proportionate decision.

Google publishes adequacy/DPF/UK-extension and contractual transfer mechanisms. Those are provider statements, not evidence that Stephen has a bespoke DPA, SCCs, IDTA or a completed transfer assessment. Confirm applicable entities/arrangements rather than claiming a specific safeguard covers every support message.
Sources: https://support.google.com/mail/answer/10434152?hl=en ; https://policies.google.com/privacy ; https://policies.google.com/privacy/frameworks?hl=en

Gmail deletion moves messages to Trash; manual permanent deletion is possible, and otherwise Trash retention can add 30 days. Archiving is not deletion. To meet the promised deadline, relevant copies must be removed from Trash by that deadline, not merely moved there then. Provider residual retention remains outside the developer's complete control.
Source: https://support.google.com/mail/answer/7401?hl=en

GitHub Pages records visitor IP addresses for security. GitHub describes international processing and transfer frameworks; do not promise UK-only website processing or invent a host-log retention period. The website source contains no analytics, third-party embeds, fonts, JavaScript, forms or site-set cookie implementation. This does not mean GitHub processes no visitor information or that the public source repository is private. Legal links load other providers when followed.
Sources: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages ; https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

### Current iOS source findings

Audited accepted main 0a2ce00bc545850d65c0b5af7aaa3aeca9a4b34d, version 0.1.0 (41). Tracked working tree clean; unrelated Previews.zip remains untracked and untouched.

- CalendarAccess/EventKitCalendarClient.swift:17,29,149 requests full event permission, queries date-window occurrences across accessible calendars (`calendars:nil`), and reads event identifier/occurrence date, start/end, title, notes, textual location, all-day status and calendar identifiers/names/source labels; discovery includes calendar type/subscription status. No event save/edit/delete API use identified. Full permission is write-capable even though implementation is read-only.
- CalendarAccess/CalendarEventOpener.swift:12 gives an original event to Apple's viewer with editing and calendar preview disabled. System viewer external actions/network effects are not proven absent by static inspection.
- Configuration/CalendarConfiguration.swift:11 and Configuration/CalendarConfigurationStore.swift:7 persist calendar metadata and custom presentation/selection state in Application Support JSON. UserDefaults stores appearance, theme, board style, Date Line preference and observed-permission flag. No persistent app event database, Keychain calls, SwiftData/Core Data, CloudKit or app-managed iCloud sync found. Platform icon state is separate.
- CalendarAccess/CalendarAccessService.swift:378,464 clears verified event snapshots on detected loss of permission; local settings/calendar metadata remain. BoardUI/BoardView.swift:93 refreshes on foreground activation. Missing calendars retain saved records as unavailable. No production erase-all control or explicit backup exclusion/custom encryption found. Backup/restore/offload/uninstall details remain device-verification items; system calendars are not deleted by this app.
- Source/package inspection found no app networking client/endpoints, external SDKs, advertising, analytics or developer crash-upload service. This is static evidence, not a network capture. Platform/provider sync and backups are distinct from developer-originated transfers.
- BoardUI/DateLineDiagnosticsControls.swift and Diagnostics/FirstFrameDiagnostics.swift have DEBUG guards; production dependencies and development UI are guarded. Debug exports can be shared by user action but are not a production support-submission flow. No explicit app-switcher privacy cover was found.
- PrivacyInfo.xcprivacy declares no collection/tracking and UserDefaults CA92.1. AboutBoardingTimeView.swift:30 still contains only a short privacy statement, with no public policy/support link. That remains a separate pre-submission app task after approved URLs exist.

### Existing archive verification (no build or signing preflight performed)

Inspected the existing `BoardingTime 28-10-2026, 09.40.xcarchive`, application under Products/Applications/BoardingTime.app. Archive identity is 0.1.0 (41), app.boardingtime.BoardingTime. Executable SHA256: 15ab03318ef72e7d457c1cd9358a77729136673898b4851b1a9f49a91c2d00ba.

- Embedded calendar usage text explains reading and non-modification. No additional usage-description key, background-mode declaration or ATS override was found in the inspected fields.
- Embedded PrivacyInfo.xcprivacy and ReleaseHistory.json are byte-identical to current source. Manifest matches the declarations above.
- No embedded Frameworks or PlugIns entries. Mach-O linked libraries are Apple system frameworks/Swift runtimes, including EventKit/EventKitUI; no third-party binary was identified. A weak libswiftCoreLocation runtime link is not evidence of GPS access; no corresponding source API/permission was found.
- Decoded application signature entitlements: application identifier, team identifier and get-task-allow=true. No iCloud, push, app-group or associated-domain entitlement was present. The embedded development profile allows broader keychain groups; that is not an app keychain implementation or proof of actual use.
- The archive has a development/debuggable local signature. Release-compiled code can have this local signature; it does not establish the final exported/re-signed TestFlight entitlements or imply the distributed app is debuggable. An actual distribution export/processed binary was not available for inspection here. No credential repair or distribution-signing check was performed.
- Named FirstFrameDiagnostics, AppearanceLaunchHarness, DevelopmentDiagnosticsSection, DateLineDiagnosticsControls, DateLineDiagnostics and makeExportFile symbols were absent. Combined with source guards this supports their exclusion; symbol absence alone is not proof for a stripped binary.
- Archive version/resources agree with accepted source; no reproducible-build or embedded Git provenance establishes every byte's commit. No app launch, packet capture, device Settings audit, backup test or TestFlight binary comparison performed.

### Provisional App Store declaration

Continue to propose Data Not Collected for the inspected production app, conditional on runtime/distribution and actual developer-diagnostics practices. On-device access/storage does not itself constitute Apple's label collection. Apple platform processing and calendar-provider sync must not automatically be attributed to the developer. Support emails are actual developer receipt of personal information, separately disclosed in the policy; the present app has no in-app form/email submission. A future in-app support form, upload or diagnostic flow must be assessed against Apple's collection and optional-disclosure rules, not assumed exempt because voluntary. Likewise assess any Apple-provided app data the developer actually collects/uses; do not automatically categorise all Apple diagnostics as either developer collection or exempt.
Source: https://developer.apple.com/app-store/app-privacy-details/

### Required wording changes before effective policy publication (not implemented)

1. Name Stephen as the person managing support and state the confirmed deletion scope: routine correspondence within 12 months of resolution, including relevant Sent, archived and Trash copies; distinguish provider residual retention and downloaded copies. Keep exceptions narrow and justified, not a blanket indefinite retention right.
2. After developer adoption of the LIA, replace the proposed lawful-basis wording with the adopted purpose/basis and a clear, separate right-to-object explanation. Do not remove review warnings before unresolved matters are decided.
3. Expand the website-hosting section to disclose possible international processing and link to GitHub's provider information; retain its IP/security disclosure. Identify relevant support provider involvement without asserting a verified processor contract or particular transfer mechanism not established for this account.
4. Clarify that any support email/attachments or platform feedback intentionally submitted to the developer can be received by Stephen, and that the no-app-upload statement does not cover these voluntary submissions. Confirm actual TestFlight/Apple diagnostics handling before adding categorical assertions.
5. Once publication is approved, set an actual effective date, remove draft-only copy and change the future-hosting wording to the verified deployed state. This audit does not authorise those edits or deployment. The approved support email and legal name are correct.

Optional editorial improvements: simplify technical identifiers/in-memory caveats for visitors; shorten the iPad FAQ to user-facing compatibility rather than test terminology; add a short permission/deletion summary and anchor; explain no account is required. Do not add a legal certification, residential address, fake App Store link or broad absolute privacy guarantees.

### Operational requirements and remaining decisions

- Developer approval needed: adopt/amend proposed LIA; approve final policy; confirm provider suitability/terms and applicable transfer obligations; confirm actual Apple feedback/diagnostics receipt; approve eventual publication and effective date. Intended non-trader self-assessment is now recorded but no legal certification or ASC submission is claimed. Reassess if monetisation/professional circumstances change. Residential-address obligations remain context-dependent; none published.
- Operationally record resolution date and review/delete before the 12-month deadline; cover sent/archived/trash, locally downloaded attachments, forwarded copies and exports under Stephen's control. Avoid retaining unneeded sensitive material. Document any justified exception and review it. Gmail settings were not changed.
- Personally restrict support access, secure Google account and devices (strong authentication/recovery), review connected apps/forwarding/offline copies, maintain a rights-request/incident process and avoid unassessed AI tools. These are recommendations, not settings verified by this audit.
- Technical remaining: inspect actual exported/processed distribution entitlements where available; observe runtime networks and Apple viewer actions; verify permission revocation/backup/uninstall and app-switcher exposure on device. No current source evidence of undisclosed app uploads was found.
- Website API still reports workflow-only Pages, status building, zero deployments; no deployment workflow exists. No Pages setting was changed in this audit. No complete live-host privacy validation claimed.

Disposition: conditional readiness for final policy review; not an unconditional publication or App Store GO. Required implementation is outside this audit: approved website policy copy/publication, then separate in-app policy/support links. No email, Gmail setting, release build, upload, submission or ASC privacy answer was changed.


## Privacy policy release candidate — 28 October 2026

Baseline: 26f2e6036d5c8190d80b22da154563bc39b9ee34. This section supersedes earlier pending LIA-adoption and unimplemented wording items where noted; historical audit evidence remains intact. The developer expressly approved legitimate interests for ordinary support following the documented assessment. The release candidate states that basis without provisional wording. It does not certify legal compliance or approve publication.

### Implemented policy changes

- Names Stephen Curtis as the personal Gmail support handler, limits use to answering/investigating/resolving/following up voluntary requests, excludes marketing/advertising and confirms app access is unaffected.
- Describes the approved ordinary-support legitimate interests and adds a separate, prominent right-to-object paragraph. Sensitive or unrelated processing is not automatically authorised.
- States permanent deletion from accessible mailbox locations within 12 months of resolution, including relevant Sent, archived and Trash copies; provider backup retention can extend beyond that. Necessary legal-obligation/claim exceptions remain purpose-limited. Encourages redaction/minimisation.
- Distinguishes voluntary support messages/attachments and developer-accessible Apple platform feedback/screenshots/diagnostics from automatic app calendar uploads. Developer-held routine support copies follow the support retention arrangements; Apple controls its own service retention. Actual account access/settings were not inspected.
- Identifies Gmail processing/automation, possible international processing and provider information links; expands GitHub host/international processing wording. Does not assert UK-only storage, end-to-end encryption, instant backup deletion, a host-log retention period or an unverified developer contract.
- Preserves calendar permissions, fields, local persistence, backup, revocation, deletion/offload, children/rights and existing contact disclosures. Keeps draft banners, noindex metadata and unpublished review status. No design/navigation, app implementation, Gmail setting or ASC answer changes.

### Completed public-document provider assessment

Checked current authoritative documents on 28 October 2026:

1. Google privacy policy (effective 16 October 2026): https://policies.google.com/privacy . Gmail help: https://support.google.com/mail/answer/10434152?hl=en . These describe service processing, including message/attachment storage, security and assistive features. Provider encryption descriptions are not a developer promise of end-to-end confidentiality or exclusive personal access. Consumer Gmail is not evidenced here as a Workspace processing-contract/retention/data-region product. Its suitability cannot be decided solely from a gmail.com address or presumed unlawful solely because it is consumer email.
2. Google transfer information (effective 23 August 2025): https://policies.google.com/privacy/frameworks . Google describes global infrastructure, adequacy mechanisms, DPF including UK Extension, and SCCs where relevant. These are published provider arrangements, not proof of a bespoke agreement with Stephen or the legal basis for every specific support transfer.
3. GitHub privacy statement (effective 27 April 2026): https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement . It describes its own controller activities and some processor contexts, international processing, SCCs and DPF/UK Extension. Do not label all hosting activities as processing solely on Stephen's instructions or infer a signed DPA from this general statement.
4. GitHub Pages documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages . Pages logs visitor IPs for security, even without a GitHub login. The site itself adds no analytics, scripts, third-party fonts, embeds or forms. Hosting-provider processing remains distinct from app calendar processing and from developer-received support emails.

Outcome: the policy can accurately identify these providers and describe their published processing and transfer information. No public-document finding establishes UK-only storage, universal processor-only roles or a developer-specific contractual safeguard. Provider roles for the actual accounts, applicable contracting entities, any controller-to-controller or processor obligations and whether a restricted-transfer assessment/arrangement is required of Stephen remain contextual legal questions. Neither those questions nor the approved LIA justify inventing safeguards or declaring legal compliance certified. No mailbox inspection, message transmission or provider-account settings change was performed.

### Final publication checklist / developer decisions

- [x] Developer approved ordinary-support legitimate-interests basis following the documented assessment.
- [x] Confirmed personal Gmail management, no marketing, redaction and 12-month accessible-mailbox deletion scope incorporated.
- [x] Current Google/GitHub public documents assessed and provider processing disclosed without contractual guarantees.
- [ ] Developer reviews and approves exact RC wording, including legal exception scope, rights and voluntary Apple feedback handling.
- [ ] Developer decides provider suitability and resolves applicable role/contract/transfer obligations proportionately; obtain qualified advice if uncertain. Public provider policies alone are not legal clearance.
- [ ] Confirm real operational access/security, deletion across Sent/archive/Trash and downloaded copies, and actual developer access to platform feedback/diagnostics. No claim these settings were audited.
- [ ] Complete remaining distribution/runtime checks identified in the archive audit; retain provisional Data Not Collected position until actual practices are confirmed. No new release build authorised by this task.
- [ ] Confirm intended non-trader self-assessment in the relevant submission process and any context-specific identity/address obligations; no legal certification or invented address.
- [ ] Explicitly approve website publication; only then set a real effective date and remove draft notices/review wording and noindex. Confirm publication mode/content before activating any deployment.
- [ ] Verify public HTTPS pages and then separately integrate privacy/support links into the iOS app. Do not describe this website RC as an App Store-ready build.

Recommendation: RC ready for developer content review; publication remains on hold. No deployment workflow is installed or activated. Prior workflow-only Pages state must be checked before source push; no Pages configuration changes are authorised here.
