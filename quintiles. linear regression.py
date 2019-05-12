import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams['figure.figsize']=(10.0,8.0)

a=pd.read_excel(open("quintiles.xlsx",'rb'))
print(a)

X=a.iloc[:,3].values
Y=a.iloc[:,7].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

print(mean_x)
print(mean_y)
m=len(X)
numer=0
denom=0

for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1= numer/denom
b0= mean_y - (b1 * mean_x)
#coefficients b1= m (slope) and b0 = c (intercept)
print(b1,b0)

#plotting
max_x= np.max(X)+80 
min_x= np.min(X) -80
 
x1= np.linspace(min_x,max_x,74)
y1= b0+b1*x1

plt.plot(x1,y1,color='red',label='regression line')
plt.scatter(X,Y,c='#ef5423',label='scatter plot')
            
plt.xlabel('Age')
plt.ylabel('Weight')
plt.legend()
plt.show()
         
ss_t=0
ss_r=0
for i in range(m):
    y_pred=b0+b1 *X[i]
    ss_t +=(Y[i] - mean_y) ** 2
    ss_r +=(Y[i]- y_pred) ** 2
    r2 = 1-(ss_r/ss_t)
    print(r2)
    

 






