from Nasser.goalsearch import GoalSearch
from Nasser.tools import GoTestStrategy


expe = GoalSearch(strategy = GoTestStrategy(), params={'strength': [0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25]})
expe.start()
print(expe.get_res())
print(expe.get_best())