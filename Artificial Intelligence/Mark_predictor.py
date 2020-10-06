# This code is an introduction to linear regression.
# I am taking "Mid-Sem Marks"(out of 100) as input data and make a model that predicts the marks of final exam.



import numpy as np
import matplotlib.pyplot as plt

#train_data is given as input to the model and train_output is the currect output that the model should predict.
train_data = np.array([60. , 65. , 70. , 90. , 85. , 50. , 65. , 91. , 78. , 88. , 39. , 87. , 67. , 50. , 99. ])
train_output = np.array([63. , 59. , 75. , 85. , 87. , 50. , 64. , 80. , 79. , 95. , 36. , 81. , 80. , 65. , 97. ])

#Scatter Plot to show the data
plt.xlabel('Mid-sem Marks')
plt.ylabel('Final Exam Marks')
plt.scatter(train_data, train_output)
plt.show()

#The Goal of the linear regression model is to predict a line that should be passing through the data that it can predict the next unknown data input.
#So if we ge the formula for that line( m*x +c ) right we can then successfully predict the output.
#We have to find the currect values of m and c.
m = 0
c = 0
n = len(train_data)
epochs = 1000 #epoch defines the number of iterations the model has to take when training
l_rate = 0.00001 #it defines the rate of learning
for epoch in range(epochs):
    h_theta = m*train_data + c
    der_m = (-2/n)*np.sum(train_data*(train_output - h_theta)) #derivation of mean squared error of predicted output and real output
    der_c = (-2/n)*np.sum(train_output - h_theta)
    m = m - (l_rate * der_m)
    c = c - (l_rate * der_c)

print(m, c)

h_theta = m*train_data + c 

#It shows the line that is generated after the model is trained
plt.scatter(train_data, train_output)
plt.plot([min(train_data), max(train_data)],  [min(h_theta), max(h_theta)], color='red')
plt.show()

#Now we will test the model by giving unknown inputs!!!
x = int(input("Enter your mid-sem marks: "))
if(x <= 100):
    h_theta = m*x + c
    print("Your marks in finals will be near to", h_theta)
else:
    print("Wrong Input!!!")