import random

SIZE = 4


class Board:
    def __init__(self):
        self.grid = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 4 if random.random() < 0.1 else 2

    @staticmethod
    def slide_line(line):
        """Slide a line towards index 0. Returns (new_line, points, merges)."""
        values = [x for x in line if x]
        result = []
        points = 0
        merges = 0
        just_merged = False  # was result[-1] created by a merge in this move?
        for value in values:
            if result and result[-1] == value and not just_merged:
                result[-1] *= 2
                points += result[-1]
                merges += 1
                just_merged = True
            else:
                result.append(value)
                just_merged = False
        return result + [0] * (SIZE - len(result)), points, merges

    # Each move returns (changed, points, merges) and adds points to the score.
    def move_left(self):
        changed, points, merges = False, 0, 0
        for r in range(SIZE):
            old = self.grid[r][:]
            self.grid[r], p, m = self.slide_line(old)
            changed |= old != self.grid[r]
            points, merges = points + p, merges + m
        self.score += points
        return changed, points, merges

    def move_right(self):
        changed, points, merges = False, 0, 0
        for r in range(SIZE):
            old = self.grid[r][:]
            new, p, m = self.slide_line(list(reversed(old)))
            self.grid[r] = list(reversed(new))
            changed |= old != self.grid[r]
            points, merges = points + p, merges + m
        self.score += points
        return changed, points, merges

    def move_up(self):
        changed, points, merges = False, 0, 0
        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            new, p, m = self.slide_line(old)
            for r in range(SIZE):
                self.grid[r][c] = new[r]
            changed |= old != new
            points, merges = points + p, merges + m
        self.score += points
        return changed, points, merges

    def move_down(self):
        changed, points, merges = False, 0, 0
        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            new, p, m = self.slide_line(list(reversed(old)))
            new = list(reversed(new))
            for r in range(SIZE):
                self.grid[r][c] = new[r]
            changed |= old != new
            points, merges = points + p, merges + m
        self.score += points
        return changed, points, merges

    def can_move(self):
        if any(0 in row for row in self.grid):
            return True
        for r in range(SIZE):
            for c in range(SIZE):
                if c + 1 < SIZE and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r + 1 < SIZE and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False
