###################################################################################################
#
# game_world.py
# Main game loop.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libarries
import pygame, math, pygame.font, random, os

# Import modules
from states.state import State
from states.pause_menu import PauseMenu
from states.resources import Resources
from states.dock import Dock
from states.fuel import Fuel
from states.navigation import Navigation


class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Declare background
        self.bg = pygame.image.load(os.path.join(self.game.assets_dir, "bg.jpg"))
        self.bg_width = self.bg.get_width()
        self.tiles = math.ceil(game.SCREEN_WIDTH / self.bg_width) + 1
        self.scroll = 0
        self.black = (0, 0, 0)

        # Declare ship variables
        self.ship = pygame.image.load("assets/ship.png").convert_alpha()
        self.shipX = 450
        self.shipY = 280
        self.shipX_change = 0.3
        self.shipY_change = 0

    def update(self, actions):
        # Check if the game was paused
        if actions["escape"]:
            new_state = PauseMenu(self.game)
            new_state.enter_state()
        # Check for colliders with sprites
        self.screen = pygame.display.set_mode((1200, 800))

        def draw_gui(x, y, sizeX, sizeY):
            return pygame.draw.rect(self.screen, (255, 0, 0), (x, y, sizeX, sizeY))

        self.m1 = draw_gui(40, 35, 40, 50)
        self.m2 = draw_gui(82, 35, 40, 50)
        self.m3 = draw_gui(124, 35, 60, 50)
        self.m4 = draw_gui(186, 35, 50, 50)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if self.m1.collidepoint(pygame.mouse.get_pos()):
                    new_state = Fuel(self.game)
                    new_state.enter_state()
                if self.m2.collidepoint(pygame.mouse.get_pos()):
                    new_state = Navigation(self.game)
                    new_state.enter_state()
                if self.m3.collidepoint(pygame.mouse.get_pos()):
                    new_state = Resources(self.game)
                    new_state.enter_state()
                if self.m4.collidepoint(pygame.mouse.get_pos()):
                    new_state = Dock(self.game)
                    new_state.enter_state()

    def render(self, display):
        # Game variables
        minimenu = pygame.image.load("assets/minimenu.png").convert_alpha()

        # Define particles
        particles = []

        # Draw moving background
        self.scroll -= 5
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0
        for i in range(0, self.tiles):
            display.blit(self.bg, (i * self.bg_width + self.scroll, 0))

        # Draw floating ship
        if self.shipX <= 420:
            self.shipX_change = 0.2
        elif self.shipY <= 300:
            self.shipY_change = 0.2
        elif self.shipX >= 460:
            self.shipX_change = -0.2
        elif self.shipY >= 330:
            self.shipY_change = -0.2

        self.shipX += self.shipX_change
        self.shipY += self.shipY_change

        display.blit(self.ship, (self.shipX, self.shipY))

        # Draw particles
        particles.append(
            [
                [self.shipX, self.shipY + 140],
                [random.randint(-50, 0), 0],
                random.randint(5, 8),
            ]
        )

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(
                display,
                (255, 255, 255),
                [int(particle[0][0]), int(particle[0][1])],
                int(particle[2]),
            )
            if particle[2] <= 0:
                particles.remove(particle)

        # Draw stuff
        display.blit(minimenu, (20, 20))
