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
                    
def gobetter(state) : 
     if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=state.goal-state.player)
     else :
        return SoccerAction (acceleration=state.ballameliorer-state.player)
    
                
def gobetterdef (state):
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=state.goal-state.player)
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
    if state.teamatt[2] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetteratt(state) 
    
    
def one(state):
    if state.bouge == True : 
        if (state.ball.x == GAME_WIDTH/2) and (state.ball.y == GAME_HEIGHT/2) and state.player.distance(state.ball)<1+PLAYER_RADIUS + BALL_RADIUS :
            return SoccerAction(state.ballameliorer-state.player, state.goal-state.player)
        if (state.devant == True) and state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS: 
            return SoccerAction(state.ballameliorer-state.player,(state.goal-state.player).normalize()*3)
        else :
            return gobetter(state)
    else : 
        if (state.ball.x == GAME_WIDTH/2) and (state.ball.y == GAME_HEIGHT/2) and state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
            return SoccerAction(state.ballameliorer-state.player, (state.goal-state.player).normalize()*2)
        else : 
            return gobetter(state)
            
        
def gardien(state) : 
     return SoccerAction(0, state.goal-state.player)

def milieu1(state) :
    if state.teammil:
        if state.distancemil == True :
            return SoccerAction(Vector2D(GAME_WIDTH*(1/3), state.coequipier2.y)-state.player, state.goal-state.player)
        else :
           return gobetter(state) 
    else :
        if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
            if state.devantmil == True :
                return SoccerAction(state.ballameliorer-state.player,(state.coequipier2-state.player))
            else :
                if state.player.distance(state.goal) < 30 : 
                    return SoccerAction(state.ballameliorer-state.player, state.goal-state.player)
                else : 
                    return SoccerAction(state.ballameliorer-state.player,state.coequipier0-state.player)
                


           
 
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    