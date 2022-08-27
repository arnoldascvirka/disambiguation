###################################################################################################
#
# navigation.py
# Module to run the navigation state.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import Libraries
import pygame, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Import modules
from states.state import State
from states.cluster import Star
from gridsql import Grid

# Create engine
engine = create_engine("sqlite:///grid.db")
Session = sessionmaker(bind=engine)
session = Session()


class Navigation(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        self.column = None

    def update(self, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        # Define colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Define WIDTH and HEIGHT of each grid location
        WIDTH = 25
        HEIGHT = 25

        # Define margin between each cell
        MARGIN = 5

        # Draw stuff
        display.fill(BLACK)
        self.game.draw_text(
            display,
            "Navigation",
            (255, 255, 255),
            self.game.SCREEN_WIDTH / 2 + 395,
            self.game.SCREEN_HEIGHT / 2 - 350,
        )

        self.game.draw_text(
            display,
            "Select star cluster.",
            (255, 255, 255),
            self.game.SCREEN_WIDTH / 2 + 392,
            self.game.SCREEN_HEIGHT / 2 - 250,
        )

        # Create a 2D array.
        grid = []
        for row in range(26):
            # Add an empty array that will hold each cell
            grid.append([])
            for column in range(25):
                grid[row].append(0)

        # Set row 1, cell 5 to one.
        grid[1][5] = 1

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                obj = session.query(Grid).all()
                if (
                    session.query(Grid.row).filter_by(row=row)
                    and session.query(Grid.column).filter_by(column=column) is None
                ):
                    moons = None
                    name = None
                    projects = Grid(column, row, moons, name)
                    session.add(projects)
                    session.commit()
                new_state = Star(self.game)
                new_state.enter_state()

        for row in range(26):
            for column in range(25):
                color = WHITE
                pygame.draw.rect(
                    display,
                    color,
                    [
                        (MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT,
                    ],
                )
