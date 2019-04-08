from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))

    
class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        ball = state.ball.position
        player = state.player_state(id_team,id_player).position
        if id_team == 1 :
            opp = state.player_state(2,id_player).position
        else : 
            opp = state.player_state(1,id_player).position
        return SoccerAction(acceleration=ball-player,
                            shoot=opp-player)
        


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Echauffement())  # Random strategy
team2.add("Player 2", Echauffement())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)