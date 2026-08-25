# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**PES University · Dept. of CSE · Software Engineering**

| | |
|---|---|
| **Student** | Rohan |
| **SRN** | PES1UG24CS383 |
| **Problem Statement** | **#15 — Pharmacy Expiry & Re-order Dispatch Engine** |
| **Domain** | Healthcare & Telemedicine |

---

## 1. Problem Context & Overview

Hospital pharmacies need an automated stock management engine that tracks batch expiry dates, generates **First-Expired-First-Out (FEFO)** dispensing lists, and triggers automated purchase orders when stock hits a threshold.

The engine sits between the dispensing counter and the supplier. It holds every medicine as a set of *batches*, each with its own expiry date, so that a stock figure is never just a number — it is a queue ordered by expiry. Three things follow from that model:

- **Dispensing** must always draw from the batch closest to expiry (FEFO), so stock is consumed before it ages out.
- **Expiry** is a date-driven event with no human trigger behind it, so the engine sweeps stock daily, warns on near-expiry batches and quarantines those already expired.
- **Re-ordering** must be measured against *dispensable* stock only — quarantined batches sit on the shelf but cannot fill a prescription, and must not mask a shortage.

### Actors

| Actor | Kind | Responsibility |
|---|---|---|
| **Pharmacy Clerk** | Primary, human | Registers incoming batches, dispenses medicine at checkout, configures per-item re-order thresholds, receives supplier consignments. |
| **Inventory Supplier** | Secondary, external | Receives dispatched purchase orders and delivers the consignment against them. |
| **Scheduler** | Secondary, system / time | Initiates the daily expiry sweep and the post-movement threshold evaluation. Modelled as an actor because these flows are time-triggered, not user-triggered. |

---

## 2. Deliverables

| # | Deliverable | File |
|---|---|---|
| 1 | Requirements table — 5 FRs, 2 NFRs, plus requirement→use-case traceability | [`requirements.md`](requirements.md) |
| 2 | UML use-case diagram — all actors, 11 use cases, `«include»` and `«extend»` | [`use-case-diagram.svg`](use-case-diagram.svg) · source: [`use-case-diagram.puml`](use-case-diagram.puml) |
| 3 | Use-case flow specification for UC-02 (Dispense Medicine — FEFO Checkout) | [`use-case-flow.md`](use-case-flow.md) |

---

## 3. UML Use-Case Diagram

![Use-case diagram for the Pharmacy Expiry & Re-order Dispatch Engine](use-case-diagram.svg)

### Relationships modelled

**`«include»`** — behaviour the base use case *always* performs, factored out because more than one base needs it, or because it is a distinct responsibility:

| Base use case | includes | Why |
|---|---|---|
| UC-02 Dispense Medicine | UC-07 Validate Batch Expiry | Every dispense re-checks the picked batch against today's date; the same check is reused by the sweep. |
| UC-02 Dispense Medicine | UC-08 Update Stock Ledger | Every dispense writes the movement and its audit entry (NFR-002). |
| UC-03 Run Daily Expiry Sweep | UC-07 Validate Batch Expiry | The sweep is a bulk application of the same expiry check. |
| UC-05 Generate & Dispatch Purchase Order | UC-10 Evaluate Stock Threshold | A purchase order is only ever raised off a threshold evaluation. |

**`«extend»`** — optional behaviour that fires only when a condition holds at a defined extension point:

| Extending use case | extends | Extension point / condition |
|---|---|---|
| UC-09 Quarantine Expired Batch | UC-03 Run Daily Expiry Sweep | Only when the sweep finds a batch with `expiry_date < today`. A sweep over healthy stock completes without it. |
| UC-11 Escalate Critical Stock-Out Alert | UC-05 Generate & Dispatch Purchase Order | Only when dispensable stock has already reached zero — a normal below-threshold re-order does not escalate. |

### Re-rendering the diagram

The committed `.svg` is the submitted artefact and needs no tooling to view. The equivalent PlantUML source is provided for regeneration:

```bash
java -jar plantuml.jar -tsvg use-case-diagram.puml
```

`use-case-diagram.puml` can also be pasted straight into <https://www.plantuml.com/plantuml> to render in the browser.

---

## 4. Requirements at a Glance

| ID | Summary | Priority |
|---|---|---|
| FR-001 | Enforce FEFO picking order at checkout | High |
| FR-002 | Capture and validate batch attributes at intake | High |
| FR-003 | Daily expiry sweep — flag near-expiry, quarantine expired | High |
| FR-004 | Per-item re-order threshold, re-evaluated on every movement | Medium |
| FR-005 | Purchase-order lifecycle tracking and receipt reconciliation | Medium |
| NFR-001 | Auto-generate and dispatch purchase orders — latency and security under peak load | High |
| NFR-002 | Immutable 5-year audit trail; 99.5% availability in operating hours | High |

Full descriptions, acceptance criteria and rationale: [`requirements.md`](requirements.md)
