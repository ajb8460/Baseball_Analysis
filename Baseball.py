from pybaseball import batting_stats
from pybaseball import pitching_stats
from pybaseball import statcast

import pandas as pd


Batting = batting_stats(2024)

Pitching = pitching_stats(2024)

#good_players = Batting[Batting['WAR'] >= 3]

#print(Batting)

from pybaseball import teamid_lookup

abbrevs = teamid_lookup()['team_abbrev']


'''from pybaseball import standings
data = standings(2016)[1]
print(data)'''