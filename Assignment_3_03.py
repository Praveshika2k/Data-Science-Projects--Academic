import pandas as pd
df=pd.read_csv('ToothGrowth.csv')
print(df)
print("Mean of the tooth length:",df['len'].mean())
print("Median of the tooth length:",df['len'].median())
print("Standard deviation of tooth length:",df['len'].std())
print("Quartile of tooth length:",df['len'].quantile())
vc=df[df['supp']=='VC']
vcm=vc['len'].mean()
print(vcm)
oj=df[df['supp']=='OJ']
ojm=oj['len'].mean()
print(ojm)
difference=vcm-ojm
print("Tooth length difference is",abs(difference))
if ojm>vcm:
    print("Orange juice results in higher average tooth length")
elif vcm>ojm:
    print("Vitamins result in higher average tooth length")
else:
    print("Both results in same tooth length")
