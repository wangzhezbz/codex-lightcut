# Codex LightCut R8.2

版本0.4.2-preview.1。包含LightCut插件、运行源码、Mac/Windows草稿引擎和依赖安装器。剪映专业版需用户自行安装。

## 支持范围

当前适配剪映专业版 **11.5.0**，Windows 已验收构建 **11.5.0.14471**。后续跟随剪映版本更新持续适配，新版本通过验证后再支持。应用原生组件仍按摘要检查，不能自行跳过。

## 交给 Codex 安装

解压到新目录，保留旧程序和数据。让Codex读取skills/lightcut/SKILL.md，校验PACKAGE_SHA256.json，然后执行本机入口：Mac为`bash install-mac.command --with-asr`，Windows为`powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File install-windows.ps1 -WithAsr`。入口自动选择包内对应平台的引擎，无需用户寻找来源或提供EngineFrom。已有环境继续沿用原LIGHTCUT_DATA_HOME，不清缓存。

安装会联网准备独立Python、媒体工具和可选语音模型；不修改系统PATH。剪映应用和官方效果资源不在包内，效果根据实际选择及账号权益准备。全程不打开、关闭或激活剪映，不自动播放声音。

首次只询问缺少的封面、画面效果、音乐、字幕和节奏选择。封面生成提供五种起始风格并展示成图确认。已有偏好直接沿用，不让用户选测试修改项。制作交付可编辑草稿，登记时等待编辑器自然退出，既有草稿不覆盖。

## 升级验证

由Codex使用environment/runtime.json里的Python执行`install/check_install.py --out <新结果目录>`，回传LightCut-R82-Install-Results.zip。确认引擎来源为current-package、对应摘要全部匹配。已验收视频不必重剪。R8.1字幕接缝逻辑保留，打包方式改变需要两端分别验证；Mac检查不能替代Windows实机安装。全部新机效果和保存重开不因打包完成自动宣称通过。

## 许可

运行组件按项目负责人确认的权利人授权集成。独立依赖的许可文本在包内licenses目录保留；剪映、字体、音乐和官方资源各自的权益不因本包改变。不得将本包许可解释为拥有剪映应用或会员素材的再分发权。
