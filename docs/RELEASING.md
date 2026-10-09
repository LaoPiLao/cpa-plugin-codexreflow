# 发布清单

## 当前发布与商店状态 — 2026-10-09

[`v0.1.0` Windows amd64 Release](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.0)
已公开发布并设为 latest，ZIP / checksums 通过匿名下载及字节验收，未安装到生产。
此前已验证并安装的本地开发版为 `0.1.0-dev.5`，本轮没有替换它。
**公开 Release 和首个商店 PR 分别获授权；PR #222 已关闭，尚未上架。**
维护者此次审核要求 Darwin amd64/arm64、Linux amd64/arm64、Windows amd64 五个平台资产。
工作分支准备 `0.1.1` 原生构建/打包验证，不修改 `v0.1.0`；本轮不发布、不重提 PR、不安装生产。
仓库：[LaoPiLao/cpa-plugin-codexreflow](https://github.com/LaoPiLao/cpa-plugin-codexreflow)。

| 项目 | 已有证据 / 尚待完成 |
|---|---|
| SDK / 来源与许可 | SDK 固定 `8.0.13`；注册来源和 ZIP 内上游版权/第三方许可已逐字节复核 |
| dev.5 离线验证 | unit/race/vet/fuzz、31 项原生 ABI、19 项 Python 测试 |
| dev.5 隔离 HTTP/WS | CPA `8.0.13` / `8.0.15` / `8.0.16` 各 50 次案例执行，共 150 次，不是独立场景数 |
| dev.5 有限真实使用 | 截至 10 月 8 日 01:42:48（UTC+8），22 条已完成 WS 上游行、16 次客户端用量核对、6 次续接；两个聊天均有工具往返和完整回答 |
| 全面验收 | 真实 HTTP/SSE、复杂历史、取消/重连等边界仍待补；未评价答案质量 |
| 仓库与发布授权 | `LaoPiLao` 公开仓库已创建；代码推送、正式包验收和 Release 分别获授权；`upstream` 及本地继承标签保留 |
| 建仓源码检查 | 仅改模块归属，当前源码 unit/race/vet/fuzz、31 项原生 ABI、19 项 Python 测试通过；不替换已安装 DLL |
| 正式构件 | `0.1.0` 新 DLL：unit/race/vet/fuzz、31 项原生 ABI、19 项 Python、三宿主 150 次隔离案例执行通过；ZIP 内 DLL 另重跑同一组 31 项通过 |
| 远程 CI | 源提交 `8758649` 的 Windows/Linux job 成功；workflow 是开发构建，不是正式 DLL 哈希的远程验证 |
| Release / 商店 | `v0.1.0` 已公开并验收下载；商店 PR #222 因仅有 Windows 包被关闭；五平台原生 CI 结果须另读回，不把源码 CI 当作新包证明 |

证据：[公开发布与下载核验](RELEASE-2026-10-08-0.1.0.md)、[0.1.0 本地发布包验收](VALIDATION-2026-10-08-0.1.0.md)、[dev.5 隔离验证](VALIDATION-2026-10-07-dev5.md)、[有限真实核对](VALIDATION-2026-10-08-live-dev5.md)。
草稿：[首发说明](RELEASE-NOTES-0.1.0-DRAFT.md)、[商店提交](../store/SUBMISSION-DRAFT.md)。

## 本地候选与正式版分开

本地候选使用独立的 `scripts/package_candidate.py --version <编号开发版本> --library <DLL> --report <原生报告> --report <隔离报告>`。
它核对真实 DLL 注册信息、同构件测试报告和 Windows amd64 格式，保留 `local://codexreflow`，拒绝覆盖已有版本输出。
ZIP 包含许可证、脱敏证据计数/哈希、逐文件清单和只读诊断汇总工具；不会安装、发布或放宽正式版来源检查。
见 [本地候选说明](LOCAL-CANDIDATE.md)。

已经生成的 dev.5 ZIP 及其 manifest 是打包当时的不可变快照，其中 `live_model_acceptance: pending`
不能事后改写成通过；后续有限真实使用证据保存在独立核对文档。不覆盖旧 ZIP，也不把它改名为正式包。

## 已核对的商店规则

2026-10-08 对照 [官方商店说明](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store#release-requirements)：

- 注册表保留插件信息；二进制、校验和 Release 说明放在作者自己的仓库。条目须有 ID、名称、简介、作者和真实仓库；提交当天重查 ID 唯一性。
- 商店读取仓库 latest Release；标签为 `v` 加点分数字版本。开发版 `0.1.0-dev.5` 不符合该正式版本要求。
- 每个支持平台提供 `<id>_<version>_<goos>_<goarch>.zip`，附 `checksums.txt`（SHA256，sha256sum 格式）。
- 动态库必须在 ZIP 根部；Windows 为 `codexreflow.dll`，不能有多份动态库、绝对或越界路径。
- 只提交注册表变更，并提供真实仓库、Release 标签及 ZIP/校验文件存在证据。草稿和本地测试报告不能代替下载核验。

已发布 `v0.1.0` 仅 Windows amd64。2026-10-09 的 [审核反馈](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/222#issuecomment-6069997676)
及 [项目 issue #1](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/1) 明确要求五个平台预编译包；
此前 README 的“每个支持平台”不足以确认只发布 Windows 可收录，不能再按这个假设重提。
新版流程见 [五平台构建与验收](MULTIPLATFORM.md)；编译/原生 ABI 通过仍不是全面真实 CPA 集成认证。

## 正式构件发布前检查

发布前：

- [x] 用户确认 `LaoPiLao/cpa-plugin-codexreflow` 为公开仓库，授权建仓及代码推送。
- [x] `go.mod` 使用 `github.com/LaoPiLao/cpa-plugin-codexreflow`；SDK 固定 `8.0.13`。
- [x] 另行取得正式二进制 Release 和文档推送授权，已完成发布及公开下载验收。
- [x] 首次商店 PR #222 单独获授权并提交，但因缺少平台资产被关闭。
- [ ] 新版五平台 Release 与商店重提另行取得授权；不从工作分支/CI 授权推定。
- [x] 正式 DLL 的 ID/版本/来源/作者已读回，商店草稿为本项目所有者，不冒充 uf-hy。
- [x] ZIP 内 LICENSE、第三方声明和完整许可文本逐字节核对，上游档案保留来源标注。
- [x] 正式 DLL 本地 unit/race/vet/fuzz、原生 ABI、Python、隔离 HTTP/WS 和 ZIP 字节回归通过。
- [x] 同源提交远程 Windows/Linux CI 成功；它是开发构建，不当作正式 DLL 哈希的远程验证。
- [x] `docs/COMPATIBILITY.md` 区分正式包隔离证据与 dev.5 有限真实证据；未验收边界明确列为限制，不声称全面通过。
- [x] README 不声称未验证的平台、全模型支持或普遍质量提升。
- [x] 发布内容不包含密钥、账号或生产请求记录；商店草稿填写已验证的真实资产链接。

只改正式版本/仓库 metadata 也会产生新的 DLL 哈希；不能把 dev.5 的哈希、报告或使用样本改个版本名当作正式构件证明。
先确定来源与公开范围，再生成新构件和对应报告；任何生产试装或新增付费调用仍需另行授权。

## 构建流程（不覆盖已封存版本）

`v0.1.0` 已封存发布；`VERSION` 的 `0.1.1` 是待验收/待发布包版本，不是已存在的 Release。
在匹配的原生宿主和已提交源码上执行（Windows 先载入 `scripts/dev_env.ps1`）：

```powershell
python scripts/build_platform.py --goos windows --goarch amd64
```

每个平台打包到独立、不可覆盖的目录；根部为 `.dll` / `.so` / `.dylib` 与三个许可文件。
先验证原生注册及同库 ABI 报告，再从 ZIP 实际字节重跑相同测试；汇总器核对全部五个目录、
来源/源码/版本、报告及文件哈希，生成统一五行 `checksums.txt`。完整命令见 [五平台流程](MULTIPLATFORM.md)。
不要因为文件叫 `build/codexreflow.dll` 就认为它是最新构件；该非版本化路径可能保留旧构建。
正式打包前必须成功执行上面的构建，并读回注册 metadata 与 SHA256，不跳过打包器的拒绝检查。

已通过 GitHub Release 创建远程 `v0.1.0`，明确指向被测源码
`875864934cf82dbba90a7f85985f36ebd3a256d1`；不是后续仅修改文档的 `main`。
本地同名标签继承自 CodexComp，保留不动，**不要执行 `git push --tags`、整批标签同步或强制移动标签**。
新检出可正常取得 Reflow 的远程标签；已有继承标签的维护目录须使用明确源码 SHA，不以本地同名标签推定源码。

待另行授权后，向 [官方注册表](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store)提仅改 `registry.json` 的 PR，
带仓库、版本、构件存在证据和功能简介。最终收录由维护者审核，不保证通过。
发布/上传/发 PR 都不能因为写好了脚本或用户要求测试而自动执行。

目前 workflow 只有 read 权限，只产出开发构件；尚无自动发布任务。

推荐下一步：完成并读回五平台 CI 的实际原生结果、下载核验候选包后，再单独确认新版发布和商店重提。
不覆盖旧 Release，不因离线 ABI 通过而扩大真实集成或质量声明，不改生产安装。
