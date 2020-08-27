# FPL_DreamTeam
A simple program for optimizing a Fantasy Premier League team within game constraints. The program uses the MIP library to conduct optimization within constraints and is based on the "0/1 Knapsack Problem" which can be found at https://docs.python-mip.com/en/latest/examples.html . 

## Run
With Python, MIP, and Pandas libraries installed call 'python dreamteam.py' from directory where dreamteam.py and elements.csv are saved.

## Data
elements.csv is from FPL API.

To reproduce instead of download, simply use the following script:

```python
import json

import requests

import pandas as pd

d=json.loads(requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').text)

df=pd.json_normalize(d['elements'])

df.to_csv('C:/Users/nath1/Documents/CS/105/project/dreamteam/' + 'elements' + '.csv')
```

## Output
Outputs dreamteam.csv with players, cost, total points last season and other relevant player features. This team will be within the FPL game constraints outlined in the program.

Also outputs total cost and total points of the team last season.

## Notes
* In the current state the program is not inclusive of bench players as bench player appearances are uncertain and bench management optimization is far more complex.
* This program could be easily adapted to maximize another feature, such as predicted points.
* With predicted points feature, this program could be expanded to a player transfer recommendation system. 
