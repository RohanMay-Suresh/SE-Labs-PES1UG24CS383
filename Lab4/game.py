from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.best_score = 0
        self.history = []  # at most one snapshot: one-level undo

    def display(self):
        print("\n" + "+------+------+------+------+")
        for row in self.board.grid:
            print("|" + "|".join(f"{x:^6}" if x else f"{' ':^6}" for x in row) + "|")
            print("+------+------+------+------+")
        print("Score:", self.board.score, " Best:", self.best_score)

    def move(self, key):
        moves = {"a": self.board.move_left, "d": self.board.move_right,
                 "w": self.board.move_up, "s": self.board.move_down}
        if key not in moves:
            return False
        before = self.board.snapshot()
        changed, points, merges = moves[key]()
        if not changed:
            return False  # unchanged move: no new tile
        self.history = [before]
        self.board.add_random_tile()
        self.best_score = max(self.best_score, self.board.score)
        return True

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return False
        self.board.restore(self.history.pop())
        return True

    def run(self):
        print("2048 — W/A/S/D to move, U to undo, Q to quit.")
        while True:
            self.display()
            if self.board.has_won():
                print("You reached 2048! You win.")
                return
            if not self.board.can_move():
                print("No legal moves remain. Game over.")
                return
            key = input("> ").strip().lower()
            if key == "q":
                return
            if key == "u":
                self.undo()
                continue
            if key not in "wasd":
                print("Use W/A/S/D.")
                continue
            self.move(key)
