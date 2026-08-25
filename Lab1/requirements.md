# Requirements Specification

**Problem Statement #15 — Pharmacy Expiry & Re-order Dispatch Engine**
Domain: Healthcare & Telemedicine | Lab 1: Requirements Engineering & UML Use-Case Modelling

**Actors:** Pharmacy Clerk (primary, human) · Inventory Supplier (secondary, external organisation) · Scheduler (secondary, system/time actor that initiates the daily expiry sweep and the threshold evaluation)

---

## 1. Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **FR-001** | Functional — Dispensing / FEFO | The system shall enforce FEFO picking order by prioritizing medicine batches with the nearest expiry date during sales checkout. | High | **Pass:** For every dispense line, the oldest *valid* (unexpired, non-quarantined) batch of that medicine is selected first. **Fail:** A newer batch is assigned while an older unexpired batch of the same medicine still holds stock. | First-Expired-First-Out is the standard hospital stock-rotation rule. Manual picking lets near-expiry stock age on the shelf until it must be written off, so the ordering must be enforced by the system rather than left to the clerk's judgement. |
| **FR-002** | Functional — Inventory Intake | The system shall capture batch number, manufacturer, quantity and expiry date for every medicine batch registered into stock, and shall reject any batch whose expiry date is on or before the date of registration. | High | **Pass:** Batch is stored with all four attributes plus a system-generated batch ID and status `AVAILABLE`; a batch submitted with a missing attribute or a past/same-day expiry date is rejected with a validation message and is not persisted. **Fail:** A batch is accepted with a null expiry date, or an already-expired batch enters `AVAILABLE` stock. | FR-001 and FR-003 are only as reliable as the data captured at intake. A batch with no expiry date is invisible to FEFO ordering, and admitting already-expired stock creates a direct patient-safety hazard. |
| **FR-003** | Functional — Expiry Monitoring | The system shall run a daily expiry sweep that flags every batch expiring within the configured near-expiry window (default 90 days) as `NEAR_EXPIRY`, and shall move every batch past its expiry date to `QUARANTINED`, making quarantined batches unavailable for dispensing. | High | **Pass:** After the sweep, every batch with `expiry_date < today` has status `QUARANTINED` and is excluded from FEFO selection; every batch expiring within the window appears on the near-expiry alert list. **Fail:** An expired batch remains dispensable, or a batch inside the window is absent from the alert list. | Expiry is a date-driven event with no user action behind it, so detection must be automatic. Quarantining rather than deleting preserves the batch for supplier return and for the audit trail required by NFR-002. |
| **FR-004** | Functional — Re-order Configuration | The system shall allow the Pharmacy Clerk to configure a safety-stock threshold and a re-order quantity per medicine item, and shall re-evaluate *dispensable* stock against that threshold after every stock movement. | Medium | **Pass:** Threshold and re-order quantity are persisted per item; a re-order trigger is raised within the same transaction as the movement that takes dispensable stock below the threshold. **Fail:** The threshold is not applied, or the evaluation counts `QUARANTINED` / expired batches as available stock. | Consumption rates differ per drug, so a single global threshold would over-stock some items and starve others. Excluding quarantined stock is essential — otherwise expired batches mask a real shortage and the re-order in NFR-001 never fires. |
| **FR-005** | Functional — Supplier Fulfilment | The system shall track each dispatched purchase order through the states `DISPATCHED → ACKNOWLEDGED → RECEIVED → CLOSED`, and on receipt shall reconcile the delivered quantity against the ordered quantity, raising a short-delivery discrepancy record when they differ. | Medium | **Pass:** A PO reaches `CLOSED` only after the delivered batches have been registered via FR-002 and the quantities match; a mismatch produces a discrepancy record carrying the variance and leaves the PO open. **Fail:** A PO is auto-closed on dispatch, or a quantity mismatch is accepted silently. | Closes the loop opened by NFR-001 — without receipt tracking the engine cannot tell an order in transit from an order never fulfilled, and would re-order the same item repeatedly. The discrepancy record also gives the pharmacy evidence for supplier billing disputes. |

## 2. Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **NFR-001** | Performance & Security | The system shall automatically generate and dispatch supplier purchase order requests when item stock dips below safety threshold. | High | **Pass:** Benchmarking tests confirm target latency and security standards under simulated peak load — specifically, the purchase order is generated and transmitted within 60 seconds of the FR-004 trigger while sustaining 500 concurrent stock movements, over TLS 1.2+ with a digitally signed payload. **Fail:** Dispatch latency exceeds 60 s at target load, or a purchase order is transmitted unsigned or over an unencrypted channel. | Re-ordering is only useful if it beats the supplier's daily cut-off; latency directly translates into stock-out days. A purchase order is a financially binding instruction to an external party, so transport encryption and payload signing are needed to prevent interception or tampering. |
| **NFR-002** | Reliability & Auditability | The system shall record every stock movement (intake, dispense, quarantine, PO dispatch, receipt) as an immutable, timestamped, user-attributed audit entry retained for 5 years, and shall remain available for at least 99.5% of pharmacy operating hours (07:00–22:00). | High | **Pass:** A 1000-transaction regression run produces one audit entry per movement with actor ID and UTC timestamp; direct `UPDATE`/`DELETE` on the audit store is rejected; measured monthly downtime inside the operating window is ≤ 4.5 hours. **Fail:** Any movement completes without an audit entry, or an existing audit row can be altered. | Controlled-drug regulation and hospital accreditation require a reconstructible history of who moved which batch and when; a mutable log would not survive an audit. The availability target reflects that dispensing halts entirely when the engine is down, since FEFO order cannot be determined manually at counter speed. |

## 3. Requirement → Use-Case Traceability

| Requirement | Realised by use case(s) |
|---|---|
| FR-001 | UC-02 Dispense Medicine (FEFO Checkout), UC-07 Validate Batch Expiry |
| FR-002 | UC-01 Register Medicine Batch, UC-06 Receive Supplier Consignment |
| FR-003 | UC-03 Run Daily Expiry Sweep, UC-09 Quarantine Expired Batch |
| FR-004 | UC-04 Configure Re-order Threshold, UC-10 Evaluate Stock Threshold |
| FR-005 | UC-05 Generate & Dispatch Purchase Order, UC-06 Receive Supplier Consignment |
| NFR-001 | UC-05 Generate & Dispatch Purchase Order, UC-11 Escalate Critical Stock-Out Alert |
| NFR-002 | UC-08 Update Stock Ledger (included by UC-02; every movement use case writes through it) |
