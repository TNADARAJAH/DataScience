

dataset = read.csv('Position_Salaries.csv')

dataset=dataset[,2:3]
library('ggplot2')

install.packages('rpart')
library('rpart')

regressor = rpart(formula=Salary~., data=dataset, control = rpart.control(minsplit = 1))

X_grid=seq(min(dataset$Level), max(dataset$Level), 0.01)

xdf=data.frame(Level=X_grid)

ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary), colour='red')+
  geom_line(aes(x=X_grid, y=predict(regressor,newdata=data.frame(Level=X_grid))), colour='blue')+
  xlab('Position')+
  ylab('Salary')+
  ggtitle('Decision Tree')

