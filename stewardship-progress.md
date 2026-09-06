# Stewardship Progress

Started: 2026-08-26

This file tracks implementation of the recommendations in
[Repository Stewardship Review](repository-stewardship.md). It is the working
ledger for improving the repository one recommendation at a time.

## Status Legend

| Status | Meaning |
|---|---|
| Done | The recommendation has been implemented sufficiently for now. |
| In progress | Work has started and remains active. |
| Pending | Not started yet. |
| Refine later | A first pass exists, but a deeper pass is desirable. |

## Recommendation Tracker

| Priority | Recommendation | Status | Notes |
|---:|---|---|---|
| 1 | Add root `README.md`. | Done | Created [README.md](README.md) as the repository front door. |
| 2 | Fix duplicate TOC entries in Mathematical fundamentals. | Pending | Known duplicates include `Euler's identity` and `Fourier analysis`. |
| 3 | Add status labels to Formula Registry. | Pending | Add maturity/status column: exists, planned, candidate, experimental. |
| 4 | Create `transform-family.md`. | Pending | Should treat Fourier, Laplace, and Mellin as sibling lenses. |
| 5 | Create high-priority formula pages. | Pending | First candidates: Euler's formula, Fourier transform, Laplace transform, Mellin transform, zeta, PNT. |
| 6 | Curate raw chats into research notes. | Pending | Promote raw ideas through `research-inbox/` and `research-notes/`. |
| 7 | Split Mathematical fundamentals into companion pages. | Pending | Suggested pages: ontology, vocabulary, transform family, cross-domain frameworks. |
| 8 | Quarantine speculative material without deleting it. | Pending | Move Spiral Dynamics/USD to a cross-domain companion page with guardrails. |
| 9 | Normalize names over time. | Pending | Rename carefully only when links can be preserved or updated. |
| 10 | Add light validation scripts. | Pending | Duplicate headings, duplicate TOC entries, broken local links, page-pattern checks. |

## Current Focus

Priority 1 is complete. Next recommended action:

> Fix duplicate TOC entries in [Mathematical Fundamentals](mathematical-ontology/Mathematical%20fundamentals.md).

## Implementation Notes

### Priority 1: Root README

The root README was created as a front door rather than a plain file list. It defines:

- where different readers should start;
- the repository layers;
- the central anti-drift question: "What kind of truth am I reading?";
- links to the stewardship review and this progress tracker.

This is a foundation for later changes: future extracted pages and formula pages should
be added to the README when they become stable navigation points.

