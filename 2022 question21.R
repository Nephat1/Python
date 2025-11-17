EmployeeNo <- 1:5
Name <-c ('John Peter' ,'Ann Lukas', 'Annette Jones', 'John Ford', 'Mark Robert')
gender <-c ('M', 'F','F', 'M', 'M')
age <-c (42,34,34,35,34)
department <-c ('ICT', 'Sales', 'ICT', 'Sales', 'Accounts')
salary <-c (130000,45000,135000,60000,138000)
  
staff<-data.frame (EmployeeNo,Name,gender,age,department,salary)
print(staff)

print(staff)


str(staff)
summary(staff)

tail(staff,2)
head(staff,3)

EmployeeNo <- 1:5
Name <-c ('John Peter' ,'Ann Lukas', 'Annette Jones', 'John Ford', 'Mark Robert')
gender <-c ('M', 'F','F', 'M', 'M')
age <-c (42,34,34,35,34)
department <-c ('ICT', 'Sales', 'ICT', 'Sales', 'Accounts')
salary <-c (130000,45000,135000,60000,138000)

plot(EmployeeNo, age,
     type = 'o', col='blue',
     xlab ='EmployeeNo', ylab ='age',
     main='Age vs EmployeeNo')
