# Data Preprocessing Template

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
