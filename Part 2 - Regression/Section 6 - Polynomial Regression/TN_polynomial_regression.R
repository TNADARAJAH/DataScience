

dataset = read.csv('Position_Salaries.csv')


dataset=dataset[,2:3]


dataset1 = read.csv('Position_Salaries.csv')
dataset1 = dataset1[2:3]


lin_reg = lm(formula=Salary~., data=dataset)

dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

poly_reg=lm(formula = Salary~., data=dataset)

install.packages('ggplot2')
library('ggplot2')

ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary), color = 'Red')+
#  geom_line(aes(x=dataset$Level, y=predict(lin_reg), color = 'Blue'))+
  geom_line(aes(x=dataset$Level, y=predict(lin_reg, newdata=dataset$level)), colour = 'blue')+
  ggtitle('Level V Salary')+
  xlab('Level')+
  ylab('Salary')

ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary), color = 'Red')+
  #  geom_line(aes(x=dataset$Level, y=predict(lin_reg), color = 'Blue'))+
  geom_line(aes(x=dataset$Level, y=predict(poly_reg, newdata=dataset)), colour = 'blue')+
  ggtitle('Level V Salary')+
  xlab('Level')+
  ylab('Salary')

x_grid = seq(min(dataset$Level),max(dataset$Level), 0.1)

newdf=data.frame(Level = x_grid,
                 Level2 = x_grid^2,
                 Level3 = x_grid^3,
                 Level4 = x_grid^4)

ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary), color = 'Red')+
  #  geom_line(aes(x=dataset$Level, y=predict(lin_reg), color = 'Blue'))+
  geom_line(aes(x=x_grid, y=predict(poly_reg, newdata=newdf)), colour = 'blue')+
  ggtitle('Level V Salary')+
  xlab('Level')+
  ylab('Salary')





