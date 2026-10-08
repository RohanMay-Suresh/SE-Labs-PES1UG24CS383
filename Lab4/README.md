# Lab 4 — LLM-Assisted Debugging & Feature Work

**Student:** Rohan Suresh · **SRN:** PES1UG24CS383
**Scenario:** #14 — 2048 (terminal game) · Starter repo: [SETAPESU26/14_2048](https://github.com/SETAPESU26/14_2048)

## Submission

**[`Lab4_PES1UG24CS383_G.pdf`](Lab4_PES1UG24CS383_G.pdf)**: details and evidence for every task, plus testing and the prompts used.

| Item | Link |
|---|---|
| Gameplay **before** changes | [Google Drive](https://drive.google.com/file/d/1dBPhX-SaHmd6Zy7efy1eWp4XfiCGTEhK/view?usp=drive_link) · [`SE_Lab4_Before.mp4`](SE_Lab4_Before.mp4) |
| Gameplay **after** changes | [Google Drive](https://drive.google.com/file/d/1nT-a8UHGVLacW7BmqdqvtTFyVu0yOuTT/view?usp=drive_link) · [`SE_Lab4_After.mp4`](SE_Lab4_After.mp4) |
| Complete LLM chat history | [Claude chat link](https://claude.ai/share/463f54ba-b87c-44e4-aa29-bf588b3ee43b) |

| File | Content |
|---|---|
| [`main.py`](main.py) | Entry point |
| [`game.py`](game.py) | Game loop, commands, undo, feedback messages |
| [`board.py`](board.py) | Grid movement, merging, scoring, win/no-move checks |
| [`requirements.txt`](requirements.txt) | Standard library only, no dependencies |

## Run

```bash
python main.py
```

W/A/S/D to move, U to undo, Q to quit.

## Summary

- **Task 1: merge semantics.** `slide_line()` let a tile that had just merged merge again in the same move, so `2 2 4 8` became `16`. Now each tile merges at most once per move, so `2 2 4 8` becomes `4 4 8`.
- **Task 2: game state.** Added `has_won()`, which ends the game when a tile reaches 2048. The game also ends when no legal moves remain, and a move that changes nothing doesn't add a tile.
- **Task 3: undo and best score.** One-level undo restores both the board and the score, and doesn't add a tile. The best score is tracked for the current run.
- **Task 4: move feedback.** Each command prints one message, for example `Moved left: 1 merge, +4 points.`, `Can't move up - nothing changed.`, `Undid last move.` or `Nothing to undo.`
- **Other bugs fixed:** the score never increased because merges added no points. The input check `key not in "wasd"` accepted `wa` and empty input; it now checks exact keys.

**Tested:** ordinary slides, four-equal patterns, separated equal pairs, unchanged moves, reaching 2048, boards with no moves, undo with score restore, invalid commands, and quitting.
