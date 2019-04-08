from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator.settings  import GAME_WIDTH, GAME_HEIGHT,PLAYER_RADIUS,BALL_RADIUS,maxPlayerShoot

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))

    
class One(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        ball = state.ball.position
        player = state.player_state(id_team,id_player).position
        ballam = state.ball.position + 5 * state.ball.vitesse
        if id_team == 1 :
            opp = state.player_state(2,0).position
            if ball.x < GAME_WIDTH*(1/2) :
                if opp.x < GAME_WIDTH*(3/4) and opp.y < GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH, GAME_HEIGHT)
                if opp.x >= GAME_WIDTH*(3/4) and opp.y < GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH*(1/2), GAME_HEIGHT)
                if opp.x < GAME_WIDTH*(3/4) and opp.y >= GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH, 0)
                if opp.x >= GAME_WIDTH*(3/4) and opp.y >= GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH*(1/2), GAME_HEIGHT)
                return SoccerAction(acceleration=ballam-player,
                            shoot=tir-player)
            else : 
                return SoccerAction(acceleration=Vector2D(GAME_WIDTH*(1/4),GAME_HEIGHT*(1/2))-player,shoot=opp-player)
        else : 
            opp = state.player_state(1,0).position
            if ball.x > GAME_WIDTH*(1/2) :
                if opp.x < GAME_WIDTH*(1/4) and opp.y < GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH*(2/4), GAME_HEIGHT)
                if opp.x >= GAME_WIDTH*(1/4) and opp.y < GAME_HEIGHT*(1/2) :
                    tir = Vector2D(0, GAME_HEIGHT)
                if opp.x < GAME_WIDTH*(1/4) and opp.y >= GAME_HEIGHT*(1/2) :
                    tir = Vector2D(GAME_WIDTH*(2/4), 0)
                if opp.x >= GAME_WIDTH*(1/4) and opp.y >= GAME_HEIGHT*(1/2) :
                    tir = Vector2D(0,0)
                return SoccerAction(acceleration=ballam-player,
                            shoot=tir-player)
            else :
                return SoccerAction(acceleration=Vector2D(GAME_WIDTH*(3/4),GAME_HEIGHT*(1/2))-player,
                                    shoot=opp-player)     
        


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", One())  # Random strategy
team2.add("Player 2", One())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)