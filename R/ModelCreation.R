woodchuck <- read.csv(file = '../Data/woodchuck_data.csv')

mylogit <- glm(formula = Distance.chucked.in.meters ~ Distance.in.kilometers + factor(Wind.Direction) + Age + Temp + Humity, data=woodchuck)

# Would expect some metrics here to show that the model is mathmatically sound

saveRDS(mylogit, "./WoodChuckModel.R")