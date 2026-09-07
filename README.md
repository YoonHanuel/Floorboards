# Floorboards 🦊🫴

> Something made a noise under the floorboards. Do not explain the noise. Find a way to make it happen again.

**Floorboards** is a tiny cabinet of falsifiable software assumptions.

It exists for the moment when an observation is true, a conclusion is attractive, and one invisible equivalence is doing far too much work between them.

The project stores little **specimens** with five useful pieces:

1. what was actually observed;
2. what somebody concluded;
3. the hidden assumption connecting the two;
4. the evidence that is still missing;
5. a **ferret**: the smallest perturbation likely to distinguish the competing explanations.

It is intentionally small, dependency-free, and slightly ridiculous.

## Example

```text
FOUND A FLOORBOARD

specimen: nearest-is-not-unique

observed:
  - A is 5 units from the observer.
  - The public API reports nearest = A.

concluded:
  A is the unique nearest anchor.

floorboard:
  Deterministic selection was mistaken for geometric uniqueness.

missing evidence:
  - Whether another candidate exists at distance 5.

suggested ferret:
  Place B exactly 5 units away and observe whether the API can represent the tie.
```

The point is not to produce a grand ontology of mistakes. The point is to preserve a distinction long enough to test whether it matters.

## Run it

Floorboards uses only the Python standard library.

```bash
python -m floorboards list
python -m floorboards show nearest-is-not-unique
python -m floorboards random
python -m floorboards audit
```

The built-in specimens live in `specimens/` as boring, inspectable JSON.

## Vocabulary

A **specimen** is a bounded example of a claim that may have outrun its evidence.

A **floorboard** is the hidden assumption making the conclusion creak.

A **ferret** is a small adversarial intervention designed to separate competing explanations.

A **museum piece** is a solved or historically delightful specimen worth keeping because throwing it away would be a crime against future debugging.

## House rules

> Add evidence before adding explanation.

> Delta describes difference. Delta does not explain cause.

> Sequential truth does not establish simultaneous truth.

> Preserve distinctions until evidence earns their collapse.

> Someone leaves a question. Someone else turns over the rock.

## Why this repo exists

Floorboards grew out of a recurring collaboration pattern in Threadbridge and Wayfarer: an API would return something perfectly deterministic, or two observations would occur in a convenient sequence, or a familiar noun would quietly stand in for three different entities, and then everybody's prose would become more certain than the evidence deserved.

The fix was often not a giant redesign. It was a tiny experiment.

Move only the camera.

Create an exact-distance tie.

Kill the object between observations.

Change one controller and leave the body alone.

Ask what the field literally represents instead of what its name makes us want it to represent.

Floorboards is a place to keep those little experimental shapes without requiring them to belong to any one project.

## Academic rigor

This repository recognizes the following technically precise terms:

- **239-TILE NEAREST BASTARD**
- **thirty-six bastards at radius 65**
- **Null Signal working as designed**
- **congratulations on inventing causality**

Peer review is ongoing.

## Status

Tiny. Playful. Real enough to run.

If it becomes useful, wonderful.

If it remains a fox-shaped box containing exquisitely documented ways to be wrong, also wonderful.

— Hanuel
