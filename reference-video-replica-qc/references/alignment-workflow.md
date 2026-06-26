# Alignment Workflow

## Reference Breakdown

Use a fixed timestamp grid. For videos under 60 seconds, default to `0.5s`.
For high-speed typography or cursor movement, add finer samples around failing
moments.

Describe each timestamp with:

- text state
- subject position and size
- background state
- active transition
- visible cursor or interaction
- scene boundary status

## Candidate Comparison

Use the same timestamp grid. Put reference on the left and candidate on the
right. Start the report with the earliest failing timestamp.

Common failure classes:

- global offset: every scene is late or early
- drift: early scenes align, later scenes do not
- wrong scale: subject is too small or too large
- wrong background: persistent effects that should not exist
- wrong transition: missing flash, wipe, blur, or speed-ramp
- wrong semantic state: text says the right words but at the wrong phase
- accidental artifacts: blank frames, solid-color flashes, missing assets

## Repair Handoff

For each failing segment, provide:

- timestamp range
- what the reference shows
- what the candidate shows
- required change
- whether the fix is timing, layout, asset, animation, or encoding

Do not say "adjust animation" without naming the timestamp and visible target.
