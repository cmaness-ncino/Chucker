from statsmodels.formula.api import glm
import statsmodels.api as sm
import pandas as pd
import subprocess
import os
import sqlite3
from statsmodels.genmod.generalized_linear_model import GLMResults

def main():
    model = retreive_models()["glm"]
    
    conn = setup_database_connection()

    age = retreive_age_from_id(1, conn)

    # set the input params and transform it into a dataframe
    data = {
        'Wind Direction':[360], 
        'Temp':[80], 
        'Humity':[0.059], 
        'Distance in kilometers':[99], 
        'Age':[age]}
    df = pd.DataFrame(data) 
    
    print(model.predict(df.iloc[0])[0])
    

def retreive_models():
    return {"glm": GLMResults.load('models/woodchuck_distance.pickle')}

def retreive_age_from_id(id, conn):
    id_tuple = (id,)
    c = conn.cursor()
    c.execute('SELECT Age FROM WoodChucks WHERE Id=?', id_tuple)
    return c.fetchone()[0]

def setup_database_connection():
    return sqlite3.connect('../../Database/WoodChuckLookup.db')

if __name__ == "__main__":
    main()