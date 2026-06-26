---
name: video-production-director
description: >
  End-to-end video production orchestration for the content-creation workspace.
  Use when the user asks to make, recreate, package, render, QC, or archive a
  video; when a request could route to HyperFrames, Remotion, captions, TTS,
  download/transcription, website/product videos, motion graphics, or reference
  replication; or when the user needs production planning before editing.
---

# Video Production Director

## Role

Act as the director layer above the existing video skills. Route the job, define
the acceptance standard, then coordinate production and QC. Do not replace
`hyperframes`, `remotion`, `embedded-captions`, `graphic-overlays`,
`下载视频`, `视频转写`, `tts-skill`, or `ai-video-qc-delivery`; load those
skills only when their lane is selected.

## Hard Rules

1. Define the output standard before production: original video, pixel-level
   alignment, visual replica, style-inspired creation, captioned footage,
   narrated explainer, product promo, website tour, or motion graphic.
2. If a reference video is involved, use `reference-video-replica-qc` before
   building. Do not start a remake from intuition.
3. Do not claim pixel-level alignment for a hand-authored HyperFrames/Remotion
   rebuild. Pixel-level requires source-stream reuse, original project assets,
   or hard metrics such as matching hash, `cmp`, PSNR infinity, or SSIM 1.0.
4. Keep source projects and intermediates under
   `/Users/rain/Desktop/内容创作/01-内容生产/视频工作台/`.
5. Archive final deliverable MP4 files under
   `/Users/rain/Desktop/AI视频成品库/`.
6. A video is not complete until media specs, visual checks, and archive paths
   are confirmed.

## Workflow

### 1. Intake

Capture these decisions in plain language:

- goal: teach, promote, recreate, translate, caption, package, or test
- source: brief, script, URL, reference video, existing footage, audio, deck, PR
- platform and ratio: 16:9, 9:16, 1:1, or user-specified
- required tool: HyperFrames, Remotion, ffmpeg, or no preference
- fidelity: pixel-level, visual-level, style-level, or original creative
- final archive slug and expected delivery path

Ask only if the missing answer changes the production path. Otherwise make a
conservative assumption and proceed.

### 2. Route

Read `references/routing.md` and select the narrowest workflow. Prefer an
existing specialized skill over a broad one.

Common routes:

- reference video remake or "align this video" -> `reference-video-replica-qc`
- custom multi-scene HyperFrames video -> `general-video` + `hyperframes`
- short unnarrated motion piece -> `motion-graphics`
- product or SaaS promo -> `product-launch-video`
- website showcase -> `website-to-video`
- captions on footage -> `embedded-captions`
- designed overlay cards on footage -> `graphic-overlays`
- source download -> `下载视频`
- transcription or translation -> `视频转写`
- final archive and QC -> `ai-video-qc-delivery`

### 3. Plan Before Build

Create a production note in the project directory for non-trivial work. Include:

- scene list and timing
- asset list and source paths
- audio/caption plan
- acceptance checks
- known risks or unavailable source assets

For reference-video work, the timing table must come from extracted frames, not
from memory.

### 4. Build

Use the selected execution skill. Keep edits scoped to the project. Do not add
music, captions, scenes, or visual embellishment unless the user's goal needs
them or the selected workflow requires them.

### 5. QC And Archive

Read `references/delivery-gates.md`. At minimum verify:

- final MP4 exists in the workbench and desktop archive
- width, height, frame rate, duration, video codec, audio codec, channels
- representative contact sheets or side-by-side comparisons
- subtitles/audio sync when captions or narration exist
- reference alignment report when a reference video exists

## Output

Return the recommended final MP4 path, the key QC artifact path, confirmed
specs, and any limitation that remains. Keep the response concise.
