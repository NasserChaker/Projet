from Nasser.goalsearch import GoalSearch
from Nasser.tools import GoTestStrategy


expe = GoalSearch(strategy = GoTestStrategy(), params={'strength': [0.15,0.25]})
expe.start()
print(expe.get_res())
print(expe.get_best())