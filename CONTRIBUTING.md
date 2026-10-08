# 维护流程

1. 用最小、脱敏的合成事件复现问题，区分客户端 → CPA、宿主 → 插件、插件 → 客户端三段。
2. 改动解码、折叠、终止事件、用量或格式声明时，新增对应回归测试。
3. 固定宿主/SDK 版本；升级时分别跑 HTTP、WS 和不同客户端协议，不把 HTTP 回退计为 WS 成功。
4. Windows 开发命令见 README；`scripts/native_smoke.py` 通过真实 DLL 调用 C ABI，但它不是 CPA 宿主集成测试。
5. 测试记录必须写明日期、版本、场景、实际传输和证据等级；不要上传账号、请求原文、加密推理或生产数据库。
6. 发布是单独步骤，按 `docs/RELEASING.md` 执行。故障版本不移动旧标签，用新的补丁版本修复。

开发和修复使用工作分支；`origin` 指向 [LaoPiLao/cpa-plugin-codexreflow](https://github.com/LaoPiLao/cpa-plugin-codexreflow)，
`upstream` 保留 [uf-hy/cpa-plugin-codexcomp](https://github.com/uf-hy/cpa-plugin-codexcomp)。保留上游历史和本地
`v0.1.7` 来源标签，不把继承的标签当作新插件的正式版本推送；代码推送不等于 Release 或商店提交授权。

维护目录的本地 `v0.1.0` 同样继承自 CodexComp，保留不动；Reflow 的远程 `v0.1.0` 指向
实际被测源码 `875864934cf82dbba90a7f85985f36ebd3a256d1`。不要整批推送/强制同步标签；
使用明确源码 SHA 或新检出验证版本，详见 [发布记录](docs/RELEASE-2026-10-08-0.1.0.md)。
