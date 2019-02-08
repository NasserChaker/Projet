#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:18:55 2019

@author: 3700052
"""
from soccersimulator import Ball,settings, Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools  import SimpleStrategy,SuperState
from soccersimulator.settings  import GAME_WIDTH, GAME_HEIGHT,PLAYER_RADIUS,BALL_RADIUS,maxPlayerShoot

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-0.5 ,0.5),
                            Vector2D.create_random(-0.5 ,0.5))
    

"""class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        if (id_team == 1) :
            return SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position,
                            Vector2D(150, 45) - state.player_state(id_team ,id_player).position)
        else :
            return Soccer.add("Défenseur",SimpleStrategy(defenseur2,'def'))


       
class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        if (id_team == 1) :
            if (state.ball.position.x > state.ball.position.y) :
                while (state.ball.position - state.player_state(id_team ,id_player).position)>3:
                   SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(state.ball.position.x, 0)- state.ball.position)
                for i in range(0,150-state.ball.position.x):
                    SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(state.ball.position.x + i, 0)- state.ball.position)
            else : 
                while (state.ball.position - state.player_state(id_team ,id_player).position)>3:
                   SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(0, state.ball.position.y)- state.ball.position)
                for i in range(0,90-state.ball.position.y):
                    SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(0, state.ball.position.y + i)- state.ball.position)
     else : 
            if (state.ball.position.x > state.ball.position.y) :
                while (state.ball.position - state.player_state(id_team ,id_player).position)>3:
                   SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(state.ball.position.x, 0)- state.ball.position)
                for i in range(0,150-state.ball.position.x):
                    SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(state.ball.position.x + i, 0)- state.ball.position)
             else : am ,id_player).position))
                while (state.ball.position - state.player_state(id_team ,id_player).position)>3:
                   SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(0, state.ball.position.y)- state.ball.position)
                for i in range(0,90-state.ball.position.y):
                    SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position, Vector2D(0, state.ball.position.y + i)- state.ball.position)
                    
                    
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        if (id_team == 1) :
            if (state.ball.position.x<75):
                return SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position,
                            Vector2D(150, 45) - state.player_state(id_team ,id_player).position)
            else:
                return SoccerAction(Vector2D.create_random(-0.5 ,0.5),
                            Vector2D.create_random(-0.5 ,0.5))
        else :
            if (state.ball.position.x>75):
                return SoccerAction(state.ball.position - state.player_state(id_team ,id_player).position,
                            (Vector2D(0, 45) - state.player_state(id_team ,id_player).position))
            else:
                return SoccerAction(Vector2D.create_random(-0.5 ,0.5),
                            Vector2D.create_random(-0.5 ,0.5))
"""                
def gobetter(state) : 
     if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=state.goal-state.player)
     else :
        return SoccerAction (acceleration=state.ballameliorer-state.player)
    
    
                
def gobetterdef (state):
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=state.coequipier-state.player)
    else :
        return SoccerAction (acceleration=state.ballameliorer-state.player)

    
def defenseur2 (state):
    if state.teamdef[1] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetterdef(state)


    
def gobetteratt (state):
    if state.teamatt[0] :
        if state.player.y < GAME_HEIGHT/2 :
            if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
                return SoccerAction(shoot=Vector2D(state.teamatt[1], 0)-state.player)
            else :
                return SoccerAction (acceleration=state.ballameliorer-state.player)
        else : 
            if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
                return SoccerAction(shoot=Vector2D(state.teamatt[1], GAME_HEIGHT)-state.player)
            else :
                return SoccerAction (acceleration=state.ballameliorer-state.player)
    else : 
        if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
            return SoccerAction(shoot=state.goal-state.player)
        else :
            return SoccerAction (acceleration=state.ballameliorer-state.player)
        
def attaquant2(state):
    if not state.teamdef[1] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetteratt(state) 




    # Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

    # Add players
#team1.add("Go",SimpleStrategy(gobetter,'Go'))
#team2.add("Go",SimpleStrategy(gobetter,'Go'))
team1.add("Att",SimpleStrategy(attaquant2,'Att'))
team1.add("Def",SimpleStrategy(defenseur2,'Def'))
team2.add("Def",SimpleStrategy(defenseur2,'Def'))
team2.add("Att",SimpleStrategy(attaquant2,'Att'))

 """   # Create a match
simu = Simulation ( team1 , team2 )
    
    # Simulate and display the match
show_simu ( simu )"""
