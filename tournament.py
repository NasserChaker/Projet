from socceria.strategies import defenseur2 , RandomStrategy , gobetter
from soccersimulator import SoccerTeam
from socceria.tools import SimpleStrategy,SuperState

def get_team ( nb_players ):
    team = SoccerTeam ( name = " Nasser’s ␣ Team " )
    if nb_players == 1:
        team.add("Attaquant",SimpleStrategy(gobetter,'Go - better'))
    if nb_players == 2:
        team.add("Attaquant",SimpleStrategy(gobetter,'Go'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    return team

if __name__ == '__main__ ':
    from soccersimulator import Simulation , show_simu
    
    # Check teams with 1 player and 2 players
    team1 = get_team (1)
    team2 = get_team (2)
    
    # Create a match
    simu = Simulation ( team1 , team2 )
    
    # Simulate and display the match
    show_simu ( simu )
