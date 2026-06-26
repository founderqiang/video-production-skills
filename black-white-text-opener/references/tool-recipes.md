# Tool Recipes

## HyperFrames

Use HyperFrames when the video project is already motion-heavy or visual polish
matters.

Implementation notes:

- Create an opener scene as a separate composition section.
- Animate text opacity, blur, x-offset, and scale with deterministic timings.
- Add a black rectangle/background layer for the full scene.
- Keep any grain subtle and procedural.
- Export the opener alone first, then compose it with the body.

## Remotion

Use Remotion when the project is already React/Remotion-based.

Implementation notes:

- Drive all timing from `useCurrentFrame()` and `fps`.
- Keep text states in an array generated from the opener plan.
- Use `interpolate()` for opacity, blur, and x-offset.
- Export a still frame at the first readable beat and final hold for QC.

## ffmpeg

Use ffmpeg for simple utility openers or draft previews.

Implementation notes:

- Use a black `color` source.
- Use `drawtext` for simple title and final phrase.
- Prefer it for static/fade openers, not complex word replacement.
- Verify output duration, resolution, and frame rate with `ffprobe`.
