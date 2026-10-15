# CodexReflow · 续流

**让符合条件的 GPT 请求自动接着生成。**

CodexReflow 是一个 [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)（CPA）插件。当 GPT 的一次推理疑似提前结束时，插件会在满足条件的情况下继续请求模型，把多轮结果合并后返回客户端。适合已经通过 CPA 使用 Codex 或其他兼容客户端的用户。

[English](README_EN.md) · [下载 v0.1.1](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/tag/v0.1.1) · [反馈问题](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/new?template=bug_report.md)

## 它能做什么

- **自动续接**：满足条件时继续生成，默认最多追加 3 轮。
- **兼容 HTTP 和 WebSocket**：处理两种连接方式下的流式输出，包括 HTTP/SSE。
- **省去模型名单维护**：新配置默认按名称匹配 GPT-5 及以上的标准文本模型。

续接会消耗额外 token，也可能增加等待时间。它不保证模型一定想得更多、回答一定更好。

## 安装与使用

推荐从 **CPA / ECPA 插件商店**安装：

1. 打开「插件 → 插件商店」，搜索 **CodexReflow**。
2. 点击安装。需要填写版本时，可填 `v0.1.1`；留空则使用仓库的最新发布版。
3. 在本地插件列表中启用 CodexReflow，确认显示为运行中。
4. 正常使用原来的客户端即可。**全新配置不需要手写 YAML，也不需要填写模型列表。**

如果正在使用 CodexComp，请先停用它，避免两个插件同时处理同一模型。

已有用户可以通过「选择版本」更新。更新前保留旧插件和配置，并等当前回答结束后再操作。

<details>
<summary>手动下载 v0.1.1</summary>

按操作系统和 CPU 架构选择安装包：

| 平台 | 安装包 |
|---|---|
| Windows x64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_windows_amd64.zip) |
| Linux x64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_amd64.zip) |
| Linux ARM64 | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_linux_arm64.zip) |
| macOS Intel | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_amd64.zip) |
| macOS Apple Silicon | [下载](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/codexreflow_0.1.1_darwin_arm64.zip) |

下载后可用 [checksums.txt](https://github.com/LaoPiLao/cpa-plugin-codexreflow/releases/download/v0.1.1/checksums.txt) 核对 SHA256。各平台的测试范围和已知限制见[兼容性说明](docs/COMPATIBILITY.md)。

</details>

## 需要改配置吗？

**大多数用户直接使用默认设置即可。**

| 项目 | 默认行为 |
|---|---|
| 模型选择 | 自动匹配标准 GPT 文本模型名称，例如 `gpt-6-astra`、`gpt-6-sol`、`gpt-6-luna` |
| 续接次数 | 最多追加 3 轮；加上首次请求，最多 4 轮 |
| 排除模型 | 不自动匹配名称带有图片、音频、实时语音等非文本标记的系列 |
| 调试日志 | 默认关闭；基本续接诊断仍可查看 |

自动匹配依据的是**请求中的模型名称**，不是同步 CPA 的模型目录。像 `my-coder` 这样的自定义别名，需要手动指定。

如果以前填过 `models` 名单，升级会保留旧的选择方式。想改用自动匹配，可将 `model_mode` 设为 `auto`。

需要排除某个模型、减少续接次数或使用自定义别名时，再看[配置说明](docs/CONFIGURATION.md)。

## 常见问题

### 为什么使用记录里还有 516？

CPA 可能分别记录首轮和续接轮。即使插件已经续接，首轮的 516 也会保留；续接轮也可能没有新增思考 token。

因此，**516 没消失不代表插件没生效，出现 516 也不能证明模型降智**。插件使用的是特定数字模式和上游推理状态，不是看到每个 516 都无条件追加请求。

### 怎么确认它真的续接了？

先确认插件显示为运行中，再查看同一次请求的续接日志：有没有追加轮次、最终是正常完成还是出错。客户端是否收到回答，也要一起看。

具体字段和日志汇总方法见[诊断说明](docs/DIAGNOSTICS.md)。只看插件开关或某一条 token 数，判断不了完整结果。

### WebSocket 也能用吗？

支持。后续轮次的续接需要插件掌握完整上下文，并拿到上游可用于续接的推理状态。上下文缺失、过期或超过缓存限制时，该请求可能不会续接。详细条件见[兼容性说明](docs/COMPATIBILITY.md)。

### 启用后卡住或报错怎么办？

可以先停用 CodexReflow，再用同一模型正常聊天，确认问题是否随插件停用而消失。反馈时提供 CPA / ECPA、插件和客户端版本，以及脱敏后的错误信息即可。

请不要上传密钥、账号、完整配置或原始聊天记录。[提交问题](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/new?template=bug_report.md)

## 数据与隐私

为了衔接多轮请求，插件会在进程内存中临时缓存上下文和加密推理状态。默认诊断日志不包含提示词、回答、凭证或加密推理内容。

CPA 和其他插件的日志由各自的设置决定。缓存范围、容量和有效期见[兼容性说明](docs/COMPATIBILITY.md)。

## 更多资料

- [配置说明](docs/CONFIGURATION.md)：自动 / 手动模式、排除名单、续接次数和旧配置迁移。
- [诊断说明](docs/DIAGNOSTICS.md)：如何查看续接轮次、停止原因和用量。
- [兼容性与测试记录](docs/COMPATIBILITY.md)：已经验证的范围和已知限制。
- [开发指南](CONTRIBUTING.md) · [五平台构建](docs/MULTIPLATFORM.md) · [发布流程](docs/RELEASING.md) · [更新记录](CHANGELOG.md)。

## 来源与许可证

本项目基于 [uf-hy / CodexComp v0.1.7](https://github.com/uf-hy/cpa-plugin-codexcomp/tree/v0.1.7) 独立维护，保留上游版权及 CodexCont 相关声明。它不是 OpenAI 或 CLIProxyAPI 官方插件。

采用 [MIT 许可证](LICENSE)。第三方来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 [THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt)。
