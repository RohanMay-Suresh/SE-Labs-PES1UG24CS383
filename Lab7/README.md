# Lab 7 - Fuzz Testing

Rohan Suresh, PES1UG24CS383, Section G

Assigned repo: https://github.com/SETAPESU26/L6_L7_19_parking_fee

- `parking_fee.py` - application code, with the bugs found by fuzzing fixed
- `test_parking_fee.py` - Hypothesis fuzz tests for all three functions
- `screenshots/` - original run, failing tests, fixed run, passing tests
- `Lab7_PES1UG24CS383_G.pdf` - report with screenshots and both source files

Original code: 5 of 7 tests failed.

- `minutes_parked` crashed on `None`, `''` and `'-'`, and gave a negative duration for `'1:00-0:00'`
- `hourly_rate` crashed on `None` and on unknown vehicles (`KeyError`)
- `format_plate` crashed on `None` and short strings (`IndexError`), and formatted `ka1` as `KA 1`

Fixed code: all 7 tests pass. Each function returns `None` for invalid input (times must be `HH:MM-HH:MM` with valid hours/minutes and exit after entry, plates must look like `KA01AB1234`), and `main()` prints a message instead of crashing.
