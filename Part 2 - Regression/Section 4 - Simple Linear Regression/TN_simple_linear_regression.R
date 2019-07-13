

dataset = read.csv('Salary_data.csv')

install.packages('caTools')
library(caTools)

set.seed(123)

split=sample.split(dataset$Salary, SplitRatio = 2/3)

training_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

y_pred = predict(regressor, newdata=test_set)

install.packages('ggplot2')
library(ggplot2)


ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y = training_set$Salary, color='Red')) +
  geom_line(aes(x=training_set$YearsExperience, y = predict(regressor, newdata=training_set), colour='Blue')) +
  ggtitle('Years/Salary - training Set') +
  xlab('Years') +
  ylab('Salary')

ggplot()+
  geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary, color='Red')) +
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata=training_set), color='Blue')) +
  ggtitle('Years/Salary - test Set') +
  xlab('Years') +
  ylab('Salary')




