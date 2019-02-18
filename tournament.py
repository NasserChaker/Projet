from Nasser import get_team

from soccersimulator import Simulation , show_simu
    
# Check teams with 1 player and 2 players
team1 = get_team (2)
team2 = get_team (2)
    
# Create a match
simu = Simulation ( team1 , team2 )
    
# Simulate and display the match
show_simu ( simu )
