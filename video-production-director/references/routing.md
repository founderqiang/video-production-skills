# Video Production Routing

Use the narrowest skill that fits. Do not stack multiple creation workflows
unless the task truly crosses boundaries.

| User intent | Primary route | Notes |
| --- | --- | --- |
| "复刻这个视频", "对齐这个视频", "像素级" | `reference-video-replica-qc` | Must analyze reference first. |
| Existing talking-head footage + subtitles | `embedded-captions` | For caption styling and burn-in. |
| Existing footage + graphic cards/callouts | `graphic-overlays` | For designed overlays, not plain subtitles. |
| Product / SaaS launch / feature reveal | `product-launch-video` | Use product visuals and marketing structure. |
| Dark Presenton-like SaaS magic UI style | `dark-saas-magic-video` | Use for style-level creation, not exact replication. |
| General website showcase | `website-to-video` | Use when it is not a launch/promo. |
| Topic explainer with generated narration | `faceless-explainer` | For arbitrary text/topic to narrated video. |
| Longer custom multi-scene piece | `general-video` | Fallback when no specialized lane fits. |
| Short kinetic type/logo/stat/overlay | `motion-graphics` | Usually under 10s, no narration arc. |
| HyperFrames implementation details | `hyperframes`, `hyperframes-cli` | Use after route is chosen. |
| Remotion mentioned as target tool | `remotion:remotion-best-practices` | Use only if building in Remotion. |
| Remotion project -> HyperFrames | `remotion-to-hyperframes` | Only explicit port/migration requests. |
| Download source video/audio | `下载视频` | Use before analysis or transcription. |
| Transcribe/translate video | `视频转写` | Use for transcript, translation, SRT, burn-in. |
| TTS / voice clone | `tts-skill` or `hyperframes-media` | Pick based on the selected workflow. |

If two routes seem plausible, pick the one closest to the user's artifact:
existing footage beats generated video; reference-video replication beats style
inspiration; captions beat overlays when the user only asked for subtitles.
