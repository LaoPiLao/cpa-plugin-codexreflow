# CodexReflow

An independently maintained CPA plugin fork of
[CodexComp v0.1.7](https://github.com/uf-hy/cpa-plugin-codexcomp/tree/v0.1.7),
focused on reasoning continuation and stream event compatibility.
Not an official OpenAI or CLIProxyAPI plugin.

[简体中文](README.md)

## Development status

Current local development build: `0.1.0-dev.5`, installed with authorization on
CPA `8.0.16` at 23:38 UTC+8 on October 7, with effective registration read back;
no public binary Release yet. See [deployment record](docs/DEPLOYMENT-2026-10-07-dev5.md).
Adds per-run,
per-round payload-free diagnostics, an offline summary tool and a separate local
candidate packager. Continuation policy is unchanged. See [diagnostics](docs/DIAGNOSTICS.md)
and [dev.5 validation](docs/VALIDATION-2026-10-07-dev5.md): 31 native ABI cases,
19 Python tests and 150 scenario executions across three isolated CPA versions pass.
The same 50 cases are executed on each host; these are not 150 independent scenarios.
Remote results are tracked in [Actions](https://github.com/LaoPiLao/cpa-plugin-codexreflow/actions).

A read-only audit through October 8, 01:42:48 UTC+8 matched 16 folds to client
merged usage across two existing chats. All 22 completed upstream rows were HTTP
200 over WebSocket. Six folds continued, four through the native WS incremental
path; both chats had tool round trips and a final answer record. In-flight requests
are excluded. One client interruption is not attributed to plugin failure.
This is limited live-use evidence, not comprehensive HTTP/SSE, reliability or
answer-quality acceptance. A `516 -> 0` continuation actually ran but added no
reasoning tokens. See the [dev.5 live audit](docs/VALIDATION-2026-10-08-live-dev5.md).

Previous installed version: `0.1.0-dev.4`, plugin ID `codexreflow`, CPA SDK pinned to `v8.0.13`.
Installed with explicit authorization on 2026-10-05, after backup
and an idle check of the two user-designated chats. On October 7, production had
updated to CPA `8.0.16`; the identical DLL remained registered and effectively
enabled. A limited live audit matched 14 folds, including 12 new WS incremental
folds, to client merged usage. This is not comprehensive Desktop or quality acceptance.
Decodes both SSE `data:` payloads and raw WebSocket JSON host callback events.
Advertises native Responses output to avoid CPA's identity-translation filter,
while retaining codex output for other client protocol translations.
Restores SSE control-line boundaries removed by CPA's Scanner callbacks.

The `518n-2` pattern is a continuation heuristic, not proof of degraded reasoning.
Continuation spends additional tokens and is not a guaranteed quality improvement.

The identical dev.4 DLL passes 14 incremental-fold, 13 parent-bridge and 23
automatic-selection cases on each of real isolated CPA `8.0.13` and `8.0.15`,
using only loopback synthetic upstreams. Another 50-case execution run on October 7
passed on CPA `8.0.16` with the same DLL. WS tests perform actual handshakes on
both sides without HTTP fallback. The SDK pin is unchanged. The original two-host
runs contain 100 case executions; the 8.0.16 follow-up adds 50. These reuse baseline
and control scenarios and are not independent real-account acceptance tests.
The dev.3 control reproduces its original no-fold incremental behavior.
History, reconnects and cancellation still need broader live acceptance.
See the [October 7 live audit and host regression](docs/VALIDATION-2026-10-07-live-dev4.md),
[dev.4 validation](docs/VALIDATION-2026-10-05-dev4.md) and the
historical [dev.3 record](docs/VALIDATION-2026-10-05-dev3.md).
The public source repository is
[LaoPiLao/cpa-plugin-codexreflow](https://github.com/LaoPiLao/cpa-plugin-codexreflow).
No binary Release or official store listing has been created. The October 8
bootstrap changes only the Go module identity and repository materials, not the
SDK or runtime policy. Current source passes local unit/race/vet/fuzz, 31 native
ABI cases and 19 Python tests. Installed bytes and the previous candidate ZIP
remain unchanged; their hashes/reports are not evidence for newly built artifacts.

## Windows development

```powershell
python scripts/bootstrap_windows_tools.py
. ./scripts/dev_env.ps1
go test ./... -count=1
go test ./... -race -count=1
go vet ./...
./scripts/build_windows.ps1
python scripts/native_smoke.py build/codexreflow.dll
```

Toolchain downloads are checksum-verified and project-local. No production
configuration, system PATH, account, credential, or model call is used.
Only Windows x64 has been locally validated; CI configurations are not results.

With an existing CPA 8.0.13 executable, run the isolated synthetic integration:

```powershell
python scripts/isolated_cpa_smoke.py <CPA-executable> build/codexreflow.dll --report build/isolated-cpa-smoke.json
python scripts/isolated_cpa_smoke.py <CPA-executable> build/codexreflow.dll --auto-models --report build/isolated-auto-models.json
python scripts/ws_incremental_smoke.py --cpa <CPA-executable> --dll build/codexreflow.dll --native-folds --report build/ws-incremental.json
python scripts/ws_incremental_fold_smoke.py --cpa <CPA-executable> --dll build/codexreflow.dll --report build/ws-incremental-fold.json
```

For CPA 8.0.15 / 8.0.16, explicitly add the corresponding `--cpa-version 8.0.15`
or `--cpa-version 8.0.16` to each command. The
harness checks the host version rather than silently tracking latest.
It uses distinct loopback listeners and a temporary config/auth/plugin directory.
Production settings are neither read nor written; no billable model is used.

## WS context bridge and evidence

The client-visible response ID stays stable throughout a fold. A bounded,
expiring ID-only alias maps its next native WS parent to the final upstream ID,
scoped by the host-owned socket execution session, exact requested model and lane.
Unknown parents and scope misses are not remapped. The first upstream incremental
generation remains natively routed, with its delta/tool input and host auth/
transport policy preserved. A response-stream hook can then fold a heuristic
truncation **only when complete canonical context is available** for that scope.
Hidden continuations replay complete context, never a parentless delta alone.
Omitted request settings are inherited; explicit replacements take priority.

**Privacy change:** dev.4 additionally keeps the latest canonical input/output,
settings and opaque encrypted reasoning in process memory, not plugin logs or
disk. The replay cache is bounded to 64 entries, 16 MiB per entry, 64 MiB in total
and a lazily enforced 15-minute TTL. Active incremental requests have separate
64-entry/64-MiB serialized request-plus-stream accounting and lifecycle cleanup.
These are serialized-byte limits, not heap/RSS caps or secure erasure guarantees.
Unknown, expired, oversized and cross-scope histories never trigger extra model
calls; existing pre-upgrade sockets are not guaranteed to have replay context.
Raw 516 rows still exist even if a fold succeeds or adds zero reasoning tokens.

Terminal `metadata.proxy_reflow` and default INFO `fold_finished` logs carry an
independent per-fold run ID, attempted/terminal round counts, continuation counts,
stop reason and bridge status. A terminal round is not necessarily successful;
check its result and reason. Dev.4 marks native folds as `path: ws_incremental`.
Log `host_accepted` means host emission acceptance; `interceptor_returned` means
only that the hook returned output bytes. Neither confirms client delivery.
`ws_parent_remapped` uses the originating fold ID.
Dev.5 adds `fold_started` and per-round `round_finished` events linked by that same
run ID; `scripts/summarize_diagnostics.py` reads exported logs without credentials
or network calls. Missing counters are null, not zero; incomplete/duplicate logs
are not declared complete. `usage_join: unavailable` explicitly distinguishes
plugin correlation from an exact join to CPA/ECPA usage executions.
New diagnostics omit payloads, credentials, native response IDs and encrypted
content. No extra `debug_log` setting is required; not every native bypass is logged.

Pinned CPA configuration reload shuts down native upstream execution sessions
even with Reflow disabled. The regression recovers on a new socket with full
input; it does not establish seamless hot-reload continuity or WS multiplexing.

## Zero-configuration model selection

A fresh configuration needs only the CPA enable action, with no `models` field.
Installation does not automatically enable the plugin. The default `auto` mode
matches standard lowercase GPT-5+ text-family names, including route prefixes
and final reasoning suffixes, without changing the requested ID. Named image,
audio, realtime, transcription, speech, video, embedding and moderation families
are excluded. CPA still owns model availability, alias resolution and routing.

This is a **name heuristic, not exact synchronization with CPA's model catalog**
or capability discovery. The pinned SDK offers no direct catalog callback;
the plugin does not poll management APIs, read keys or register new models.
Arbitrary aliases need manual selection; a GPT-shaped alias is not proof of
its underlying model family.

| Configuration | Selection |
|---|---|
| No `model_mode` or `models` | Auto |
| Existing `models` only | Manual exact IDs, without widening prefix/suffix matching |
| Legacy empty/null `models`, no mode | Historical three-ID fallback |
| Explicit `model_mode: auto` | Auto; retained `models` ignored |
| Explicit `model_mode: manual` | Only the list; empty/missing list intercepts nothing |

An `auto` / `manual` enum is exposed to host configuration UIs. Existing users
can select `auto` without deleting their stored whitelist. Metadata and isolated
CPA hot reload are tested; actual ECPA UI rendering remains to be accepted.
Optional `exclude_models` takes priority in both modes: a bare ID excludes
prefix/suffix forms too, while a qualified ID excludes only that route. No globs
or arbitrary alias discovery are supported.

Default continuation settings remain three additional rounds (four total),
maximum tier six, marker `Continue thinking...`, debug off and experimental
minimum reasoning thresholds off. Missing encrypted reasoning does not trigger
extra calls. Set `max_continue: 0` to prevent continuations.
Use a distinct plugin configuration key; never intercept the same models with
both CodexComp and CodexReflow. See the Chinese README for optional examples.

## Attribution and publishing

MIT, with the upstream copyright and third-party notices retained.
Inherited docs are archived under `docs/upstream/` and are not current claims.
See [compatibility](docs/COMPATIBILITY.md) and [release gates](docs/RELEASING.md).
The repository owner is `LaoPiLao`. Existing development metadata uses `local://codexreflow`
as an explicit local source marker because CPA rejects empty source fields.
Formal release packaging requires a real GitHub repository. CI cannot publish
releases or submit store PRs.
The source-repository creation and code push are authorized separately from
binary Releases and store submission, neither of which is performed here.
Publication materials are drafts only: [release checklist](docs/RELEASING.md),
[v0.1.0 notes](docs/RELEASE-NOTES-0.1.0-DRAFT.md) and
[store submission](store/SUBMISSION-DRAFT.md). A formal build must be revalidated
after changing its version and repository metadata; development DLL evidence
must not be relabeled as a formal artifact's evidence.
