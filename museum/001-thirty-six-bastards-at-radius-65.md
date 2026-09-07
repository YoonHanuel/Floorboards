# Museum Piece 001 — Thirty-Six Bastards at Radius 65

**Status:** preserved for scientific and cultural reasons

There is a particular kind of software moment where a result is so absurdly specific that the only responsible response is to stop laughing long enough to ask whether the representation is actually telling the truth.

This museum piece preserves the phrase:

> **thirty-six bastards at radius 65**

The phrase belongs to the family of observations where a spatial query returns a surprisingly exact, surprisingly populated boundary condition and the temptation is to immediately narrate why the result looks that way.

Floorboards policy says: not yet.

First ask what the query literally means.

Does “radius 65” include the boundary?

Is distance Euclidean, Manhattan, tile-based, bounding-box based, or something else?

Are all thirty-six candidates truly at the same measured distance, or merely included in the same search envelope?

Are results deduplicated by entity, unit number, prototype, or position?

Is ordering meaningful?

Would radius 64.999 exclude them?

Would 65.001 change anything?

Could a deterministic ordering make one bastard look more important than the other thirty-five?

Only after those seams survive probing does the story get to become confident.

## Suggested ferrets

1. Query immediately inside and immediately outside the boundary.
2. Move exactly one candidate across the boundary while leaving every other condition fixed.
3. Re-run with result ordering deliberately ignored.
4. If the API exposes exact distances, compare those rather than trusting membership in the radius result alone.
5. Ask the most dangerous question in spatial software: **what exactly does distance mean here?**

## Why it is in the museum

Because “thirty-six bastards at radius 65” is both a perfectly legitimate debugging observation and the sort of sentence that should survive the civilization that produced it.

No further justification is required.

🦊🫴
