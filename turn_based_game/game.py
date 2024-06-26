class Character:
    MOVES = {'N': [0, -1],
             'E': [1, 0],
             'S': [0, 1],
             'W': [-1, 0]}

    def __init__(self, name):
        self.name = name
        self.position = [5, 5]

    def move(self, direction):
        if direction in self.MOVES:
            move = self.MOVES[direction]
            self.position[0] += move[0]
            self.position[1] += move[1]


class Game:
    def __init__(self, n_rows=10, n_cols=10):
        self.characters = [Character('Player')]
        self.n_rows = n_rows
        self.n_cols = n_cols


if __name__ == "__main__":
    game = Game()
    player = game.characters[0]