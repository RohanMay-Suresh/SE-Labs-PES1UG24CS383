# Lab 2 — Agile Project Management using JIRA

**PES University · Dept. of CSE · Software Engineering**

| | |
|---|---|
| **Student** | Rohan May Suresh |
| **SRN** | PES1UG24CS383 |
| **Problem Statement** | **#15 — Pharmacy Expiry & Re-order Dispatch Engine** |
| **Jira Project** | `SE Lab PES1UG24CS383` (key **SLP**, Company-managed Scrum) |
| **Jira Board** | https://rohanmay11.atlassian.net/jira/software/c/projects/SLP/boards/2 |

---

## Submission

**[`Lab2_PES1UG24CS383_G.pdf`](Lab2_PES1UG24CS383_G.pdf)** — the single combined PDF required by the submission form. Contains the Jira project link, all screenshot evidence, and the four reflection answers.

| Handout requirement | Where it appears |
|---|---|
| Epics & User Stories / Backlog | Section 1 |
| Story Points | Section 2 |
| Active Sprint Board | Sections 3 and 4 |
| Burndown Chart | Section 5 |
| Reflection answers | Section 6 |
| Jira project link | Page 1 (and above) |

### Screenshot evidence

| File | Content |
|---|---|
| [`01-backlog-epics-stories-points.png`](01-backlog-epics-stories-points.png) | Backlog — 4 Epics, 14 User Stories, priorities, story points, Epic rollups |
| [`02-sprint1-active-board.png`](02-sprint1-active-board.png) | Sprint 1 active Scrum board, mid-sprint |
| [`03-sprint2-active-board.png`](03-sprint2-active-board.png) | Sprint 2 active Scrum board, mid-sprint |
| [`04-sprint1-burndown.png`](04-sprint1-burndown.png) | Sprint 1 burndown chart (29 points) |
| [`05-sprint2-burndown.png`](05-sprint2-burndown.png) | Sprint 2 burndown chart (27 points) |

---

## Backlog summary

Built from the Lab 1 requirements — every story traces back to an FR or NFR from Problem Statement #15.

| Epic | Stories | Points | Traces to |
|---|---|---|---|
| **SLP-1** EPIC1: Batch Intake & Expiry Governance | SLP-5 … SLP-9 | 24 | FR-002, FR-003 |
| **SLP-2** EPIC2: FEFO Dispensing at Checkout | SLP-10 … SLP-12 | 16 | FR-001 |
| **SLP-3** EPIC3: Automated Re-ordering & Supplier Fulfilment | SLP-13 … SLP-16 | 21 | FR-004, FR-005, NFR-001 |
| **SLP-4** EPIC4: Audit Trail & Compliance Reporting | SLP-17, SLP-18 | 11 | NFR-002 |
| | | **72** | |

Story points use the Fibonacci scale (1, 2, 3, 5, 8, 13) as required for Planning Poker.

## Sprint summary

| Sprint | Duration | Committed | Completed | Stories |
|---|---|---|---|---|
| **SLP Sprint 1** | 1 week | 29 pts | 29 pts | SLP-5, SLP-6, SLP-7, SLP-8, SLP-10 |
| **SLP Sprint 2** | 1 week | 27 pts | 27 pts | SLP-9, SLP-11, SLP-12, SLP-13, SLP-14, SLP-15 |
| *Backlog (uncommitted)* | — | 16 pts | — | SLP-16, SLP-17, SLP-18 |

Average velocity across the two sprints: **28 points/sprint**.

SLP-16, SLP-17 and SLP-18 were deliberately left uncommitted so the sprint scope reflected a realistic capacity rather than the entire backlog — and so the reflection had something honest to analyse.

---

## Note on the burndown charts

Both charts show the red *Remaining Values* line dropping near-vertically at the sprint start rather than descending alongside the grey guideline. This is expected: a one-week sprint was simulated in minutes, so all the "work" was marked done within a few minutes of day one. Section 6 of the PDF discusses what that shape actually signifies — that a burndown measures *when work is marked done*, not when it is performed.
