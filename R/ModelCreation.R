woodchuck <- read.csv(file = '../Data/woodchuck_data.csv')

mylogit <- glm(formula = Distance.chucked.in.meters ~ Distance.in.kilometers + factor(Wind.Direction) + Age + Temp + Humity, data=woodchuck)

saveRDS(mylogit, "./WoodChuckModel.R")