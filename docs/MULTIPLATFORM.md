# 五平台候选构建与验收

## 目的与授权边界

商店 [PR #222](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store/pull/222) 因缺少 Linux/macOS 资产被关闭，
[issue #1](https://github.com/LaoPiLao/cpa-plugin-codexreflow/issues/1) 明确要求五个组合：

| GOOS / GOARCH | 原生 GitHub runner | ZIP 根部动态库 |
|---|---|---|
| windows / amd64 | windows-2025 | codexreflow.dll |
| linux / amd64 | ubuntu-24.04 | codexreflow.so |
| linux / arm64 | ubuntu-24.04-arm | codexreflow.so |
| darwin / amd64 | macos-15-intel | codexreflow.dylib |
| darwin / arm64 | macos-15 | codexreflow.dylib |

runner 名称/架构依据 [GitHub 官方列表](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories)
核对（2026-10-09）。使用原生 runner，不把交叉编译成功当作可以加载执行。
工具链固定 Go `1.26.8`，SDK 仍为 CPA `v8.0.13`，运行 Go 实现/策略不变；actions 固定到具体 commit。

`VERSION` 准备为 **`0.1.1`，未发布**。`v0.1.0` ZIP、checksums、标签及此前开发构件保留不动。
本次授权仅为构建/打包修复及工作分支 CI；不发 Release、不移动标签、不重提商店 PR、不安装或启用生产插件、不调用真实模型。
工作流权限为 `contents: read`，仅上传有期限的 CI 候选 artifact，没有自动发布步骤。

## 每个平台的实际检查

`scripts/build_platform.py` 在匹配的 64 位原生主机上执行：

1. 确认源码已提交、宿主/Go 架构一致、CGO 开启、Go/SDK 固定。
2. 对根目录 Go 模块字节快照运行 unit、race、vet 和 15 秒 decoder fuzz，避开 ignored `build` 内的其他项目。
3. 用明确版本和本项目仓库链接生成 **新的** c-shared 动态库，不覆盖原来的非版本化构建。
4. 跑全部 Python 回归和实际库的 31 项 C ABI mock-host 测试；核对库哈希及测试版本。
5. `package_release.py` 检查 PE/ELF/Mach-O 类型与架构，真实加载并读回插件 ID/版本/仓库；只打包动态库及三个保留许可文件。
6. 读回 ZIP、CRC、许可字节和原始库字节，只把已验证的根库写入新路径，重跑同一组 31 项原生测试。
7. 输出同提交/Go 源码指纹/同库的脱敏报告与 validation 记录；不把 raw 日志或配置塞入 ZIP。

输出目录及同名包不可覆盖。校验报告中的 unknown/失败不改成成功，缺一平台或报告不全即失败。
原生 ABI mock 使用合成宿主回调，**不是实际 CPA 进程/HTTP/WS、真实模型或 Desktop 测试**。
同一组 31 项在五种主机重复执行为 155 次；包装后再执行同组 155 次，不宣传为 310 种独立场景。

## 本地使用

需 Python 3.11+、匹配架构的 Go 1.26.8/C 编译器、CGO 开启。
Windows 使用既有、校验下载的项目内工具，先执行 `. ./scripts/dev_env.ps1`；不要在 Windows 上加载 Linux/macOS 库来伪造原生验收。
在已提交源码上选择当前宿主的组合，例如：

```text
python scripts/build_platform.py --goos windows --goarch amd64
python scripts/build_platform.py --goos linux --goarch arm64
python scripts/build_platform.py --goos darwin --goarch arm64
```

默认本地新库：`build/platform-<goos>-<goarch>/`；平台候选：`dist/0.1.1/<goos>_<goarch>/`。
重跑必须选择新的 `--build-dir` / `--output-dir`（仍在 ignored build/dist 下），不删除或覆盖历史输出。

## 五平台汇总

`.github/workflows/platform-packages.yml` 每个原生 job 上传一个 `platform-<goos>-<goarch>` artifact。
下载目录必须恰好包含五个平台子目录。每个子目录包含：

```text
codexreflow_0.1.1_<goos>_<goarch>.zip
checksums.txt
registration.json
native-smoke.json
packaged-native-smoke.json
validation.json
```

汇总命令：

```text
python scripts/assemble_release.py --input-dir .tools/platform-artifacts --output-dir dist/full-platform-candidate --repository https://github.com/LaoPiLao/cpa-plugin-codexreflow
```

汇总器不执行外平台库；验证的是同次可信 CI 的原生报告，不是密码学证明或全面集成认证。
要求所有平台使用同一源码提交及根 Go 指纹，检查注册信息、测试完整性、逐个报告/库/ZIP 哈希、许可字节、架构和无额外文件。
全部通过才生成五个 ZIP、统一五行 SHA256 `checksums.txt` 及独立 `validation-summary.json`；该 JSON 是验收资料，未来不应混入安装 ZIP。

## 仍需独立验收的边界

- 写好 workflow 或合成格式测试通过不代表五平台已实际构建/加载。必须读回 job 和候选字节记录。
- ABI 通过不替代每个平台的实际 CPA 宿主/HTTP/WS；旧 Windows `v0.1.0` 隔离报告或 dev.5 在线样本不移作 `0.1.1` 新构件证明。
- 暂不承诺任意 Linux 发行版/glibc、旧 macOS、macOS 签名/公证、所有宿主/客户端/模型或答案质量。
- 516 不是降智证明；新增构建平台不改变续接成本/隐私或提升质量的保证。

下一步：读回五平台 CI，下载候选并复核；需要实际 CPA 集成时另跑合成隔离宿主测试。
新版 Release、商店重提及生产试装保持独立授权，不因候选 artifact 成功而自动执行。
