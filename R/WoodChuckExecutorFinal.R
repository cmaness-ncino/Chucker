#!/usr/bin/env Rscript
library(RSQLite)
options(warn=-1)

EstimateChuckingDistance <- function(wind_direction, temp, humidity, water_distance, chuck_id){
    models <- PrepareModels()
    mylogit <- models$mylogit_model

    if(wind_direction > 360 || wind_direction < 0){
        stop("Variable wind_direction is out of bounds. Value Should be between 0 and 360")
    }

    if(humidity > 1 || humidity < 0){
        stop("Variable humidity is out of bounds. Value should be between 0 and 1")
    }

    age <- RetreiveAgeFromId(chuck_id)
    
    newdata = data.frame(
        Wind.Direction=wind_direction, 
        Temp=temp, 
        Humity=humidity, 
        Distance.in.kilometers=water_distance, 
        Age=age)

    prediction <- predict(mylogit, newdata)

    print(prediction[["1"]])
}

PrepareModels <- function(){
    mylogit <- readRDS(file = "./WoodChuckModel.R")
    preparedModels <- list("mylogit_model" = mylogit)
    
    return(preparedModels)
}

RetreiveAgeFromId <- function(chuck_id){
    db <- dbConnect(RSQLite::SQLite(), dbname="../Database/WoodChuckLookup.db")
    woodchuck <- dbGetQuery(db, paste("SELECT Age FROM WoodChucks where Id=", chuck_id))
    
    return(woodchuck[["Age"]])
}

EstimateChuckingDistance(wind_direction=360, temp=80, humidity=0.059, water_distance=99, chuck_id=1)