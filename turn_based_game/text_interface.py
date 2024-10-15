from game import Game


class TextInterface:
    def __init__(self):
        self.game = Game()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True

    def _create_area(self):
        self.game_area = [['.'] * self.game.n_cols
                          for _ in range(self.game.n_rows)]
        for character in self.game.characters:
            pos = character.position
            self.game_area[pos[1]][pos[0]] = character.name[0]

    def _draw_area(self):
        self._create_area()
        print(f"\u2554{'\u2550' * self.game.n_cols}\u2557")
        for row in self.game_area:
            print(f"\u2551{"".join(row)}\u2551")
        print(f"\u255A{'\u2550' * self.game.n_cols}\u255D")

    def _handle_input(self):
        direction = input('Enter N,E,W or S to move: ')
        collision_character = self.game.move_character(self.player, direction)
        if collision_character:
            print(f"{self.player} meets {collision_character}")

    def main_loop(self):
        print("Welcome to Andrew's Game")
        self._draw_area()
        while self.running:
            self._handle_input()
            self._draw_area()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()
