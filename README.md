# Video Production Skills

面向 AI 视频创作与复刻的三件套 skill：参考视频复刻质检、暗色 SaaS / AI 产品风格短片、黑底白字打字开场。

这些 skill 适用于 Codex、Claude Code、Cursor 等支持本地 skill 目录或 Skills CLI 的 AI 编程/创作代理。仓库中的每个一级目录都是一个独立可安装的 skill。

## Skill 导览

| Skill | 做什么类型的视频 | 视频风格 | 详情 |
| --- | --- | --- | --- |
| `reference-video-replica-qc` | 参考视频拆解、复刻对齐、像素/视觉级质检 | 证据驱动的复刻工作流：0.5 秒抽帧、时间线报告、对照图、PSNR/SSIM/哈希验证 | [查看页面](docs/reference-video-replica-qc.md) |
| `dark-saas-magic-video` | 暗色 SaaS / AI 产品短片、工具发布视频、产品能力展示 | Presenton-like magic UI：黑色空间、底部紫光、动感大字、渐变 CTA、漂浮 UI、模型环、导出物件 | [查看页面](docs/dark-saas-magic-video.md) |
| `black-white-text-opener` | 新视频片头、教程开场、观点视频开头、产品视频引子 | 纯黑/近黑背景 + 白色大字逐字打出 + 同步 typing click 音效 + 干净转场 | [查看页面](docs/black-white-text-opener.md) |

## 效果预览

### 黑底白字打字开场

<video src="./assets/videos/black-white-text-opener-preview.mp4" controls playsinline width="100%"></video>

### 暗色 SaaS / Magic UI

<video src="./assets/videos/dark-saas-magic-video-preview.mp4" controls muted loop playsinline width="100%"></video>

### 参考视频复刻质检

<video src="./assets/videos/reference-video-replica-qc-preview.mp4" controls muted loop playsinline width="100%"></video>

## 推荐安装

先查看仓库内可安装的 skill：

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --list
```

按需安装单个 skill：

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --skill reference-video-replica-qc
npx skills add https://github.com/Pluviobyte/video-production-skills --skill dark-saas-magic-video
npx skills add https://github.com/Pluviobyte/video-production-skills --skill black-white-text-opener
```

## 怎么选择

- 要复刻一个已有视频、拆解时间线、验证是否对齐：用 `reference-video-replica-qc`。
- 要做暗色科技感 SaaS / AI 产品短片：用 `dark-saas-magic-video`。
- 要给新视频加黑底白字、逐字打字、打字音效开场：用 `black-white-text-opener`。

## 典型用法

- "每 0.5 秒抽帧，拆解参考视频并检查新视频是否对齐。"
- "做一个类似 Presenton 那种暗色 SaaS magic UI 风格的产品短片。"
- "做一个黑底白字开场，白色文字一个个打出来，并配合打字音效。"

## 设计边界

- `reference-video-replica-qc` 不凭感觉宣称像素级对齐；像素级需要一致哈希、`cmp`、PSNR infinity 或 SSIM 1.0 等硬证据。
- `dark-saas-magic-video` 是风格级创作 skill，不用于逐帧复刻。
- `black-white-text-opener` 是生成型开场 skill，默认要求逐字打字和同步 typing click 音效；不用于复用原片或声明像素级对齐。

<details>
<summary>English</summary>

# Video Production Skills

Three reusable skills for AI video work:

| Skill | Video Type | Style |
| --- | --- | --- |
| `reference-video-replica-qc` | Reference video analysis, recreation QC, alignment verification | Evidence-driven frame extraction, timelines, side-by-side review, hard metrics |
| `dark-saas-magic-video` | Dark SaaS / AI product shorts | Presenton-like magic UI with black space, purple glow, kinetic type, gradient CTA, floating UI |
| `black-white-text-opener` | Opening title cards for new videos | Black background, typed white text, timed typing clicks, clean transition |

Recommended install:

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --list
npx skills add https://github.com/Pluviobyte/video-production-skills --skill reference-video-replica-qc
npx skills add https://github.com/Pluviobyte/video-production-skills --skill dark-saas-magic-video
npx skills add https://github.com/Pluviobyte/video-production-skills --skill black-white-text-opener
```

These skills are designed for Codex, Claude Code, Cursor, and other agents that support local skills or the Skills CLI.

</details>
