## Identifier approach

Use an immutable, category-neutral identifier:

```
OBS-000001
OBS-000002
OBS-000003
```

A filename combines that identifier with a readable slug:

```
OBS-000009-prime-exclusion-activates-at-p2.md
```

Category-neutral IDs are preferable to identifiers such as `P-009` or `T-003`. An observation initially classified as a prime property may later be understood primarily as a translation. Its labels can change without changing its identity.

### Identifier rules

1. Allocate identifiers sequentially from one repository-wide sequence.
2. Pad the numeric part to six digits.
3. Never reuse an identifier, including after rejection or deletion.
4. Never renumber snippets when files are reordered.
5. Keep the identifier stable when wording or metadata changes.
6. Create a new identifier when the mathematical statement changes materially.
7. Record merges and replacements rather than silently deleting old identities.

For example:

```
workflow_status: merged
superseded_by: OBS-000027
```

The replacement records the reverse relationship:

```
relations:
  supersedes:
    - OBS-000009
    - OBS-000014
```

### Revisions

Editorial improvements retain the same ID:

```
id: OBS-000009
revision: 3
```

Create a new observation when any of these change materially:

- mathematical object;
- claimed relation;
- valid domain;
- exact status;
- translation being asserted.

Changing the title, example, explanation, or labels does not require a new ID.

## Suggested directory structure

```
brain-dumps/
  README.md
  observations/
    README.md
    OBS-000001-periodic-divisor-column.md
    OBS-000002-prime-columns-as-generators.md
    OBS-000003-overlap-reduces-new-contribution.md
    OBS-000009-prime-exclusion-activates-at-p2.md
```

The observation files become the source of truth. The index is then a generated or manually maintained catalogue of their metadata.

This creates a clean lifecycle:

```
brain dump
    ↓
atomic observation
    ↓
context-first screening
    ↓
stand-alone snippet
    ↓
promoted note or preserved negative result
```

The essential rule is: **one identifier represents one stable observational claim, not one file, paragraph, topic, or source conversation.**