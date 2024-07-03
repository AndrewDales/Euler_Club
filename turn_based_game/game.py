class Character:
    MOVES = {'N': [0, -1],
             'E': [1, 0],
             'S': [0, 1],
             'W': [-1, 0]}

    def __init__(self, name, position=None):
        if position is None:
            position = [5, 5]
        self.name = name
        self.position = position

    def find_new_location(self, direction):
        new_location = None
        if direction in self.MOVES:
            move = self.MOVES[direction]
            new_location = [self.position[0] + move[0], self.position[1] + move[1]]
        return new_location

    def move(self, direction):
        new_location = self.find_new_location(direction)
        if new_location:
            self.position = new_location

    def __str__(self):
        return self.name


class Game:
    def __init__(self, n_rows=10, n_cols=10):
        self.characters = [Character('Player'), Character('Orc', [3, 1]), Character('Dragon', [7, 6])]
        self.n_rows = n_rows
        self.n_cols = n_cols

    @property
    def character_positions(self):
        return [character.position for character in self.characters]

    def check_collision(self, location):
        collision_character = None
        if location in self.character_positions:
            collision_index = self.character_positions.index(location)
            collision_character = self.characters[collision_index]
        return collision_character

    def move_character(self, character, direction):
        new_position = character.find_new_location(direction)
        collision_character = self.check_collision(new_position)
        if not collision_character:
            character.move(direction)
        return collision_character


if __name__ == "__main__":
    game = Game()
    player = game.characters[0]