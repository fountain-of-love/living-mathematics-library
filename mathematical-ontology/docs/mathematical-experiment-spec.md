# Mathematical Experiment Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for computational, numerical, visual, or exploratory mathematical experiments.
- **Companion:** [Mathematical Process](./mathematical-process.md)

## 1. Role

A mathematical experiment records an exploration whose evidence is empirical, computational, visual, or heuristic.

Experiments may suggest patterns, test conjectures, expose counterexamples, or guide proof work. They do not turn observations into theorems.

## 2. Page Contract

```markdown
# Experiment Title

> One-sentence purpose.

## Question

What is being explored?

## Setup

- Inputs.
- Parameters.
- Algorithms or tools.
- Data sources.

## Procedure

Repeatable steps.

## Observations

- Observed result.

## Interpretation

What the observations may suggest.

## Limitations

- Numerical, sampling, precision, implementation, or conceptual limits.

## Follow-Up

- Next experiment, conjecture, proof task, or counterexample search.

## Sources And Artifacts

- [Source or artifact](https://example.org)

## Does Not Establish

- Claim, conjecture, theorem, or interpretation that this experiment does not prove.
```

## 3. Required Sections

Every experiment page should include:

- question;
- setup;
- procedure;
- observations;
- interpretation;
- limitations;
- follow-up;
- `does-not-establish` or a stated reason it is not applicable.

## 4. Evidence Status

Use these labels when helpful:

- exploratory;
- replicated;
- contradicted;
- inconclusive;
- promoted-to-conjecture;
- promoted-to-proof-target.

## 5. Empty Field Discipline

Do not omit setup, parameters, observations, limitations, or artifacts merely because they are incomplete.

Use explicit values from [Mathematical Process](./mathematical-process.md), such as `unknown`, `not-applicable`, `not-yet-verified`, `not-yet-developed`, `open`, and `not-known`.

## 6. Review Checklist

- The procedure is repeatable.
- Inputs and parameters are visible.
- Observations are separated from interpretation.
- Limitations are explicit.
- Missing information is explicit rather than silently absent.
- No experimental result is presented as proof.
- The experiment explicitly states what it does not establish.
