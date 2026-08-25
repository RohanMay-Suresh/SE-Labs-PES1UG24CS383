# Use-Case Flow Specification

**Problem Statement #15 — Pharmacy Expiry & Re-order Dispatch Engine**

---

## UC-02 — Dispense Medicine (FEFO Checkout)

| Field | Value |
|---|---|
| **Use-Case ID** | UC-02 |
| **Name** | Dispense Medicine (FEFO Checkout) |
| **Primary Actor** | Pharmacy Clerk |
| **Secondary Actors** | — (Scheduler is notified indirectly via the re-order trigger) |
| **Stakeholders & Interests** | *Patient* — receives valid, unexpired medicine. *Pharmacy Clerk* — completes checkout quickly without judging expiry dates manually. *Hospital Administration* — minimises write-off of expired stock and keeps an auditable dispensing record. |
| **Trigger** | The Pharmacy Clerk submits a prescription or counter sale for checkout. |
| **Related Requirements** | FR-001 (FEFO ordering), FR-004 (threshold re-evaluation), NFR-002 (audit trail) |
| **Frequency of Use** | High — several hundred times per operating day |

### Preconditions

1. The Pharmacy Clerk is authenticated and holds the `DISPENSE` permission.
2. A valid prescription or counter-sale record exists, listing medicine codes and quantities.
3. At least one batch of each requested medicine exists with status `AVAILABLE`.
4. The daily expiry sweep (UC-03) has completed for the current date, so batch statuses are current.

### Postconditions

**On success:**

1. The requested quantity is deducted from the nearest-expiry `AVAILABLE` batch(es) of each medicine.
2. The stock ledger is updated and an immutable audit entry is written for every deduction, attributed to the clerk and timestamped (NFR-002).
3. Dispensable stock for each affected item is re-evaluated against its safety threshold; a re-order trigger is raised where the threshold has been breached (FR-004).
4. A dispense slip is generated listing, per line, the medicine, quantity, batch ID and expiry date issued.

**On failure:** No stock is deducted, no ledger or audit entry is written, and the sale remains open — the transaction is atomic.

### Main Success Scenario

| # | Actor | Step |
|---|---|---|
| 1 | Clerk | Opens the checkout screen and selects the prescription / sale record to dispense. |
| 2 | System | Displays each requested medicine with the quantity to be dispensed. |
| 3 | Clerk | Confirms the dispense request. |
| 4 | System | For each line, retrieves all batches of that medicine with status `AVAILABLE` and sorts them by expiry date, ascending. |
| 5 | System | *include* **UC-07 Validate Batch Expiry** — re-checks the selected batch against the current system date to confirm it has not expired since the last sweep. |
| 6 | System | Allocates the requested quantity to the nearest-expiry valid batch and displays the proposed allocation (medicine, batch ID, expiry date, quantity) for confirmation. |
| 7 | Clerk | Confirms the allocation. |
| 8 | System | *include* **UC-08 Update Stock Ledger** — deducts the allocated quantity, writes the ledger movement and the audit entry, and commits the transaction. |
| 9 | System | *include* **UC-10 Evaluate Stock Threshold** — compares remaining dispensable stock against the configured safety threshold and raises a re-order trigger if it has been breached. |
| 10 | System | Generates and prints the dispense slip, and returns the clerk to the checkout screen. |

### Alternate Flow

**A1 — Nearest-expiry batch holds insufficient quantity** *(branches from step 6)*

| # | Actor | Step |
|---|---|---|
| 6a.1 | System | Detects that the nearest-expiry valid batch holds less than the requested quantity. |
| 6a.2 | System | Allocates the full remaining quantity of that batch, then moves to the next batch in ascending expiry order and repeats until the requested quantity is fully covered — preserving FEFO order across the split. |
| 6a.3 | System | Displays the multi-batch allocation, showing the quantity drawn from each batch with its batch ID and expiry date. |
| 6a.4 | Clerk | Confirms the split allocation. |
| — | — | The flow rejoins the main success scenario at **step 8**, where all deductions in the split are committed as a single atomic transaction. |

*If the combined stock across all valid batches is still short of the requested quantity, the system dispenses nothing, informs the clerk of the shortfall with the maximum dispensable quantity, and raises a re-order trigger for the item (FR-004).*

### Business Rules

- **BR-01** Batches with status `QUARANTINED` are never eligible for allocation. Batches flagged `NEAR_EXPIRY` remain fully dispensable — under FEFO they are precisely the ones picked first.
- **BR-02** Where two batches share the same expiry date, the batch registered earliest is picked first.
- **BR-03** A dispense transaction is all-or-nothing: a failure on any line rolls back every line in the sale.
