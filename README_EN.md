# CodexReflow

**Automatically continue eligible GPT requests.**

CodexReflow is a plugin for [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) (CPA). When a response meets its reasoning-truncation rules, it requests another round and merges the results for the client. It is intended for people already using Codex or another compatible client through CPA.

[简体中文](README.md) · [Download v0.1.1](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.1) · [Report a problem](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/new?template=bug_report.md)

## What it does

- **Continues eligible responses:** up to three additional rounds by default.
- **Works with HTTP and WebSocket:** handles streaming events over both, including HTTP/SSE.
- **Avoids maintaining a model list:** fresh configurations automatically match standard GPT-5+ text-model names.

Continuations consume additional tokens and may increase waiting time. They do not guarantee more reasoning or better answers.

## Install and use

The recommended route is the **CPA / ECPA plugin store**:

1. Open the plugin store and search for **CodexReflow**.
2. Install it. If prompted for a version, enter `v0.1.1`, or leave the field empty to use the repository's latest release.
3. Enable CodexReflow in the local plugin list and check that it is running.
4. Keep using your existing client. **A fresh configuration needs no handwritten YAML or model list.**

If you use CodexComp, disable it before enabling CodexReflow so that both plugins do not handle the same models.

Existing users can update through the version-selection action. Keep the previous plugin and configuration for rollback, and wait for active responses to finish before updating.

<details>
<summary>Manual downloads for v0.1.1</summary>

Choose the package for your operating system and CPU architecture:

| Platform | Package |
|---|---|
| Windows x64 | [Download](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_windows_amd64.zip) |
| Linux x64 | [Download](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_amd64.zip) |
| Linux ARM64 | [Download](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_arm64.zip) |
| macOS Intel | [Download](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_amd64.zip) |
| macOS Apple Silicon | [Download](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_arm64.zip) |

Verify the SHA256 against [checksums.txt](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/checksums.txt). See the [compatibility notes](docs/COMPATIBILITY.md) for platform coverage and known limitations.

</details>

## Do I need to configure it?

**Most users can keep the defaults.**

| Setting | Default behavior |
|---|---|
| Model selection | Automatically matches standard GPT text-model names such as `gpt-6-astra`, `gpt-6-sol` and `gpt-6-luna` |
| Continuation limit | Up to 3 additional rounds, or 4 rounds including the original request |
| Non-text models | Names marked as image, audio, realtime and other non-text families are excluded from automatic matching |
| Debug logging | Off; basic continuation diagnostics remain available |

Automatic matching uses the **model name in the request**. It does not synchronize CPA's model catalog. Custom aliases such as `my-coder` need manual selection.

Upgrades preserve the selection behavior of existing `models` lists. Set `model_mode` to `auto` if you want to switch to automatic matching.

See the [configuration reference](docs/CONFIGURATION.md) when you need exclusions, a lower continuation limit or custom aliases.

## Common questions

### Why do usage records still show 516?

CPA may record the original request and each continuation separately. The original 516 entry remains even when a continuation succeeds. An additional round may also produce no new reasoning tokens.

**Seeing 516 does not prove that the plugin failed or that a model was downgraded.** Continuation depends on a numeric heuristic and usable upstream reasoning state; it is not triggered unconditionally by every 516 entry.

### How can I tell whether it continued?

Check that the plugin is running, then inspect the logs for the same request: did it start an additional round, and did the request finish normally or fail? Also check whether the client received the response.

The [diagnostics guide](docs/DIAGNOSTICS.md) explains the fields and log-summary tool. An enabled switch or a single token count is not enough to establish the result.

### Does WebSocket work too?

Yes. Continuation on later turns requires complete context and usable upstream reasoning state. Missing, expired or oversized context may prevent continuation for that request. See the [compatibility notes](docs/COMPATIBILITY.md) for the conditions.

### What if requests stall or fail after enabling it?

Disable CodexReflow and try normal conversation with the same model to see whether the problem persists. A useful report includes CPA / ECPA, plugin and client versions, plus redacted error details.

Do not upload credentials, account information, full configuration files or raw conversations. [Report a problem](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/new?template=bug_report.md).

## Data and privacy

The plugin temporarily caches context and encrypted reasoning state in process memory to connect successive turns. Default diagnostic logs omit prompts, answers, credentials and encrypted reasoning content.

CPA and other plugins control their own logging. See the [compatibility notes](docs/COMPATIBILITY.md) for cache scope, size limits and expiration.

## Further reading

The configuration, diagnostics and development guides are currently in Chinese:

- [Configuration](docs/CONFIGURATION.md): automatic and manual modes, exclusions, continuation limits and legacy settings.
- [Diagnostics](docs/DIAGNOSTICS.md): continuation rounds, stop reasons and usage.
- [Compatibility and validation](docs/COMPATIBILITY.md): tested coverage and known limitations.
- [Development](CONTRIBUTING.md) · [Multiplatform builds](docs/MULTIPLATFORM.md) · [Release process](docs/RELEASING.md) · [Changelog](CHANGELOG.md).

## Attribution and license

CodexReflow is an independently maintained fork of [uf-hy / CodexComp v0.1.7](https://github.com/uf-hy/cpa-plugin-codexcomp/tree/v0.1.7). It retains the upstream copyright and CodexCont-related notices. It is not an official OpenAI or CLIProxyAPI plugin.

Licensed under [MIT](LICENSE). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt) for third-party attribution.
