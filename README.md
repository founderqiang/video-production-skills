# Video Production Skills

面向 AI 视频创作与复刻的三件套 skill：参考视频拆解与对齐质检、暗色 SaaS / AI 产品风格短片，以及黑底白字开场动画。

这些 skill 适用于 Codex、Claude Code、Cursor 等支持本地 skill 目录或 Skills CLI 的 AI 编程/创作代理。仓库中的每个一级目录都是一个独立可安装的 skill。

## 包含的 Skills

| Skill | 作用 |
| --- | --- |
| `reference-video-replica-qc` | 参考视频复刻质检：按 0.5 秒抽帧、生成时间线、对比候选视频、区分像素级 / 视觉级 / 风格级对齐。 |
| `dark-saas-magic-video` | 暗色 cinematic SaaS / AI 产品短片风格：黑色空间舞台、底部紫色辉光、动感大字、渐变 CTA、漂浮 UI、模型环和导出物件。 |
| `black-white-text-opener` | 新视频开场动画：纯黑/近黑背景、白色大字、渐显/模糊变清晰/打字/词语替换，并干净转入正片。 |

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

做参考视频复刻或像素级对齐时，优先使用 `reference-video-replica-qc`；做同风格原创短片时，使用 `dark-saas-magic-video`；做黑底白字、文字渐显、字体变化类开场时，使用 `black-white-text-opener`。

## 典型用法

- "每 0.5 秒抽帧，拆解参考视频并检查新视频是否对齐。"
- "做一个类似 Presenton 那种暗色 SaaS magic UI 风格的产品短片。"
- "做一个黑底白字开场，文字逐渐出来，然后切入正片。"

## 设计边界

- `reference-video-replica-qc` 不会凭感觉宣称像素级对齐；像素级需要硬证据，例如一致哈希、`cmp` 通过、PSNR infinity 或 SSIM 1.0。
- `dark-saas-magic-video` 是风格级创作 skill，不用于逐帧复刻。
- `black-white-text-opener` 是生成型开场 skill，不用于复用原片或声明像素级对齐。

<details>
<summary>English</summary>

# Video Production Skills

Three skills for AI video production:

- `reference-video-replica-qc`: evidence-driven reference video analysis and comparison, including 0.5-second frame extraction and pixel/visual/style fidelity classification.
- `dark-saas-magic-video`: dark cinematic SaaS/product motion style inspired by magic UI product videos.
- `black-white-text-opener`: reusable black-background white-text opening animations for new videos.

Recommended install:

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --list
npx skills add https://github.com/Pluviobyte/video-production-skills --skill reference-video-replica-qc
npx skills add https://github.com/Pluviobyte/video-production-skills --skill dark-saas-magic-video
npx skills add https://github.com/Pluviobyte/video-production-skills --skill black-white-text-opener
```

These skills are designed for Codex, Claude Code, Cursor, and other agents that support local skills or the Skills CLI.

</details>
