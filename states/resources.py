###################################################################################################
#
# resources.py
# Module to run the resources state.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import Libraries
import pygame, os

# Import modules
from states.state import State


class Resources(State):
    def __init__(self, game):
        self.game = game

        State.__init__(self, game)
        # Set the menu
        self.menu_img = pygame.image.load(
            os.path.join(self.game.assets_dir, "4menus.png")
        ).convert_alpha()
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (
            200,
            400,
        )

    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(self.menu_img, self.menu_rect)
