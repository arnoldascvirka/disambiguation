###################################################################################################
#
# title.py
# Module to run the main menu state.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libraries
import pygame, os, sys

# Import modules
from states.state import State
from states.game_world import Game_World
from states.load_game import LoadGame


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.menu_img = pygame.image.load(
            os.path.join(self.game.assets_dir, "mainmenu.png")
        ).convert()
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (
            1200 / 2,
            800 / 2,
        )
        # Set the cursor and menu states
        self.menu_options = {0: "New game", 1: "Load game", 2: "Quit"}
        self.index = 0
        self.cursor_img = pygame.image.load(
            os.path.join(self.game.assets_dir, "maincursor.png")
        ).convert_alpha()
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.menu_rect.y + 505
        self.cursor_rect.x, self.cursor_rect.y = (
            self.menu_rect.x + 705,
            self.cursor_pos_y,
        )

    def update(self, actions):
        self.update_cursor(actions)
        if actions["action1"]:
            self.transition_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.menu_img, self.menu_rect)
        display.blit(self.cursor_img, self.cursor_rect)

    def transition_state(self):
        if self.menu_options[self.index] == "New game":
            new_state = Game_World(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == "Load game":
            new_state = LoadGame(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == "Quit":
            sys.exit()

    def update_cursor(self, actions):
        if actions["down"]:
            self.index = (self.index + 1) % len(self.menu_options)
        elif actions["up"]:
            self.index = (self.index - 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index * 85)
