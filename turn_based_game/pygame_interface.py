import pygame
from game import Game

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SQUARE_SIZE = 60


class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        # self.surf.fill((255, 0, 0))
        pygame.draw.circle(self.surf,
                           (255, 0, 0),
                           (SQUARE_SIZE // 2, SQUARE_SIZE // 2),
                           SQUARE_SIZE // 3,
                           )


class GameGUI:
    key_moves = {K_UP: 'N',
                 K_DOWN: 'S',
                 K_RIGHT: 'E',
                 K_LEFT: 'W',
                 }

    def __init__(self):
        pygame.init()

        self.game = Game()
        self.player = self.game.characters[0]
        self.player.sprite = CharacterSprite()

        self.screen = pygame.display.set_mode([self.game.n_cols * SQUARE_SIZE,
                                               self.game.n_rows * SQUARE_SIZE])
        self.running = True

    @staticmethod
    def _convert_position(grid_position):
        return (SQUARE_SIZE * grid_position[0] + SQUARE_SIZE // 2,
                SQUARE_SIZE * grid_position[1] + SQUARE_SIZE // 2)


    def main_loop(self):
        while self.running:
            self._handle_input()
            self._draw()
        pygame.quit()

    def _handle_input(self):
        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            if event.type == KEYDOWN and event.key in self.key_moves:
                direction = self.key_moves[event.key]
                self.player.move(direction)

    def _draw(self):
        self.screen.fill((0,0,0))
        coord_pos = self._convert_position(self.player.position)
        player_rect = self.player.sprite.surf.get_rect(center=coord_pos)
        self.screen.blit(self.player.sprite.surf, player_rect)
        pygame.display.flip()


if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()