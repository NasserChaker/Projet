from Nasser.strategies import defenseur2 , RandomStrategy , gobetter,attaquant2,one, gardien
from soccersimulator import SoccerTeam
from Nasser.tools import SimpleStrategy, SuperState, GoTestStrategy
def get_team (nb_players):
    team = SoccerTeam ( name = " Nasser’s ␣ Team " )
    if (nb_players == 1):
        team.add("one",SimpleStrategy(one,'Nasser'))
    if nb_players == 2:
        team.add("Attaquant",SimpleStrategy(attaquant2,'att'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    return team
