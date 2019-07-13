
dataset = read.csv('Data.csv')

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN=function(x) mean(x, na.rm=TRUE)),
                     dataset$Age
                     )

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$salary, FUN = function(x) mean(x, na.rm=TRUE)),
                        dataset$Salary
                        )

dataset$Country = factor(dataset$Country, 
                         labels=c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           labels=c(1,2))


