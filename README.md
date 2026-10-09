# CodexReflow · 续流

CPA 的 Codex 推理续接与流式兼容插件。基于
[CodexComp v0.1.7](https://github.com/uf-hy/cpa-plugin-codexcomp/tree/v0.1.7)
的独立维护分支，**不是 OpenAI 或 CLIProxyAPI 官方插件**。

[English](README_EN.md) · [兼容性与验收](docs/COMPATIBILITY.md) · [维护流程](CONTRIBUTING.md)

## 当前状态

- [`v0.1.1` 五平台 Release](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.1) 已于 2026-10-09 18:43:21（UTC+8）公开并读回为 latest stable。Windows amd64、Linux amd64/arm64、macOS amd64/arm64 原生 CI 全部通过；五个 ZIP 和统一校验文件均经匿名下载逐字节复核。公开下载的 Windows DLL 另通过 31 项原生离线案例。**未安装到生产，亦非五平台全面 CPA/真实模型验收。** 见 [本次发布记录](docs/RELEASE-2026-10-09-0.1.1.md) 和 [五平台流程与边界](docs/MULTIPLATFORM.md)。
- 商店已于 10 月 9 日经独立授权重提 [PR #225](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/225)，**当前开放、未合并，待维护者审核，尚未上架**。只新增一个注册条目，保留原有 111 个条目；五平台资产重提前再次匿名下载复核通过。旧 [PR #222](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/222) 因 Windows-only 被关闭，保留不动；补齐包不保证收录。见 [商店重提记录](docs/STORE-SUBMISSION-2026-10-09-0.1.1.md)。
- 历史 [`v0.1.0` Windows amd64 Release](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.0) 于 2026-10-08 公开，正文/标签/资产保留不变，不再是 latest。其正式包通过离线/隔离 HTTP/WS 回归，未安装到生产；旧证据不移作 `0.1.1` 新构件集成验收。见 [旧正式包验收](docs/VALIDATION-2026-10-08-0.1.0.md) 和 [旧发布记录](docs/RELEASE-2026-10-08-0.1.0.md)。
- 最近一次已记录的授权部署为开发版 `0.1.0-dev.5`，插件 ID：`codexreflow`；2026-10-07 23:38（UTC+8）安装到 CPA `8.0.16`，本次发布及文档更新不替换生产安装。dev.5 增加按次逐轮脱敏诊断、只读汇总工具和独立的本地候选打包器，不修改续写策略。见 [诊断说明](docs/DIAGNOSTICS.md)、[dev.5 验证记录](docs/VALIDATION-2026-10-07-dev5.md)、[安装记录](docs/DEPLOYMENT-2026-10-07-dev5.md)。
- 10 月 8 日截至 01:42:48（UTC+8）的只读核对：两个已有会话共 22 条已完成上游记录均为 HTTP 200，16 次处理的客户端合并用量吻合，6 次实际续接（其中 4 次原生 WS 增量路径），两个会话均有完整回答和工具往返记录。全部上游样本使用 WS；不覆盖仍在运行的请求、真实 HTTP/SSE 的全面验收或答案质量。见 [dev.5 有限真实核对](docs/VALIDATION-2026-10-08-live-dev5.md)。
- SDK 锁定为 CLIProxyAPI `v8.0.13`，无相邻目录 `replace`，不追随宿主最新版本自动构建。
- SSE / 裸 JSON 共用事件解码和折叠逻辑；对 Responses 客户端声明直接输出格式，避开 CPA 8.0.9+ 的 identity-frame 误过滤路径。
- 相同 dev.5 DLL 分别通过真实 CPA `8.0.13` / `8.0.15` / `8.0.16` 进程 + 本地合成上游的 HTTP/WS 隔离回归；每种宿主 50 次案例执行，共 150 次，另通过 31 项原生 ABI 和 19 项 Python 测试。WS 双端握手，未回退 HTTP；不是 150 种独立场景，远程结果请查看 [Actions](https://github.com/LaoPiLao/cpa-plugin-codexreflow/actions)。
- 新配置默认自动匹配 GPT-5 及以上的标准文本系列名称，无须维护模型白名单；旧显式白名单仍保持精确匹配。
- 在 dev.3 的响应 ID 衔接基础上，新增**完整上下文已知时**的原生 WS 增量续写。每种宿主各通过 14 项新增增量、13 项衔接和 23 项自动选择回归；另重现 dev.3 不追加增量思考的行为作为对照。
- **隔离回归和有限真实样本都不是全面生产认证。** 取消、复杂上下文、重连和质量仍未全面验收；后台会话的 `interrupted` 记录不能单独归因为插件故障。
- 公开源码仓库：[LaoPiLao/cpa-plugin-codexreflow](https://github.com/LaoPiLao/cpa-plugin-codexreflow)。`v0.1.1` 固定到被测源码 `6c71eee`，旧 `v0.1.0` 保留在 `8758649`；文档另更新于 `main`，不移动发布标签。正式构件使用真实仓库来源，不能以继承的本地同名标签识别发布源码。
- [发布源提交的五平台 CI](https://github.com/LaoPiLao/cpa-plugin-codexreflow/actions/runs/37916034316) 各通过 unit/race/vet/fuzz、47 项 Python 测试、原库及包内库各 31 项原生 ABI；两组各 155 次案例执行不是 310 种独立场景。运行 Go 实现、SDK 和策略相对 `v0.1.0` 不变；已封存构件及历史报告不覆盖、不改名复用。

### 下载 v0.1.1

| 平台 | 安装 ZIP |
|---|---|
| Windows amd64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_windows_amd64.zip) |
| Linux amd64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_amd64.zip) |
| Linux arm64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_arm64.zip) |
| macOS amd64（Intel） | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_amd64.zip) |
| macOS arm64（Apple Silicon） | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_arm64.zip) |

下载后对照 [checksums.txt](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/checksums.txt)
核对 SHA256，保留旧插件及配置以便回滚；公开发布不会自动安装或启用。

验证详情：[v0.1.1 五平台发布与下载](docs/RELEASE-2026-10-09-0.1.1.md) · [五平台流程](docs/MULTIPLATFORM.md)。历史证据：[v0.1.0 正式包验收](docs/VALIDATION-2026-10-08-0.1.0.md) · [v0.1.0 发布记录](docs/RELEASE-2026-10-08-0.1.0.md) · [dev.5 有限真实核对](docs/VALIDATION-2026-10-08-live-dev5.md) · [dev.5 隔离回归](docs/VALIDATION-2026-10-07-dev5.md) · [dev.4 真实增量续写与 CPA 8.0.16](docs/VALIDATION-2026-10-07-live-dev4.md) · [WS 增量续写与授权部署](docs/VALIDATION-2026-10-05-dev4.md) · [WS 衔接与诊断](docs/VALIDATION-2026-10-05-dev3.md) · [默认自动匹配](docs/VALIDATION-2026-10-05-dev2.md) · [断流修补](docs/VALIDATION-2026-10-05-dev1.md) · [首轮历史记录](docs/VALIDATION-2026-10-05.md)。

## 功能与边界

保留上游的 `518n-2` 检测、`encrypted_content` 续写、输出缓冲和多轮用量合并。
该数字模式只是续写启发式，**不能仅凭 516 判定降智，也不能保证续写提升答案质量**。
续写会消耗真实 token，并增加延迟。

改进：

1. 同时解析 HTTP/SSE 的 `data:` 帧和 CPA WebSocket 回调的裸 JSON；支持分块、合并事件及字符串内的 `data:` / 花括号，并恢复 CPA 扫描后丢失的 SSE 控制行换行边界。
2. Responses 输出不重复翻译；保留 `codex` 输出声明，供宿主翻译 Chat Completions / Messages。
3. 不完整、畸形和过大事件明确失败，而不是静默等到 EOF；错误信息不包含响应原文。
4. 独立插件 ID、日志前缀和会话缓存命名空间；兼容旧会话请求头。
5. 默认自动匹配、可选手动白名单和优先排除名单；在插件配置元数据中提供 `auto` / `manual` 下拉选项。
6. 续写维持稳定的客户端响应 ID；后继原生 WS 首次上游调用仅把已知父 ID 映射到追加轮的实际 ID，保留客户端增量和宿主路由。
7. WS 增量响应通过响应流钩子复用折叠器；仅在同连接/模型/通道的完整上下文命中、满足截断启发式且具备加密状态时追加调用。隐藏续写重放完整上下文，而不是删除父 ID 后只发送当前增量。

模型路由器仍只接管匹配模型、支持协议、无 `previous_response_id` 的流式请求，Responses 的
`input` 必须为数组。携带父 ID 的首次生成仍由 CPA 原生处理；dev.4 在响应阶段增加有条件的续写。
未知、过期或过大的上下文不会触发额外模型调用，也不会被拼成残缺重放；升级前已有的连接不保证命中。
不同连接、模型或通道不能借用缓存，`generate:false` 不接管。

**隐私变化：** 除 dev.3 的 ID 别名外，dev.4 在进程内存暂存最新完整输入/输出、请求设置及不透明加密推理，
不写入插件日志或磁盘。上下文缓存最多 64 项、每项 16 MiB、合计 64 MiB，TTL 15 分钟，按访问/写入惰性清理；
活动增量请求另有 64 项、请求及累计流字节合计 64 MiB 的预算，生命周期回调清理。
这些限制按序列化字节计，不是 Go 堆/RSS 上限或安全内存擦除保证。详见 [dev.4 验证与边界](docs/VALIDATION-2026-10-05-dev4.md)。
**不要同时启用 CodexComp 和 CodexReflow 来接管同一模型**，避免嵌套续写或路由递归。

## 本地开发（Windows x64）

需要 Python 3.11+。下载并校验便携 Go / LLVM-MinGW；所有工具和缓存只放在 `.tools/`，不修改系统 PATH：

```powershell
python scripts/bootstrap_windows_tools.py
. ./scripts/dev_env.ps1
go test ./... -count=1
go test ./... -race -count=1
go vet ./...
go test -run '^$' -fuzz '^FuzzDecoderChunkBoundaries$' -fuzztime=15s -parallel=2
./scripts/build_windows.ps1
python scripts/native_smoke.py build/codexreflow.dll --report build/native-smoke.json
```

开发 DLL：`build/codexreflow.dll`。本项目没有自动安装、自动启用插件或修改 Codex 配置的脚本。
原生 smoke test 用 **真实 DLL + 合成 CPA C ABI 宿主回调**；不使用账号、密钥或模型。

有本地 CPA 8.0.13 可执行文件时，可运行更高一级的隔离测试：

```powershell
python scripts/isolated_cpa_smoke.py <CPA可执行文件> build/codexreflow.dll --report build/isolated-cpa-smoke.json
python scripts/isolated_cpa_smoke.py <CPA可执行文件> build/codexreflow.dll --auto-models --report build/isolated-auto-models.json
python scripts/ws_incremental_smoke.py --cpa <CPA可执行文件> --dll build/codexreflow.dll --native-folds --report build/ws-incremental.json
python scripts/ws_incremental_fold_smoke.py --cpa <CPA可执行文件> --dll build/codexreflow.dll --report build/ws-incremental-fold.json
```

使用 CPA 8.0.15 / 8.0.16 时，各命令必须显式追加对应的 `--cpa-version 8.0.15` / `--cpa-version 8.0.16`；测试会核对宿主版本，不自动追随更新。
它启动独立端口、空账号目录、合成 HTTP/WS 上游，仅在临时实例内启用插件，不读取或改写生产配置。
覆盖正常回答、控制行、续写和工具事件；`--auto-models` 另验证无模型配置、旧名单迁移、排除规则、缺少加密状态及默认续写上限。
严格 WS 集另覆盖续写后增量文本、合成工具回传、完整重放、重连和并发连接隔离；新增集验证原生增量
516/1034 的隐藏续写、省略设置的继承、三轮预算、零预算/缺少加密状态、失败/不完整及追加零思考 token。
不等同于实际工具执行、真实模型或 Desktop 验收。固定 CPA 配置重载会关闭上游执行会话，
即使插件关闭也如此；这不是无缝热重载，客户端须以新连接及完整输入恢复。

五平台正式包在原生 CI 上使用 Go `1.26.8` 构建并实际加载测试；本地开发记录为 Windows x64。
这些原生 ABI 结果不替代 Linux/macOS 实际 CPA/HTTP/WS 集成；重建需选择匹配架构的宿主，
完整命令和限制见 [五平台流程](docs/MULTIPLATFORM.md)。

## 默认使用：不需要手写模型列表

全新安装只需在 CPA 的插件界面启用 CodexReflow；不填写 `models`，不必手写 YAML。
这是启用后的默认行为，并不代表插件安装后会擅自自动启用。等价的最小配置如下：

```yaml
plugins:
  configs:
    codexreflow:
      enabled: false # 首次安装先保持关闭，确认验收和回滚方案后再启用
```

默认 `model_mode: auto`：匹配小写 `gpt-5` 及以上标准名称，例如 `gpt-5.6-sol`、
`gpt-6-astra`、`gpt-6-sol`、`gpt-6-luna`；匹配时支持 CPA 路由前缀与末尾推理后缀，
如 `lab/gpt-6-sol(max)`，但不改写请求 ID 或验证后缀能力。
排除名称含 image / audio / realtime / transcribe / transcription / tts / video / embedding(s) / moderation 词段的系列。
新标准名称不需要更新白名单，模型是否可用以及映射至哪个上游仍由 CPA 决定。

**这是请求名称启发式，不是读取或精确同步 CPA 模型目录，也不是自动发现模型能力。**
非标准别名（如 `my-coder`）无法从名称推断，应切换手动模式；标准 GPT 名称的别名也不保证实际指向 GPT。
目前固定 SDK 未提供插件可直接调用的模型目录接口，本实现不轮询管理 API、不读取密钥、不注册新模型。

### 旧配置与可选调整

已有 `models` 配置且没有显式 `model_mode` 时，升级不会扩大原名单。
要改为自动模式，在宿主支持该配置字段的界面选择 `model_mode = auto` 即可；保留的名单不会参与自动匹配。
元数据及隔离 CPA 配置热重载已验证，ECPA 界面实际渲染仍需用户验收。

| 配置 | 实际模型选择 |
|---|---|
| 不填写 `model_mode` 和 `models` | 默认自动模式 |
| 旧的 `models: [具体 ID]` | 手动模式，原始请求 ID 精确匹配，不自动扩展前缀或后缀 |
| 旧的 `models: []` / `null`，无模式 | 保留历史三个 ID：`gpt-5.5`、`gpt-5.6-luna`、`gpt-5.6-terra` |
| 显式 `model_mode: auto` | 自动规则，忽略保留的 `models` |
| 显式 `model_mode: manual` | 只使用 `models`；未填或空名单不接管任何模型 |

高级配置为可选项，不是首次使用要求：

```yaml
model_mode: auto
exclude_models: [gpt-6-luna] # 两种模式都优先排除；此项也排除该 ID 的前缀/后缀形式
max_continue: 3             # 默认最多追加三轮，总计最多四轮，可能增加费用与延迟
max_tier_n: 6
marker_text: "Continue thinking..."
debug_log: false
```

需要手动指定别名时使用 `model_mode: manual` 和 `models: [my-coder]`；名单替换而非追加。
`exclude_models` 不支持通配符或任意别名解析；含前缀的排除项只影响该前缀路由。
`max_continue: 0` 可禁止额外续写；自动命中并不自动续写，仍须符合截断启发式且具备加密推理状态。
实验性的 `min_reasoning_tokens` 默认关闭，不建议为了增加数字而开启。

稳定会话头按优先级读取：`X-CPA-Session-Id`、`X-CodexReflow-Session-Id`、旧的
`X-CodexComp-Session-Id`、`X-Claude-Code-Session-Id`。

## 用量与诊断

Responses 终止事件中的 `metadata.proxy_rounds`、`metadata.proxy_billed_usage` 和
`metadata.proxy_stopped_reason` 保留上游语义。CPA 可能分别记录每个上游轮次；
出现多个 516 行并不等于插件未执行。应核对同一请求的轮次、最终文本、工具调用和真实费用。
其他客户端协议的 metadata 可见性取决于宿主翻译，不作保证。

dev.3 起在终止事件添加 `metadata.proxy_reflow`，并在默认 INFO 日志写入一次 `fold_finished`：

- `run_id`：每次折叠独立生成，不复用宿主请求/连接编号，也不冒充用量执行 ID。
- `rounds_started` / `rounds_completed`：尝试开启轮数 / 已收到终止事件的轮数；后者不保证该轮成功，须结合 `result` 和 `stop_reason`。
- `continuations_started` / `continuations_completed`：扣除首轮后的对应计数，可判断是否追加调用及其终止情况，不是计费结算或质量评分。
- `stop_reason` / `ws_context_bridge`：停止原因 / 父 ID 衔接状态。
- dev.4 原生增量路径另有 `path: ws_incremental`；日志另有 `result` 和 `emission`。`host_accepted` 仅指宿主接受输出；`interceptor_returned` 只指响应钩子返回字节，二者均非客户端送达确认。

父 ID 改写还会记录 `ws_parent_remapped`，携带对应折叠的 `run_id`。
dev.5 另记录同一 `run_id` 的 `fold_started` 和每轮 `round_finished`，支持直接查看各轮 token 序列；
`usage_join: unavailable` 明示尚不能精确连接 ECPA 用量行。可用 `scripts/summarize_diagnostics.py` 只读生成脱敏报告。
新增诊断不含请求、提示词、回答、凭证、原生响应 ID 或加密内容，无须开启 `debug_log`。
没有为所有原生绕过请求生成接管日志；日志缺失本身不能证明失败。
**dev.4 扩展了完整上下文已知的 WS 增量续写，但不会抹去原始 516 记录。** 上下文未命中、预算为零、
缺少加密状态，或追加轮没有新增思考 token 时，最终仍可能是 516；不能仅据这个数字判断是否生效。

## 发布与商店

仓库归属、Go 模块路径和商店草稿使用本项目真实 URL。建仓、正式包验收、发布及文档推送分别获授权；
`v0.1.1` 五平台 Release 已发布并完成公开下载复核，旧版 `v0.1.0` 保留不变。
首个商店 PR #222 已关闭；随后独立获授权重提 [PR #225](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/225)，目前待审核、未合并。
本次仅同步文档，不再提交/评论 PR，不改变生产安装。见 [商店重提记录](docs/STORE-SUBMISSION-2026-10-09-0.1.1.md)、[发布清单](docs/RELEASING.md) 和 [商店提交材料](store/SUBMISSION-DRAFT.md)。
CI 只有读取仓库的权限，只生成候选构件，不自动创建 Release、移动标签、发 PR 或上架。
下一步等待维护者审核，再按反馈处理；生产试装和真实模型测试仍保持独立授权。

## 来源与许可证

MIT。保留 uf-hy 的版权及 CodexCont / codexcomp 的第三方声明。
新项目不冒充上游，未经重新验证不复用上游的效果、平台或兼容性宣传。
历史文档存放在 `docs/upstream/`，只作来源档案，不是当前安装说明。

详细信息见 [LICENSE](LICENSE)、[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和
[THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt)。
