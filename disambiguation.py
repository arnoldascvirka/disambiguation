###################################################################################################
#
# Main.py
# The file that runs the main game of Disambiguation.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libraries
import pygame, pygame.font, os
from pygame.locals import *


# Import modules
from states.title import Title


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Disambiguation")
        self.running, self.playing = True, True
        self.actions = {
            "up": False,
            "down": False,
            "action1": False,
            "action2": False,
            "start": False,
            "escape": False,
        }
        self.prev_time = 0
        self.state_stack = []
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:

            clock = pygame.time.Clock()
            clock.tick()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                if event.key == pygame.K_s:
                    self.actions["down"] = True
                if event.key == pygame.K_p:
                    self.actions["action1"] = True
                if event.key == pygame.K_o:
                    self.actions["action2"] = True
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = True
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.actions["up"] = False
                if event.key == pygame.K_s:
                    self.actions["down"] = False
                if event.key == pygame.K_p:
                    self.actions["action1"] = False
                if event.key == pygame.K_o:
                    self.actions["action2"] = False
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = False
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = False

    def update(self):
        self.state_stack[-1].update(self.actions)
        pass

    def render(self):
        self.state_stack[-1].render(self.screen)
        # Render current state to the screen
        self.screen.blit(
            pygame.transform.scale(
                self.screen, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            ),
            (0, 0),
        )
        pygame.display.update()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        # Create pointers to directories
        self.assets_dir = os.path.join("assets")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(
            os.path.join(self.font_dir, "SF_Cartoonist_Hand.ttf"), 40
        )

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
