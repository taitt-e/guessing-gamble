library(readxl)
library(ggplot2)

DPD_data= data.frame(read_excel('C:/Users/t_z11/Downloads/Dynamic_Programming_Data.xlsx'))
a <- DPD_data[, 3]
b <- DPD_data[, 2]

boxplot(b~a, data=DPD_data, xlab = "Range N", ylab = "Runtime (μs)", main = "How range N affects runtime.")
ggplot(DPD_data, aes(x=N, y=Runtime..Microseconds.))+geom_point()+geom_smooth(method="lm")

b <- DPD_data[, 1]

boxplot(b~a, data=DPD_data, xlab = "Range N", ylab = "Number of Guesses", main = "How range N affects Guess Count.")
ggplot(DPD_data, aes(x=N, y=Number.of.Guesses))+geom_point()+geom_smooth(method="lm")

