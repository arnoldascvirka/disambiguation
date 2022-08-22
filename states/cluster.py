###################################################################################################
#
# game_world.py
# Module to run the star cluster module.
#
# Arnoldas Cvirka 2022 July 30th
#
###################################################################################################
# Import Libraries
import pygame, os, math, random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import modules
from states.state import State
from gridsql import Grid

# Create engine
engine = create_engine("sqlite:///grid.db")
Session = sessionmaker(bind=engine)
session = Session()


# fmt: off
class Star(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        self.scroll = 0
        self.bg = pygame.image.load(os.path.join(self.game.assets_dir, "bg.png"))
        self.bg_width = self.bg.get_width()
        self.tiles = math.ceil(game.SCREEN_WIDTH / self.bg_width) + 1
        self.wid = random.randint(200, 800)
        self.hei = random.randint(200, 500)
        self.menu = pygame.image.load(os.path.join(self.game.assets_dir, "starmenu.png"))
        with open('assets/names.txt') as d:
            lines = d.readlines()
            self.f = random.choice(lines)
        
        # Declare planet stuff
        self.angle = 0
        planet1 = pygame.image.load(os.path.join(self.game.assets_dir, "planet1.png")).convert_alpha()
        planet2 = pygame.image.load(os.path.join(self.game.assets_dir, "planet2.png")).convert_alpha()
        planet3 = pygame.image.load(os.path.join(self.game.assets_dir, "planet3.png")).convert_alpha()
        self.planet_choice = [planet1, planet2, planet3]
        self.planet = random.choice(self.planet_choice)
        
        # Declare moon stuff
        self.moon1 = pygame.image.load("assets/moon1.png").convert_alpha()
        self.moon2 = pygame.image.load("assets/moon2.png").convert_alpha()
        self.moon3 = pygame.image.load("assets/moon3.png").convert_alpha()
        self.moon1c = random.getrandbits(1)
        self.moon2c = random.getrandbits(1)
        self.moon3c = random.getrandbits(1)
        self.moons = 0
        
    def renderPlanets(self, surf, pos, originPos, angle):
        #Declare planet vars.
        planet_rect = self.planet.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - planet_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_planet_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_planet = pygame.transform.rotate(self.planet, angle)
        rotated_planet_rect = rotated_planet.get_rect(center=rotated_planet_center)
        surf.blit(rotated_planet, rotated_planet_rect)

        
    def renderMoons(self, surf, image, pos, originPos, angle):
        # Declare moon vars
        moon_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - moon_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
        surf.blit(rotated_image, rotated_image_rect)
        
# fmt: on
    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.scroll -= 5
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0
        for i in range(0, self.tiles):
            display.blit(self.bg, (i * self.bg_width + self.scroll, 0))

        # Declare planet vars.
        pos = (self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
        w, h = self.planet.get_size()
        
        self.renderPlanets(display, pos, (w / 2, h / 2), self.angle)
        self.angle += 1
        if self.moon1c == 1:
            self.renderMoons(display, self.moon1, pos, (self.wid, self.hei), self.angle)
        if self.moon2c == 1:
            self.renderMoons(display, self.moon2, pos, (self.wid, self.hei), self.angle)
        if self.moon3c == 1:
            self.renderMoons(display, self.moon3, pos, (self.wid, self.hei), self.angle)

        display.blit(self.menu, (0, 0))
        self.game.draw_text(display, f"Planet: {self.f}", (0, 0, 0), 180, 120)
        self.game.draw_text(display, f"Moons: {self.moons}", (0, 0, 0), 170, 200)
