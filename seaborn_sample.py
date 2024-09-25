import seaborn as sbs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mtcars=pd.read_csv('mtcars.csv')
print(mtcars.head())
print(mtcars.info())
print(mtcars.shape)
# res=sbs.barplot(x='cyl',y='carb',data=mtcars,color="yellow")
# res=sbs.barplot(x='cyl',y='carb',data=mtcars,palette="rocket")
# res=sbs.countplot(x='cyl',data=mtcars,palette="Set1")
# res=sbs.countplot(x='carb',data=mtcars,palette='rocket')
# res=sbs.countplot(y='gear',data=mtcars,palette='rocket')
# res=sbs.countplot(x='gear',hue='cyl',data=mtcars,palette='Set1')
res=sbs.histplot(mtcars.mpg,bins=10,color='g',kde=True)

#also finding left skew, right skew and kurtosis

#copy from chatgpt

plt.show()