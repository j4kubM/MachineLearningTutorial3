# keyboardAgents.py
# -----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley.
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import Agent
from game import Directions
from game import GameStateData
import random


##Isa
import sys


class KeyboardAgent(Agent):
   # NOTE: Arrow keys also work.
    WEST_KEY  = 'a'
    EAST_KEY  = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'

    def __init__( self, index = 0 ):

        self.lastMove = Directions.STOP
        self.index = index
        self.keys = []

    def getAction( self, state):
        from graphicsUtils import keys_waiting
        from graphicsUtils import keys_pressed
        keys = keys_waiting() + keys_pressed()
        if keys != []:
            self.keys = keys

        legal = state.getLegalActions(self.index)
        move = self.getMove(legal)

        if move == Directions.STOP:
            # Try to move in the same direction as before
            if self.lastMove in legal:
                move = self.lastMove

        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP

        if move not in legal:
            move = random.choice(legal)

        self.lastMove = move
        return move

    def getMove(self, legal):
        move = Directions.STOP
        if   (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if   (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if   (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if   (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move        
    def printLineData(self, gameState):
            """Program a method called printLineData() inside the BasicAgentAA agent from the bustersAgents.py 
                This method should return a string with the information from the Pac-Man state you consider relevant.
                Then, you call this method from the main loop of the game in Game.py to write the information to a file
                For each tick, you should store a line with all the considered information, splitting each data with commas.
                Moreover, each time a new game starts, the new lines must be appended below the old ones. You should not
                rewrite the file when a new game starts
            """
            pos=gameState.getPacmanPosition()
            posX=pos[0]
            posY=pos[1]
            North=False
            South=False
            East=False
            West=False
            actions=gameState.getLegalPacmanActions() 
            if 'North' in str(actions):
                North=True
            if 'East' in str(actions):
                East=True
            if 'West' in str(actions):
                West=True
            if 'South' in str(actions):
                South=True
            direction=str(gameState.data.agentStates[0].getDirection())
            ghosts=gameState.getGhostPositions()
            g1X=ghosts[0][0]
            g1Y=ghosts[0][1]
            g2X=ghosts[1][0]
            g2Y=ghosts[1][1]
            g3X=ghosts[2][0]
            g3Y=ghosts[2][1]
            g4X=ghosts[3][0]
            g4Y=ghosts[3][1]
            result=[posX, posY, North, East, South, West, direction, g1X, g1Y, g2X, g2Y, g3X, g3Y, g4X, g4Y ]
            #print(result)
            return result
        
