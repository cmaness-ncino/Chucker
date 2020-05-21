from statsmodels.formula.api import glm
import statsmodels.api as sm
import pandas as pd
import subprocess
import os

def main():
    print("Executing from:")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    print("Reading Data")
    data = pd.read_csv("../../Data/woodchuck_data.csv")
    print(data)

    print("Fitting model")
    formula = "Q('Distance chucked in meters') ~ Q('Distance in kilometers') + Q('Wind Direction') + Q('Age') + Temp + Humity"
    model = glm(formula=formula, data=data).fit()

    # You'd have some mathmatical forms of 
    # verification here - but in this example 
    # we don't care about accuracy just about
    # the process

    model.save("models/woodchuck_distance.pickle")

    print(type(model))

    data = {'Wind Direction':[360], 'Temp':[80], 'Humity':[0.059], 'Distance in kilometers':[99], 'Age':[3]} 
    df = pd.DataFrame(data) 
    
    print(model.predict(df.iloc[0])[0])


if __name__ == "__main__":
    main()