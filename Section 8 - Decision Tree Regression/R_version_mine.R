# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#install.packages('rpart')
library(rpart)

regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5))

#install.packages('ggplot2')
library(ggplot2)

# The code below is not high reolution therefore the graph is wrong
# Get the high resolution code from the regression template
# ggplot() + 
#   geom_point(aes(x = dataset$Level, y = dataset$Salary), 
#             colour = 'red') + 
#   geom_line(aes(x=dataset$Level, y = predict(regressor, newdata = dataset)),
#             colour = 'blue') +
#   ggtitle('Truth or Bluff ( Decision Tree Regression') + 
#   xlab('Level') +
#   ylab('Salary') 

# The high resolution template
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Regression Model)') +
  xlab('Level') +
  ylab('Salary')