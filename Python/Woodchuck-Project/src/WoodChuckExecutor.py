from statsmodels.formula.api import glm
import statsmodels.api as sm
import pandas as pd
import sqlite3
from statsmodels.genmod.generalized_linear_model import GLMResults

def main():
    print("Executing WoodChuck Model")

    model = GLMResults.load('models/woodchuck_distance.pickle')
    conn = sqlite3.connect('../../Database/WoodChuckLookup.db')

    c = conn.cursor()
    c.execute('SELECT Age FROM WoodChucks WHERE Id=1')

    # set the input params and transform it into a dataframe
    data = {
        'Wind Direction':[360], 
        'Temp':[80], 
        'Humity':[0.059], 
        'Distance in kilometers':[99], 
        'Age':[c.fetchone()[0]]}
    df = pd.DataFrame(data) 
    
    print(model.predict(df.iloc[0])[0])


if __name__ == "__main__":
    main()