# Video Production Skills

面向 AI 视频创作与复刻的三件套 skill：参考视频拆解与对齐质检、暗色 SaaS / AI 产品风格短片，以及黑底白字开场动画。

这些 skill 适用于 Codex、Claude Code、Cursor 等支持本地 skill 目录或 Skills CLI 的 AI 编程/创作代理。仓库中的每个一级目录都是一个独立可安装的 skill。

## 包含的 Skills

| Skill | 作用 |
| --- | --- |
| `reference-video-replica-qc` | 参考视频复刻质检：按 0.5 秒抽帧、生成时间线、对比候选视频、区分像素级 / 视觉级 / 风格级对齐。 |
| `dark-saas-magic-video` | 暗色 cinematic SaaS / AI 产品短片风格：黑色空间舞台、底部紫色辉光、动感大字、渐变 CTA、漂浮 UI、模型环和导出物件。 |
| `black-white-text-opener` | 新视频开场动画：纯黑/近黑背景、白色大字逐字打出、同步打字音效、词语替换，并干净转入正片。 |

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

做参考视频复刻或像素级对齐时，优先使用 `reference-video-replica-qc`；做同风格原创短片时，使用 `dark-saas-magic-video`；做黑底白字、逐字打字、打字音效、字体变化类开场时，使用 `black-white-text-opener`。

## 怎么选择

| 你想做什么 | 使用 |
| --- | --- |
| 复刻参考视频、逐帧分析、判断是否对齐 | `reference-video-replica-qc` |
| 做类似 Presenton 的暗色 SaaS / AI 产品短片 | `dark-saas-magic-video` |
| 给新视频加一段黑底白字逐字打字开场 | `black-white-text-opener` |

## 黑底白字开场

`black-white-text-opener` 默认制作这种开场：

1. 纯黑或近黑背景先保持一小段时间。
2. 白色文字一个字一个字出现。
3. 每个可见字符对应一个轻微 typing click 音效。
4. 中间可以切换关键词或第二段文案。
5. 最后一行文字短暂停留，再转入正片。

它会生成可执行的 timing plan，里面包含：

- `typing_events`：每个字符出现的时间点。
- `sfx_events`：每个打字音效的时间点、音量和轻微 pitch 变化。
- `warnings`：如果文案太长、打字速度过快，会提示缩短文案或拉长时长。

示例：

```bash
python3 black-white-text-opener/scripts/create_opener_plan.py \
  --title "我开源了 视频复刻 Skill" \
  --replace "HyperFrames" "Remotion" \
  --final "就能够复刻。" \
  --preset slow \
  --typing-cps 12 \
  --out opener-plan.json
```

## 典型用法

- "每 0.5 秒抽帧，拆解参考视频并检查新视频是否对齐。"
- "做一个类似 Presenton 那种暗色 SaaS magic UI 风格的产品短片。"
- "做一个黑底白字开场，白色文字一个个打出来，并配合打字音效。"

## 设计边界

- `reference-video-replica-qc` 不会凭感觉宣称像素级对齐；像素级需要硬证据，例如一致哈希、`cmp` 通过、PSNR infinity 或 SSIM 1.0。
- `dark-saas-magic-video` 是风格级创作 skill，不用于逐帧复刻。
- `black-white-text-opener` 是生成型开场 skill，默认要求逐字打字和同步 typing click 音效；不用于复用原片或声明像素级对齐。

<details>
<summary>English</summary>

# Video Production Skills

Three skills for AI video production:

- `reference-video-replica-qc`: evidence-driven reference video analysis and comparison, including 0.5-second frame extraction and pixel/visual/style fidelity classification.
- `dark-saas-magic-video`: dark cinematic SaaS/product motion style inspired by magic UI product videos.
- `black-white-text-opener`: reusable black-background openers where white text types in character by character with timed typing clicks.

Recommended install:

```bash
npx skills add https://github.com/Pluviobyte/video-production-skills --list
npx skills add https://github.com/Pluviobyte/video-production-skills --skill reference-video-replica-qc
npx skills add https://github.com/Pluviobyte/video-production-skills --skill dark-saas-magic-video
npx skills add https://github.com/Pluviobyte/video-production-skills --skill black-white-text-opener
```

These skills are designed for Codex, Claude Code, Cursor, and other agents that support local skills or the Skills CLI.

## Choosing A Skill

| Goal | Use |
| --- | --- |
| Analyze, recreate, or verify reference-video alignment | `reference-video-replica-qc` |
| Create a dark cinematic SaaS/product short | `dark-saas-magic-video` |
| Create a black-background opener with typed white text and typing clicks | `black-white-text-opener` |

`black-white-text-opener` generates a timing plan with `typing_events`,
`sfx_events`, and warnings for copy that is too long for the selected cadence.

</details>
