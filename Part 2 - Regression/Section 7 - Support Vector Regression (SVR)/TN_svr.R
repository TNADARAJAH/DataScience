

dataset = read.csv('Position_salaries.csv')
dataset = dataset[2:3]

install.packages('caTools')
library('caTools')

X=dataset$Level
y=dataset$Salary

install.packages('e1071')
library('e1071')

regressor = svm(formula = Salary~., data = dataset, type = 'eps-regression', kernel = 'radial')

y_pred = predict(regressor, data.frame(Level = 6.5))

library(ggplot2)


ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary), colour='Red')+
  geom_line(aes(x=dataset$Level, y = predict(regressor, newdata=dataset)), colour = 'blue')+
  xlab('Level')+
  ylab('Salary')+
  ggtitle('Level/Salary')

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot()+             
  geom_point(aes(x=dataset$Level, y=dataset$Salary), colour='red')+
  geom_line(aes(x=x_grid, y = predict(regressor, newdata=data.frame(Level=x_grid))), colour = 'blue')+
  xlab('Level')+
  ylab('Salary')+
  ggtitle('Level/Salary - HD')

