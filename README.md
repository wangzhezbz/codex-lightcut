<p align="center">
  <img src="assets/hero-zh.svg" alt="Codex 轻剪：把剪辑交给 Codex，把时间留给创作。后台剪辑，可编辑草稿。开发中。" width="100%">
</p>

<p align="center">
  <a href="docs/platforms.md#macos"><img src="assets/platform-macos.svg" alt="macOS：本机流程已验证，尚无通用安装包。查看兼容说明。" width="49%"></a>
  <a href="docs/platforms.md#windows"><img src="assets/platform-windows.svg" alt="Windows：基础适配开发中，等待实机验收。查看测试进度。" width="49%"></a>
</p>

<p align="center">
  <strong>简体中文</strong> · <a href="README.en.md">English</a>
</p>
<p align="center">
  <a href="docs/getting-started.md">从这里开始</a> ·
  <a href="docs/capabilities.md">功能与边界</a> ·
  <a href="docs/roadmap.md">开发路线</a> ·
  <a href="CHANGELOG.md">更新记录</a> ·
  <a href="docs/licensing.md">许可说明</a>
</p>

## 让 Codex 帮你完成剪辑初稿

**Codex LightCut · Codex 轻剪**，面向 macOS 与 Windows 的后台视频剪辑项目。目标是让 Codex 根据素材和要求处理剪切、字幕、封面与声音，交付可以在剪映继续调整的草稿。

视频、字幕和音乐保留独立轨道。制作过程不主动打开剪映、不模拟键鼠；草稿登记遇到编辑器运行时等待自然退出。你可以继续工作，在方便时打开草稿检查和精修。

> **当前是早期开发阶段。** 本仓库提供原创项目介绍、静态展示页和开发文档，尚未发布可安装的剪辑程序或运行引擎。下表所列实现来自本地研究版本，不能通过克隆这个公开仓库直接运行。Windows 尚未完成实机验收。

## 一条素材，到可继续编辑的草稿

```text
素材 + 剪辑要求
      ↓
Codex 分析内容，形成剪辑计划
      ↓
后台处理素材、字幕、封面与声音
      ↓
校验素材、时间线及固定参数
      ↓
生成草稿 → 等待可登记时机 → 你打开并精修
```

内容取舍和气口判断目前仍有 Agent 分析与人工复核环节。自动质检能发现参数和文件问题，不能替代实际画面与听感验收。

## 已经做到哪一步

| 能力 | 本地研究版本 | 公开交付状态 |
| :--- | :--- | :--- |
| 可编辑时间线 | 多轨、剪切、普通变速、字幕与素材引用 | 工程格式与开发说明整理中 |
| macOS 草稿 | 匹配的剪映 11.5.0 本机环境已交付真实口播草稿 | 尚无通用安装包 |
| Windows 草稿 | 基础构建、校验和登记入口已接入候选代码 | DLL、登记、保存重开待实机验收 |
| 美颜、滤镜、调色 | Mac 指定本机资源已适配，部分既有样片得到用户确认 | Windows 原生资源适配待完成 |
| 字幕与声音 | 单行字幕参数、固定字幕位置、人声与 BGM 独立音量校验 | 不代表所有画布与版本均已验证 |
| 封面 | 已在真实项目中使用新生成封面与首帧封面 | 自动生图流程尚未作为独立功能发布 |
| 气口处理 | 已做波形对比和局部精修 | 词级强制对齐与稳定听感仍需完善 |
| 后台队列与缓存 | 本地已实现；登记时等待编辑器自然退出 | 资源占用与完整耗时继续测试 |

完整矩阵见 [功能与边界](docs/capabilities.md)。**“后台”不等于不消耗资源，“代码测试通过”不等于两端原生播放通过。**

## 怎么开始

- **想了解或试用**：先看 [使用与试用说明](docs/getting-started.md)，以及 [平台兼容性](docs/platforms.md)。当前没有公开安装包。
- **愿意协助 Windows 测试**：看 [验收步骤](docs/testing.md)，通过 Issue 提供脱敏后的环境信息。
- **想参与开发**：阅读 [协作指南](CONTRIBUTING.md) 和 [架构说明](docs/architecture.md)。
- **只想看展示页面**：本仓库根目录的 `index.html` 可离线打开；它是产品介绍页，不是剪辑客户端。

## 当前验证记录

截至 **2026-09-23**，本地 Studio 的 50 项测试、Windows 候选引擎的 64 项测试通过；另完成了 Mac 宿主上的 Windows 分支模拟构建。该模拟使用测试替身，不加载 Windows DLL，也不能证明 Windows 渲染或播放正确。

Mac 原引擎保持独立，本机运行身份检查通过。这些数字是本地研究记录，不是本公开仓库的 CI 成绩。公开仓库只校验文档、链接及展示资源。

性能会分别记录首次准备、转写、素材处理、草稿构建和验收耗时；在完成基准前，不承诺“所有视频几秒剪完”。

## 来源、许可与关系

本地研究参考了 [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless) 及其 [Windows PR #15](https://github.com/mcncarl/jianying-headless/pull/15)。感谢原作者公开研究成果。受其许可范围限制，本仓库不分发该引擎、修改版或对应测试包。

本仓库原创展示页面、文档及检查脚本使用 [MIT 许可](LICENSE)。MIT 不扩展到未包含的第三方引擎、剪映程序、字体、音乐或效果资源，详见 [许可范围](docs/licensing.md)。

这是独立社区项目，与 OpenAI、剪映及其他同名产品不存在官方隶属关系。名称中的 Codex 表示预期协作方式，不代表官方出品。
