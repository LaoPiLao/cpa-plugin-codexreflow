# 商店提交草稿 — CodexReflow

**未提交。** 源码仓库已确认并创建为公开的 `LaoPiLao/cpa-plugin-codexreflow`；
此前授权完成建仓和代码推送；随后经授权完成 `0.1.0` 本地正式包验收。
正式 Release 上传与商店 PR 尚未授权，资产尚未公开可下载。
本文不是授权，也不是已经满足资产存在要求的证明。不要把本地候选 ZIP 交给商店安装器。

## 注册表条目

使用 [registry.entry.template.json](registry.entry.template.json) 作为单条来源模板。
`author`、`repository`、`homepage` 已填写真实归属；将插件对象追加到官方
`registry.json` 的现有 `plugins` 数组；**不是用模板覆盖整个注册表**。
提交时再次检查 `codexreflow` ID 是否唯一；本次页面查询未发现同名条目，不代表预留名称。
不必填 legacy `version` 字段，也不添加尚未存在的 logo 链接。

## PR 标题草稿

`Add CodexReflow plugin`

## PR 正文草稿

> 下列未填项必须在正式 Release 实际上传并可下载之后填写，才能转为提交正文。

- Repository: https://github.com/LaoPiLao/cpa-plugin-codexreflow
- Latest release: **待填写实际存在的 `v0.1.0` Release 链接**
- Windows amd64 asset: **待填写实际存在的 `codexreflow_0.1.0_windows_amd64.zip` 下载链接**
- Checksums: **待填写实际存在的 `checksums.txt` 下载链接及核验结果**

本地正式包已有 [验收记录](../docs/VALIDATION-2026-10-08-0.1.0.md)；ZIP SHA256 为
`63e0c62b414bea0dd98f1225f7507b78dcf8d0e7505e88147542a013ae8bd52d`。
这不是公开下载存在证据，提交前仍须上传后重新下载核验。

CodexReflow is an independent MIT-licensed fork of CodexComp v0.1.7. It adds
HTTP/SSE and raw WebSocket event decoding/folding, bounded native WS incremental
continuation with known complete context, automatic GPT text-name matching and
payload-free per-round diagnostics. It is not an official OpenAI or CLIProxyAPI
plugin; continuation is heuristic and may increase token usage and latency without
improving answer quality. Initial assets are intended for Windows amd64 only.

This PR changes only the registry entry. Binaries, checksums and release notes
remain in the author's repository. Upstream licenses and attribution are retained.

## 提交前检查

- [ ] 用户明确授权商店 PR；不能将仓库创建或本地试装授权当作商店提交授权。
- [ ] 正式仓库、Release、ZIP、checksums 四项链接可公开访问；不是占位符或 `local://` 来源。
- [ ] 标签、DLL 注册版本、ZIP 名称、校验文件和仓库来源完全匹配。
- [ ] 下载后复核 SHA256；ZIP 根部只有 `codexreflow.dll` 一份动态库，没有绝对/越界路径。
- [ ] 用正式构件重新完成原生 ABI 和隔离 HTTP/WS 回归，不能只引用开发 DLL 的结果。
- [ ] 官方注册表 ID 仍唯一；PR 不包含原始日志、账号、构件或其他无关条目。
- [ ] 功能/平台声明不超出证据；商店是否收录由维护者审核。

核对依据（2026-10-08）：[官方商店说明](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store#adding-a-plugin)、
[官方注册表](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/blob/main/registry.json)。提交当天仍需重查。

推荐下一步：先完成作者仓库的正式发布与下载核验，再单独获授权提交注册表 PR。
