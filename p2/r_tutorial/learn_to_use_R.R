rm(list =ls(envir = globalenv()), envir = globalenv()); if(is.null(dev.list())) dev.off(); gc(); cat("\014")

setwd('C:/Users/User/repos/lis4369/a5/r_tutorial/')

# pdf(file ="C:/Users/User/repos/lis4369/a5/r_tutorial/myplotfile.pdf")

# install.packages("quantmod", dependencies = TRUE)
# install.packages("dplyr", dependencies = TRUE)
# install.packages("ggplot2", dependencies = TRUE)

# update.packages(ask = FALSE, checkBuilt =  TRUE)

# installed.packages()


# library("quantmod")
# getSymbols("AAPL")
# 
# barChart(AAPL)
# barChart(AAPL, subset='last 14 days')
# chartSeries(AAPL, subset='last 14 days')
# barChart(AAPL['2013-04-1::2013-04-12'])
# barChart(AAPL['2013-03-1::'])
# barChart(AAPL['2020'])




# 
library(ggplot2)
qplot(disp, mpg, data=mtcars)
qplot(disp, mpg, ylim=c(0,35), data=mtcars)
qplot(cty, hwy, data = mpg)
qplot(cty, hwy, data = mpg, geom="jitter")
ggplot(mtcars, aes(x=disp, y=mpg)) + geom_point()
ggplot(mtcars, aes(x=disp, y=mpg)) + geom_line()
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line()
# 
# 
# str(mtcars)

