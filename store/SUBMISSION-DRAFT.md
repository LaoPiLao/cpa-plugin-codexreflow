# 商店提交草稿 — CodexReflow

**首次提交已关闭；五平台 Release 已发布，尚未重提商店。**
公开仓库为 `LaoPiLao/cpa-plugin-codexreflow`；建仓、构建/验收、main 合并、公开 Release
与文档推送分别经授权完成。`v0.1.1` 已于 2026-10-09 发布并读回为 latest stable，
五个 ZIP 及统一校验文件均经匿名下载核验。
首次商店 [PR #222](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/222) 经独立授权提交，
10 月 9 日关闭、未合并：[审核反馈](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/222#issuecomment-6069997676)要求补齐五平台。
本次文档核对时官方注册表仍无 `codexreflow`。下面只更新重提材料，**不创建 PR、评论或重新打开旧 PR**；
重提需另行确认，收录由维护者决定。见 [本次发布证据](../docs/RELEASE-2026-10-09-0.1.1.md)
及 [五平台说明](../docs/MULTIPLATFORM.md)；[旧版发布记录](../docs/RELEASE-2026-10-08-0.1.0.md)仅作历史参考。

## 注册表条目

使用 [registry.entry.template.json](registry.entry.template.json) 作为单条来源模板。
`author`、`repository`、`homepage` 已填写真实归属；将插件对象追加到官方
`registry.json` 的现有 `plugins` 数组；**不是用模板覆盖整个注册表**。
提交时再次检查 `codexreflow` ID 是否唯一；本次注册表读取未发现同名条目，不代表预留名称。
不必填 legacy `version` 字段，也不添加尚未存在的 logo 链接。

## PR 标题草稿

`Add CodexReflow plugin`

## v0.1.1 重提 PR 正文材料（尚未提交）

> 仅为文档草稿。真正提交当天必须重新核对规则、ID 唯一性、latest 及全部公开下载；不能把此处更新当作已重提。

- Repository: [LaoPiLao/cpa-plugin-codexreflow](https://github.com/LaoPiLao/cpa-plugin-codexreflow)
- Latest release: [v0.1.1](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.1)
- Source/tag: [6c71eee479e9939a3d300b9231117fae11eef296](https://github.com/LaoPiLao/cpa-plugin-codexreflow/commit/6c71eee479e9939a3d300b9231117fae11eef296)
- Windows amd64: [codexreflow_0.1.1_windows_amd64.zip](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_windows_amd64.zip)
- Linux amd64: [codexreflow_0.1.1_linux_amd64.zip](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_amd64.zip)
- Linux arm64: [codexreflow_0.1.1_linux_arm64.zip](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_arm64.zip)
- macOS amd64: [codexreflow_0.1.1_darwin_amd64.zip](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_amd64.zip)
- macOS arm64: [codexreflow_0.1.1_darwin_arm64.zip](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_arm64.zip)
- Checksums: [checksums.txt](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/checksums.txt); all six public assets anonymously downloaded and verified byte-for-byte, including SHA256, size, ZIP CRC, architecture and retained licenses, on October 9, 2026.
- Native package CI: [main run #37916034316](https://github.com/LaoPiLao/cpa-plugin-codexreflow/actions/runs/37916034316), five native jobs plus aggregate job all passed; these exact tested bytes were published.

完整资产大小、SHA256、来源及验收范围见 [独立发布记录](../docs/RELEASE-2026-10-09-0.1.1.md)。
公开下载的 Windows DLL 本地另读回注册并重跑 31 项原生离线案例通过；不是生产试装。

CodexReflow is an independent MIT-licensed fork of CodexComp v0.1.7. It adds
HTTP/SSE and raw WebSocket event decoding/folding, bounded native WS incremental
continuation with known complete context, automatic GPT text-name matching and
payload-free per-round diagnostics. It is not an official OpenAI or CLIProxyAPI
plugin; continuation is heuristic and may increase token usage and latency without
improving answer quality. This release provides Windows amd64, Linux amd64/arm64
and macOS amd64/arm64 packages, addressing the missing-platform feedback in the
closed PR #222. CPA SDK remains pinned to v8.0.13; Go implementation and policy
are unchanged from v0.1.0.

Each native target passed Go unit/race/vet/fuzz, all 47 Python regressions and
the same 31-case C ABI mock-host suite on both original and packaged library bytes.
That is 155 case executions per group, not 310 distinct scenarios. This is
offline native validation, not full CPA/HTTP/WebSocket, real-model or Desktop
acceptance on every platform. No production installation or live-model tests
were performed for these new binaries. Historical dev.5 and v0.1.0 integration
evidence is separate. Arbitrary older glibc/musl, older macOS and distribution
signing/notarization are not validated.

The proposed PR changes only the registry entry. Binaries, checksums and release notes
remain in the author's repository. Upstream licenses and attribution are retained.

## 提交前检查

- [x] 首次 PR #222 经授权提交，但因缺少平台资产被关闭。
- [x] 新版五平台 Release 独立获授权，已发布并验收；不是从工作分支/CI 授权推定。
- [ ] 用户另行授权商店重提；不能将发布或文档推送授权当作重提授权。
- [x] 五平台实际资产及统一 `checksums.txt` 已发布并匿名下载复核；链接不是占位符。
- [x] 正式仓库、Release、ZIP、checksums 四项链接可公开访问；不是占位符或 `local://` 来源。
- [x] 远程标签、五平台库注册版本、ZIP 名称、校验文件和仓库来源完全匹配；不以继承的本地同名标签推定来源。
- [x] 匿名下载后复核 SHA256；每个 ZIP 根部只有对应平台的一份动态库及三个许可文件，无绝对/越界路径。
- [x] 新正式构件完成五平台原生 ABI 与包内字节回归；公开 Windows 字节再验收，不挪用开发 DLL 或旧 v0.1.0 的隔离报告。
- [ ] 官方注册表 ID 仍唯一；PR 不包含原始日志、账号、构件或其他无关条目。
- [x] 草稿明确五平台实际 CPA/HTTP/WS 与真实模型未全面验收，声明不超出证据；商店是否收录由维护者审核。

核对依据（2026-10-08）：[官方商店说明](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store#adding-a-plugin)、
[官方注册表](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/blob/main/registry.json)。提交当天仍需重查。

推荐下一步：单独确认商店重提授权，再重查规则、ID 唯一性和公开资产，
仍只提交注册表 PR，不改其他条目或生产配置。
