import pandas as pd
import plotly.express as px
import numpy as np
from scipy import stats
np.random.seed(42)

fruits=['Apples','Banana','Cherries','Dates','Elderberries','Figs','Grapes','Honeydew']
regions=['North','South','East','West']
data={
    'Fruit':np.random.choice(fruits,100),
    'Region':np.random.choice(regions,100),
    'Quantity':np.random.randint(1,50,size=100),
    'Price':np.random.uniform(90.5,255.0,size=100)
}

df=pd.DataFrame(data)
print(df.head())
print(df.describe())
print(df.info())

#boxplot
# fig_fruit = px.box(df, x='Fruit', y='Price', title='Price Distribution by Fruit')
# fig_fruit.show()

# #scatterplot
# fig_scatter = px.scatter(df, x='Quantity', y='Price', color='Region',
#                         title='Quantity vs. Price by Region',
#                         labels={'Quantity': 'Quantity', 'Price': 'Price'},
#                         size='Quantity',
#                         hover_name='Fruit') 

# fig_scatter.show()


#histogram
# fig_histo=px.histogram(df,x='Price',nbins=100,title='Price distribution')
# fig_histo.show()

# #extras, refer the pythodocumetation('You get afte the google search of 'plotly bsic charts')
# #refer plotly charts, with map integration and all for the ai part of SIH, also refer "https://www.data.gov.in/"

scatter_2=px.scatter(df,x='Quantity',y='Price',trendline='ols',title='Scatter plot for quantity and price')
scatter_2.show()
