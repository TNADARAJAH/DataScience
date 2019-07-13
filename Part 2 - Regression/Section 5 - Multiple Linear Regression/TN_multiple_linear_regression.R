

dataset = read.csv('50_startups.csv')

dataset$State=factor(dataset$State, labels=c(1, 2, 3))


install.package(caTools)

library(caTools)
set.seed(123)

split = sample.split(dataset$Profit, SplitRatio = 0.8)

training_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = training_set)

y_pred = predict(regressor, data = test_set)

summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = training_set)

y_pred = predict(regressor, data = test_set)

summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = training_set)

y_pred = predict(regressor, data = test_set)

summary(regressor)

maxVar = max(coef(summary(regressor))[c(2:5), "Pr(>|t|)"])


coef(summary(regressor))
