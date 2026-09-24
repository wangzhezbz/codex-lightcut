<p align="center"><img src="assets/hero-en.svg" alt="Codex LightCut — Let Codex handle the edit. Keep your time for the story." width="100%"></p>

<p align="center"><a href="README.md">简体中文</a> · <strong>English</strong></p>
<p align="center"><a href="docs/getting-started.md">Get started</a> · <a href="docs/capabilities.md">Capabilities</a> · <a href="docs/roadmap.md">Roadmap</a> · <a href="docs/licensing.md">Licensing</a></p>

## Background editing. An editable draft.

**Codex LightCut** is an early-stage project for Codex-assisted video editing on macOS and Windows. Its goal is to turn source footage and editing instructions into a Jianying draft with separate video, caption and audio tracks, ready for you to refine.

The local workflow prepares and validates drafts without launching the editor or simulating keyboard and mouse input. Registration waits while the editor is running. Background work still consumes system resources.

**This public repository currently contains original presentation assets, documentation and their validation script. It does not contain a runnable editing engine or an installer.** The implementation described below exists in a separate local research workspace.

| Platform | Local research status | Public availability |
| --- | --- | --- |
| macOS | Real talking-head drafts delivered in a matching Jianying 11.5.0 environment | No general-purpose installer |
| Windows | Tested native builds, registration, effects and R8.1 caption-seam sample | Other versions, save/reopen and clean-machine delivery pending |

Local work covers cuts, basic speed changes, subtitles, covers, independent speech/BGM settings, and selected Mac-native beauty/color effects. Acoustic forced alignment, a desktop application and a full end-to-end benchmark remain unfinished. Content decisions and listening checks still require review.

As of 2026-09-24, the Windows R8.1 handoff reports 44 passing checks. A real caption-seam sample was registered and accepted by the user. This applies to the tested environment, not arbitrary footage or versions. See the [R8.1 record](docs/release-r81.md).

## Explore

- [Getting started](docs/getting-started.md): availability and a sample editing brief.
- [Platform compatibility](docs/platforms.md): version scope and testing boundaries.
- [Development roadmap](docs/roadmap.md): completed work and acceptance criteria.
- [Contributing](CONTRIBUTING.md): documentation, design and compatibility feedback.
- Open `index.html` locally to view the static project page. It is a presentation, not an editing application. Detailed development documents are currently in Chinese.

## Attribution and license

Local research references [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless), including [Windows PR #15](https://github.com/mcncarl/jianying-headless/pull/15). Its restricted engine and modified research package are **not distributed here**.

Original materials in this public repository use the [MIT license](LICENSE). This does not license external engines, Jianying, fonts, music or effect resources. See [licensing scope](docs/licensing.md).

Independent community project. Not affiliated with or endorsed by OpenAI, Jianying or other similarly named products.

## Supported Jianying version

Currently adapted to Jianying Pro **11.5.0** on macOS and Windows; the verified Windows build is **11.5.0.14471**. Compatibility work will follow future Jianying releases. New versions are supported only after verification, not automatically on release.
