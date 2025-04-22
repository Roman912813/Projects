
#####Univariate Quantitative Analysis 


#Importing data using read.csv()
widge<-read.csv("/Users/gabealvarez/Downloads/GSSData.csv")

#Attaching the dataframe 
attach(widge)

#Table of Descriptive Statistics for Quantitative Variables 
install.packages("table1")
library(table1)

table1::label(widge$tvhours) <-"TV HOURS"
table1::label(widge$age) <-"AGE"
table1::label(widge$chldidel) <-"CHILDREN"

table1::table1(~ tvhours + age + chldidel, data=widge)
#Graphical Displays of Univariate Quantitative Variables 


#Creating a Histogram of TVHOURS, AGE, CHILDREN 
hist(widge$tvhours, main="Figure 1: Histogram of Hours of TV Watched (n=397)",
     xlab = "Number of Hours Watching TV Per Day" , ylab = "Number of U.S. Citizens")

hist(widge$age, main="Figure 3: Histogram of the Age From The Sample (n=397)",
     xlab = "Age" , ylab = "Number of U.S. Citizens")

hist(widge$chldidel, main="Figure 5: Histogram of the Amount of Childern Per Each Person (n=397)",
     xlab = "Number of Children" , ylab = "Number of U.S. Citizens")


#Creating a Boxplot of TVHOURS, AGE, CHILDREN
boxplot(widge$tvhours, main="Figure 2: Boxplot of Hours of TV Watched (n=397)",
    ylab = "Number of Hours Watching TV Per Day")

boxplot(widge$age, main="Figure 4: Boxplot of Age From Sample Population (n=397)",
        ylab = "Age")

boxplot(widge$chldidel, main="Figure 6: Boxplot of Ideal Amount of Children Per Each Person (n=397)",
        ylab = "Number of Children")

#Working in the Tidy Verse with ggplot2 

install.packages("tidyverse")
library(ggplot2)


#Histogram
tvhours_hist <- ggplot(widge, aes(x=tvhours)) +geom_histogram(binwidth = 0.5)

print(tvhours_hist + labs(title = "Figure 1:Histogram of Hours of TV Watched (n=397)", y="Number of U.S. Citizens", x="Number of Hours Watching TV Per Day"))

age_hist <- ggplot(widge, aes(x=age)) +geom_histogram(color="white", binwidth = 5)

print(age_hist + labs(title = "Figure 3:Histogram of Age From Sample Population(n=397)", y="Number of U.S. Citizens", x="Age"))

chldidel_hist <- ggplot(widge, aes(x=chldidel)) +geom_histogram(color="white", binwidth = 1)

print(chldidel_hist + labs(title = "Figure 5:Histogram of the Amount of Ideal Childern Per Each Person (n=397) ", y="Number of U.S. Citizens", x="Number of Children"))

######Univariate Categorical Analysis 

# Frequency Table 
table1::label(widge$sex) <-"Sex"
table1::label(widge$race) <-"Race"
table1::label(widge$polparty) <-"Political Party"

table1::table1(~sex + race + polparty, data=widge)

#Pie Chart
pie(table(sex), main="Figure 7: Pie Chart of Sex in Sample Population (n=397)")

sex_labels <- round((table(sex))/sum(table(sex))*100,1)
sex_lables <-paste(sex_labels, "%", sep="")
greyscale <- c("grey", "black")
pie(table(sex), main= "Figure 7: Pie Chart of Sex in Sample Population (n=397)", col=greyscale,
    labels=sex_labels)
legend(1, 0.5, c("Female", "Male"), fill=greyscale)
AfrAm="African American"
pie(table(race), main="Figure 7: Pie Chart of Race in Sample Population (n=397)")

race_labels <- round((table(race))/sum(table(race))*100,1)
race_lables <-paste(race_labels, "%", sep="")
greyscale <- c("green", "black", "blue","red" )
pie(table(race), main= "Figure 9: Pie Chart of Race in Sample Population (n=397)", col=greyscale,
    labels=race_labels)
legend(0.5, -0.5, c("African American", "Hispanic", "Other" , "White"), fill=greyscale)

polparty_labels <- round((table(polparty))/sum(table(polparty))*100,1)
polparty_lables <-paste(polparty_labels, "%", sep="")
greyscale <- c("blue", "grey", "green","red" )
pie(table(polparty), main= "Figure 11: Pie Chart of Political Party in Sample Population (n=397)", col=greyscale,
    labels=polparty_labels)
legend(1, 0.5, c("Democrat", "Independant", "Other" , "Republican"), fill=greyscale)

#Bar Chart 
barplot(sort(table(sex) , increasing=TRUE), main="Figure 8: Bar Chart of Sex in Sample Population (n=397)",
        ylab = "Frequency", xlab = "sex", ylim = c(0,250))

barplot(sort(table(race) , increasing=TRUE), main="Figure 10: Bar Chart of Race in Sample Population (n=397)",
        ylab = "Frequency", xlab = "race", ylim = c(0,350))

barplot(sort(table(polparty) , increasing=TRUE), main="Figure 12: Bar Chart of Political Party in Sample Population (n=397)",
        ylab = "Frequency", xlab = "Political Party", ylim = c(0,200))

#####Bivariate Analysis 2 Categorical 
table1::label(widge$sex) <- "Sex"
table1::label(widge$owngun) <- "Own a Gun"
table1::table1(~ owngun | sex, data = widge)

#Grouped Bar Chart 
counts1 <- table(owngun, sex)
barplot(counts1, main= "Figure 13: Side-by-Side Bar Chart of Gun Owners by Sex (n=397)",
        xlab="Sex" , ylab="Frequency", ylim = c(0,175), col=c("red", "blue"),
        legend = rownames(counts1), beside=TRUE)

#Stacked Bar Chart 
counts2 <- table(owngun, sex)
barplot(counts2, main= "Figure 14: Stacked Bar Chart of Gun Owners by Sex (n=397)",
        xlab="Sex", ylab="Frequency" , ylim=c(0,250), col=c("green", "purple"),
        legend = rownames(counts2))

#100% Stacked Bar Chart 
owngun_sex_table <- table(owngun, sex)
percentage <- apply(owngun_sex_table, 2, function(x){x*100/sum(x,na.rm=T)})
barplot(percentage,main= "Figure 15: 100% Stacked Bar Chart of Gun Owners by Sex (n=397)",
        xlab="Sex" , ylab="Percentage" , col=c("red", "yellow"),
        legend = rownames(owngun_sex_table))

#### Bivariate Anaylsis 1 Cat 1 Quant 
table1::label(widge$tvhours) <- "Hours of TV Watched Daily"
table1::label(widge$age) <- "Age"
table1::label(widge$chldidel) <- "Ideal Number of Children"
table1:: table1(~ tvhours + age + chldidel | sex, data=widge)

#Side-by-Side Boxplot of Sex and Hours of TV Watched Daily 
tvhours_sex_box <- ggplot(widge, aes(x=tvhours, color=sex)) + geom_boxplot(outlier.color = "blue",
                                                                           outlier.shape=8, outlier.size= 4)
tvhours_sex_box
print(tvhours_sex_box + labs(title= "Figure 16: Boxplot of Hours of TV Watched Daily by Sex (n=397)", x="Hours of TV Watched Daily"))

####Bivariate Analysis 2 Quant 

#Scatterplot 
plot(age, tvhours, main= "Figure 17: Scatterplot of Age and Hours of TV Watched Daily (n=397)",
     xlab= "Age" , ylab= "Hours of TV Watched Daily", pch=20)
 
abline(lm(age~tvhours), col="red")

#Correlation Coefficient
cor(widge$age, widge$tvhours, use = "complete.obs")

####Confidence Interval 
#Install packages ("Rmisc")
install.packages("Rmisc")
library(Rmisc)

conf_int <- round(CI(widge$age, ci=0.90),2)
conf_int

conf_int <- round(CI(widge$age, ci=0.95),2)
conf_int

conf_int <- round(CI(widge$age, ci=0.99),2)
conf_int


#####Variable Creation
head(widge)
widge$tvconsumption[tvhours < 3] <-"Low"
widge$tvconsumption[tvhours >= 3 & tvhours < 5] <- "Medium"
widge$tvconsumption[tvhours >= 5] <- "High"

#reattach data
attach(widge)
table(tvconsumption)

#Stratified Analysis 
table1::label(widge$age) <- "Age"
table1::label(widge$chldidel) <- "Ideal Number of Children"
table1:: table1(~age + chldidel | tvconsumption, data=widge)

write.csv(GSSData, "/Users/gabealvarez/Downloads/Roman_Alvarez_RProject", row.names=FALSE)



