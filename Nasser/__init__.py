from Nasser.strategies import defenseur2 , RandomStrategy , gobetter,attaquant2,one, gardien, milieu1
from soccersimulator import SoccerTeam
from Nasser.tools import SimpleStrategy, SuperState, GoTestStrategy

def get_team (nb_players):
    team = SoccerTeam(name = "Nasser’s Team")
    if (nb_players == 1):
        team.add("One",SimpleStrategy(one,'One'))
    if nb_players == 2:
        team.add("Attaquant",SimpleStrategy(attaquant2,'Att'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    if nb_players == 4: 
        team.add("Attaquant",SimpleStrategy(attaquant2,'Att'))
        team.add("Milieu",SimpleStrategy(milieu1,'Mil'))
        team.add("Milieu",SimpleStrategy(milieu1,'Mil'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    return team
