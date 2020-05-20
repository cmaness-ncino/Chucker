#!/usr/bin/env Rscript
library(RSQLite)
options(warn=-1)

EstimateChuckingDistance <- function(wind_direction, temp, humidity, water_distance, chuck_id){
    mylogit <- readRDS(file = "./WoodChuckModel.R")

    db <- dbConnect(RSQLite::SQLite(), dbname="../Database/WoodChuckLookup.db")
    age <- dbGetQuery(db, paste("SELECT Age FROM WoodChucks where Id=", chuck_id))[["Age"]]

    newdata = data.frame(
        Wind.Direction=wind_direction, 
        Temp=temp, 
        Humity=humidity, 
        Distance.in.kilometers=water_distance, 
        Age=age)

    prediction <- predict(mylogit, newdata)

    print(prediction[["1"]])
}

EstimateChuckingDistance(wind_direction=124, temp=80, humidity=0.059, water_distance=99, chuck_id=1)