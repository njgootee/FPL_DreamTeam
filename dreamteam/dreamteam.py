from mip import *
import pandas as pd

def dreamteam(budget):
    '''
    Initializations
    '''
    #Read data
    df = pd.read_csv("elements.csv")

    #Initialize indexes 
    I = range(len(df))

    #Initialize model
    m = Model()

    #Selection variable
    x = [m.add_var(var_type=BINARY) for i in I]

    #Model objective: Maximize total points from previous season
    m.objective = maximize(xsum(df["total_points"][i] * x[i] for i in I))
    
    '''
    Constraints
    '''
    #Must not exceed budget
    m += xsum(df["now_cost"][i] * x[i] for i in I) <= budget
    
    #Must be exactly 11 players
    m += xsum(x[i] for i in I) == 11
    
    #Must not have more than 3 players from each team
    for team_code in df["team_code"].unique():
        m += xsum(x[i] for i in I if df["team_code"][i] == team_code) <= 3

    #Must have exactly 1 goalkeeper
    m += xsum(x[i] for i in I if df["element_type"][i] == 1) == 1

    #Must have between 3 and 5 defenders
    m += xsum(x[i] for i in I if df["element_type"][i] == 2) >= 3
    m += xsum(x[i] for i in I if df["element_type"][i] == 2) <= 5

    #Must have between 2 and 5 midfielders
    m += xsum(x[i] for i in I if df["element_type"][i] == 3) >= 2
    m += xsum(x[i] for i in I if df["element_type"][i] == 3) <= 5

    #Must have between 1 and 3 forwards
    m += xsum(x[i] for i in I if df["element_type"][i] == 4) >= 1
    m += xsum(x[i] for i in I if df["element_type"][i] == 4) <= 3

    '''
    Optimize model
    '''
    m.optimize()

    '''
    Output Results
    '''
    #Build and save dreamteam 
    selected = [i for i in I if x[i].x >= 0.99]
    team_df = df[["id", "first_name", "second_name", "total_points", "now_cost", "team_code", "element_type"]].iloc[selected].copy()
    team_df.to_csv('dreamteam.csv')

    #Output total cost and total points from last season
    print("Total Cost: ", team_df["now_cost"].sum(), "Total points: ", team_df["total_points"].sum())

#Execute function, 830 is typical budget for starting 11 when filling bench with 'fodder' players
dreamteam(budget=830)