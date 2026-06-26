# Video Production Skills

这是一个长期维护的 AI 视频制作 skill 总库，用来沉淀我在视频创作、视频复刻、动效生成、片头包装、质检交付等流程中反复使用的方法。

仓库不是只服务于某一个视频项目。后续所有和视频制作有关的 skill 都会优先收录在这里，并按“视频类型 / 风格 / 工作流环节”持续扩展。当前首批收录的是参考视频复刻质检、暗色 SaaS / AI 产品短片、黑底白字打字开场。

这些 skill 适用于 Codex、Claude Code、Cursor 等支持本地 skill 目录或 Skills CLI 的 AI 编程/创作代理。仓库中的每个一级目录都是一个独立可安装的 skill。

## 已收录 Skills

| Skill | 视频制作环节 | 适合做什么 | 视频风格 / 方法 | 详情 |
| --- | --- | --- | --- | --- |
| `reference-video-replica-qc` | 复刻分析 / 质检 | 参考视频拆解、复刻对齐、像素/视觉级质检 | 证据驱动：0.5 秒抽帧、时间线报告、对照图、PSNR/SSIM/哈希验证 | [查看页面](docs/reference-video-replica-qc.md) |
| `dark-saas-magic-video`<br>暗色 SaaS 魔术短片 | 风格化正片生成 | 暗色 SaaS / AI 产品短片、工具发布视频、产品能力展示 | Presenton-like magic UI：黑色空间、底部紫光、动感大字、渐变 CTA、漂浮 UI、模型环、导出物件 | [查看页面](docs/dark-saas-magic-video.md) |
| `black-white-text-opener` | 片头包装 | 新视频片头、教程开场、观点视频开头、产品视频引子 | 纯黑/近黑背景 + 白色大字逐字打出 + 同步 typing click 音效 + 干净转场 | [查看页面](docs/black-white-text-opener.md) |

## 效果预览

### 黑底白字打字开场

[播放 MP4](https://github.com/Pluviobyte/video-production-skills/blob/main/assets/videos/black-white-text-opener-preview.mp4)

<video src="./assets/videos/black-white-text-opener-preview.mp4" controls playsinline width="100%"></video>

### 暗色 SaaS / Magic UI

[播放预览 MP4](https://github.com/Pluviobyte/video-production-skills/blob/main/assets/videos/dark-saas-magic-video-preview.mp4)

<video src="./assets/videos/dark-saas-magic-video-preview.mp4" controls muted loop playsinline width="100%"></video>

完整示例成片：**雪踏乌云暗色 SaaS 介绍短片**

[播放完整成片 MP4](https://github.com/Pluviobyte/video-production-skills/blob/main/dark-saas-magic-video/assets/showcases/xuetawuyun-dark-saas-showcase-1080p.mp4)

<video src="./dark-saas-magic-video/assets/showcases/xuetawuyun-dark-saas-showcase-1080p.mp4" controls playsinline width="100%"></video>

### 参考视频复刻质检

[播放 MP4](https://github.com/Pluviobyte/video-production-skills/blob/main/assets/videos/reference-video-replica-qc-preview.mp4)

<video src="./assets/videos/reference-video-replica-qc-preview.mp4" controls muted loop playsinline width="100%"></video>

## 仓库会如何扩展

后续新增的视频制作 skill，会优先按下面几类组织：

- 复刻与质检：参考视频拆解、时间线还原、像素级/视觉级对齐、交付检查。
- 片头与包装：黑底白字、标题卡、章节转场、字幕条、CTA 结尾。
- 风格化正片：暗色 SaaS、AI 工具发布、课程预告、观点口播包装、教程动效。
- 素材处理：抽帧、字幕、配音、屏幕录制清理、音画同步。
- 平台适配：抖音、小红书、公众号视频封面/比例/节奏差异。

每个新增 skill 应该同时包含：

- 一个独立 skill 目录，包含 `SKILL.md` 和必要脚本。
- 一个 `docs/<skill-name>.md` 介绍页，说明视频类型、风格、适合/不适合场景。
- 优先提供 MP4 视频预览，放在 `assets/videos/` 或 skill 自己的 `assets/showcases/`。
- 抽帧图、contact sheet、对照图只作为封面/质检辅助，放在 `assets/images/`。
- 在本 README 的表格中补充一行，说明它属于哪个视频制作环节。

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

## 设计边界

- `reference-video-replica-qc` 不凭感觉宣称像素级对齐；像素级需要一致哈希、`cmp`、PSNR infinity 或 SSIM 1.0 等硬证据。
- `dark-saas-magic-video` 是风格级创作 skill，不用于逐帧复刻。
- `black-white-text-opener` 是生成型开场 skill，默认要求逐字打字和同步 typing click 音效；不用于复用原片或声明像素级对齐。

<details>
<summary>English</summary>

# Video Production Skills

This is a long-term AI video production skills library. It is designed to collect reusable skills for video creation, recreation, motion design, opener packaging, asset processing, and delivery QA.

The repository is not limited to the first three skills. Future video-production skills should be added here with a dedicated skill directory, a docs page, and preview media when possible.

| Skill | Production Stage | Video Type | Style / Method |
| --- | --- | --- | --- |
| `reference-video-replica-qc` | Recreation analysis / QA | Reference video analysis, recreation QC, alignment verification | Evidence-driven frame extraction, timelines, side-by-side review, hard metrics |
| `dark-saas-magic-video` / Dark SaaS Magic Short | Styled main video | Dark SaaS / AI product shorts | Presenton-like magic UI with black space, purple glow, kinetic type, gradient CTA, floating UI |
| `black-white-text-opener` | Opener packaging | Opening title cards for new videos | Black background, typed white text, timed typing clicks, clean transition |

Recommended install:

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --list
npx skills add https://github.com/Pluviobyte/video-production-skills --skill reference-video-replica-qc
npx skills add https://github.com/Pluviobyte/video-production-skills --skill dark-saas-magic-video
npx skills add https://github.com/Pluviobyte/video-production-skills --skill black-white-text-opener
```

These skills are designed for Codex, Claude Code, Cursor, and other agents that support local skills or the Skills CLI.

</details>
