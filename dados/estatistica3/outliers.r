boxplot(iris$Sepal.Width)
boxplot(iris$Sepal.Width, outline=F)

boxplot.stats(iris$Sepal.Width)

boxplot.stats(iris$Sepal.Width)$out

#install.packages('outliers')

library(outliers)

outlier(iris$Sepal.Width)
  