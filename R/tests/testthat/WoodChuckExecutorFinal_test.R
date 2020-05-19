source("../../WoodChuckExecutorFinal.R", chdir = TRUE)
library(testthat)

test_that("Handle out of range wind direction", {
  expect_error(
    EstimateChuckingDistance(
        wind_direction=361, 
        temp=80, 
        humidity=0.059, 
        water_distance=99, 
        chuck_id=1),
    "Variable wind_direction is out of bounds. Value Should be between 0 and 360", 
    fixed=TRUE
  )
})

test_that("Handle out of range humidity", {
  expect_error(
    EstimateChuckingDistance(
        wind_direction=360, 
        temp=80, 
        humidity=2, 
        water_distance=99, 
        chuck_id=1),
    "Variable humidity is out of bounds. Value should be between 0 and 1", 
    fixed=TRUE
  )
})