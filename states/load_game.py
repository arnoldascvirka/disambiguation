###################################################################################################
#
# load_game.py
# Module to run the load game state.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import Libraries
import pygame, os

# Import modules
from states.state import State


class LoadGame(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(
            display,
            "Load game:",
            (0, 0, 0),
            self.game.SCREEN_WIDTH / 2 - 400,
            self.game.SCREEN_HEIGHT / 2 - 200,
        )
