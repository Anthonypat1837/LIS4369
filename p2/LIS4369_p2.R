rm(list =ls(envir = globalenv()), envir = globalenv()); if(is.null(dev.list())) dev.off(); gc(); cat("\014")

setwd('C:/Users/User/repos/lis4369/p2/')

a <- 9
a

a + 5

b <- sqrt(a)
b

c <- c(1,2,5.3,6,-2,4)

print(c)

typeof(c)

is.list(c)
is.vector(c)

d <- c("one", "two", "three")
d

typeof(d)

e <- c(TRUE, TRUE, TRUE, FALSE, TRUE, FALSE)

typeof(e)

d[1]

my_str <- "Hello, World!"
my_str

typeof(my_str)

sqrt(a)

sqrt(c)

a^2

c^2

min(c)

max(c)

mean(c)

sum(c)

# url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"
# titanic <- read.csv(file=url, head=TRUE,sep=",")

# titanic

# summary(titanic)

# dir()

# getwd()

# names(titanic)

# titanic$Name

# titanic$Age

# attributes(titanic)

# ls()


# mean(titanic$Age)

# mean(titanic$Age, na.rm=TRUE)
# median(titanic$Age, na.rm=TRUE)
# quantile(titanic$Age, na.rm=TRUE)
# min(titanic$Age, na.rm=TRUE)
# max(titanic$Age, na.rm=TRUE)
# var(titanic$Age, na.rm=TRUE)
# sd(titanic$Age, na.rm=TRUE)

# summary(titanic$Age, na.rm=TRUE)

# titanic[!complete.cases(titanic),]

# titanic_no_missing_data <- na.omit(titanic)
# titanic_no_missing_data

# pdf(file="C:/Users/User/repos/lis4369/a5/myplotfile.pdf")
# stripchart(titanic_no_missing_data$Age)

# boxplot(titanic_no_missing_data$Age)

# dev.off()


# boxplot(titanic_no_missing_data$Age,
#     main='Distribution of Titanic Passengers Ages',
#     xlab='Ages',
#     horizontal=TRUE)

# plot(titanic_no_missing_data$Age, titanic_no_missing_data$Survived,
#     main="Relationship Between Ages and Survival",
#     xlab="Age",
#     ylab="Survived")

# save.image()

# install.packages("ggpubr")
ggpubr::show_point_shapes()

pdf(file="C:/Users/User/repos/lis4369/p2/lis4369_output.pdf")





#1.

mtcars

#2.

head(mtcars, 10)

#3.

tail(mtcars, 10)

#4.

str(mtcars)

#5.

colnames(mtcars)

#6.

head(mtcars,1)

#7.

mtcars$mpg

#8.

mtcars$cyl

#9.

mtcars[3,4]

#10.

mtcars[mtcars$cyl>4,]

#11.

mtcars[mtcars$cyl>4 & mtcars$gear>4,]

#12.

mtcars[mtcars$cyl>4 & mtcars$gear==4,]

#13.

mtcars[mtcars$cyl>4 | mtcars$gear==4,]

#14.

mtcars[mtcars$cyl>4 & mtcars$gear!=4,]

#15.

nrow(mtcars)

#16.

length(mtcars)

#17.

dim(mtcars)

#18.

str(mtcars)

#19.

mean(mtcars$hp, na.rm=TRUE)
median(mtcars$hp, na.rm=TRUE)
quantile(mtcars$hp, na.rm=TRUE)
min(mtcars$hp, na.rm=TRUE)
max(mtcars$hp, na.rm=TRUE)
var(mtcars$hp, na.rm=TRUE)
sd(mtcars$hp, na.rm=TRUE)

#20.

summary(mtcars$hp)

# install.packages("RColorBrewer")

library(RColorBrewer)

brewer.pal(n = 8, name = "Set2")

palette(brewer.pal(n = 8, name = "Set2"))


# plot(mtcars$disp, mtcars$mpg,
#     main='Anthony Patregnani: Displacement vs MPG',
#     xlab='Displacement',
#     ylab='MPG',
#     pch='*',
#     cex=1.5,
#     col="5")

library(ggplot2)
qplot(disp, mpg, data=mtcars,
      main='Anthony Patregnani: Displacement vs MPG',
      xlab='Displacement',
      ylab='MPG',
      col=cyl)


plot(mtcars$wt, mtcars$mpg,pch=21,
    main="Anthony Patregnani: Weight vs MPG",
    xlab="Weight in thousands",
    ylab="MPG",
    col="2")

save.image()


dev.off()