# Data Preprocessing Template
setwd("~/projects/machine_learning/Part 1 - Data Preprocessing")
# Importing the dataset
dataset = read.csv('dataset/Data.csv')  #Indexes start at 1



# Taking care of missing data

# ifelse(condition, value if condition is true, value if condition is false)
# is.na => returns True If value in the column Age is missing
# ave(column, function to calculate mean)

# The general idea in R is that NA stands for "unknown".  
# If some of the  values in a vector are unknown, then the mean of the vector is also unknown.

# na.rm = TRUE => exclude the missing values while calculating the mean of the values
dataset$Age = ifelse(is.na(dataset$Age),
	ave(dataset$Age, FUN= function(x) mean(x,na.rm = TRUE)),
	dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
	ave(dataset$Salary, FUN= function(x) mean(x,na.rm = TRUE)),
	dataset$Salary)



# Encoding Categorical data
# factor(column, vector_of_categories, number_u_want_to_correspond_to_each_category)
dataset$Country = factor(dataset$Country,
						levels=c('France','Spain','Germany'),
						labels=c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
						levels=c('Yes','No'),
						labels=c(1,0))
