from Nasser.strategies import defenseur2 , RandomStrategy , gobetter,attaquant2 ,one, gardien, milieu1, defenseur3, defenseur4, attaquant3, attaquant4
from soccersimulator import SoccerTeam
from Nasser.tools import SimpleStrategy, SuperState, GoTestStrategy

def get_team (nb_players):
    team = SoccerTeam(name = "Nasser’s Team")
    if (nb_players == 1):
        team.add("One",SimpleStrategy(one,'One'))
    if (nb_players == 2):
        team.add("Attaquant",SimpleStrategy(attaquant2,'Att'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    if (nb_players == 4): 
        team.add("d3",SimpleStrategy(defenseur3,'Def3'))
        team.add("d4",SimpleStrategy(defenseur4,'def4'))
        team.add("a3",SimpleStrategy(attaquant3,'att3'))
        team.add("a4",SimpleStrategy(attaquant4,'Att4'))
    return team
