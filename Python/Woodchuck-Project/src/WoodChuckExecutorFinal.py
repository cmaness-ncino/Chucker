from statsmodels.formula.api import glm
import statsmodels.api as sm
import pandas as pd
import sqlite3
from statsmodels.genmod.generalized_linear_model import GLMResults

def main():
    print(estimate_chucking_distance(wind_direction=360, temp=80, humidity=0.059, water_distance_in_kilometers=99, chucker_id=1))

def estimate_chucking_distance(wind_direction = 0, temp=0, humidity=0, water_distance_in_kilometers=0, chucker_id=None):
    model = retreive_models()["glm"]

    if wind_direction > 360 or wind_direction < 0:
        raise Exception('Variable wind_direction is out of bounds. Value Should be between 0 and 360')
    if humidity > 1 or humidity < 0:
        raise Exception('Variable humidity is out of bounds. Value should be between 0 and 1')
    
    conn = setup_database_connection()

    age = retreive_age_from_id(chucker_id, conn)

    # set the input params and transform it into a dataframe
    data = {
        'Wind Direction':[wind_direction], 
        'Temp':[temp], 
        'Humity':[humidity], 
        'Distance in kilometers':[water_distance_in_kilometers], 
        'Age':[age]}
    df = pd.DataFrame(data) 
    
    distance_of_wood_chucked = model.predict(df.iloc[0])[0]

    return distance_of_wood_chucked

def retreive_models():
    return {"glm": GLMResults.load('models/woodchuck_distance.pickle')}

def retreive_age_from_id(id, conn):
    id_tuple = (id,)
    
    c = conn.cursor()
    c.execute('SELECT Age FROM WoodChucks WHERE Id=?', id_tuple)
    age = c.fetchone()[0]

    return age

def setup_database_connection():
    return sqlite3.connect('../../Database/WoodChuckLookup.db')

if __name__ == "__main__":
    main()