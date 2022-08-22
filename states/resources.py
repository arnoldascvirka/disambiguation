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

    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(
            display,
            "Resources:",
            (0, 0, 0),
            150,
            200,
        )
