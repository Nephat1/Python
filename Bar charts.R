#create the data for the chart
H<- c(7,12,28,3,41)
#plot the bar chart
barplot(H)

#create the data for the chart
H<- c(7,12,28,3,41)
M<-c('Mar','Apr','May','Jun','Jul')

#plot the bar chart
barplot(H,names.arg=M,xlab='Month',ylab='Revenue',col='blue',
        main='Revenue chart',boarder='red')

#create the input vector
colors =c('green','orange','brown')
months<-c('Mar','Apr','May','Jun','Jul')
regions <-c('East','West','North')
data<- expand.grid(Month=months,Region=region,Color=colors)
print(data)
#create the matrix of the values
Values <-matrix(c(2,9,3,11,9,4,8,7,3,12,5,2,8,10,11), nrow = 3,ncol=5,byrow=TRUE)
#create a bar chart
barplot(Values,main='total revenue',names.arg=months,xlab='months',ylab='revenue',col=colors)
#add the legend to the chart
legend(x = 'topright',inset =c(0.35,0),legend = regions,title ='Region',cex=1,fill=colors,bty='n')


# Create vectors
Patientnumber <- c("P001345", "P001563", "P001450", "P001546")
weight <- c(80, 67, 85, 70, 73)
Patientfees <- c(45, 50, 45, 56, 43)

# Combine into a data frame
patientdata <- data.frame(Patientnumber, weight, Patientfees)
print(patientdata)

# Plot weight vs patient fees
barplot(weight,
        names.arg = Patientfees,
        main = "Patient Fees vs Weight",
        xlab = "Patient fees",
        ylab = "Weight (kg)",
        col = "blue",
        border = "red")


