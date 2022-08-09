###################################################################################################
#
# dock.py
# Module to run the dock state.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import Libraries
import pygame, os

# Import modules
from states.state import State


class Dock(State):
    def __init__(self, game):
        self.game = game

        State.__init__(self, game)
        # Set the menu
        self.menu_img = pygame.image.load(
            os.path.join(self.game.assets_dir, "3menus.png")
        ).convert_alpha()
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (
            200,
            400,
        )
        # # Set the cursor and menu states
        # self.menu_options = {0: "Save game", 1: "Load game", 2: "Exit"}
        # self.index = 0
        # self.cursor_img = pygame.image.load(
        #     os.path.join(self.game.assets_dir, "cursor.png")
        # )
        # self.cursor_rect = self.cursor_img.get_rect()
        # self.cursor_pos_y = self.menu_rect.y + 105
        # self.cursor_rect.x, self.cursor_rect.y = (
        #     self.menu_rect.x + 73,
        #     self.cursor_pos_y,
        # )

    def update(self, actions):
        # self.update_cursor(actions)
        # if actions["action1"]:
        #     self.transition_state()
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(self.menu_img, self.menu_rect)
        # display.blit(self.cursor_img, self.cursor_rect)

    # def transition_state(self):
    #     if self.menu_options[self.index] == "Save game":
    #         new_state = SaveGame(self.game)
    #         new_state.enter_state()
    #     elif self.menu_options[self.index] == "Load game":
    #         new_state = LoadGame(self.game)
    #         new_state.enter_state()
    #     elif self.menu_options[self.index] == "Exit":
    #         while len(self.game.state_stack) > 1:
    #             self.game.state_stack.pop()

    # def update_cursor(self, actions):
    #     if actions["down"]:
    #         self.index = (self.index + 1) % len(self.menu_options)
    #     elif actions["up"]:
    #         self.index = (self.index - 1) % len(self.menu_options)
    #     self.cursor_rect.y = self.cursor_pos_y + (self.index * 50)
