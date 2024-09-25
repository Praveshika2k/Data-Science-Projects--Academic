import pandas as pd
df=pd.DataFrame({'name':["n1",'n2','n3','n4','n5'],'age':['a1','a2','a3','a4','a5'],'gender':['female','male','male','female','male'],'mark':['m1','m2','m3','m4','m5'],'score':[90,76,86,79,78]})
students=pd.DataFrame({'name':['emma'],'age':[18],'gender':['female'],'mark':[12],'score':[87]})
df1 = pd.concat([df, students])
df2=df1.assign(lettergrade=['A','B','C','A','B','A'])
print(df2)
scr=df2[df2['score']>80]
print(scr)
gen=df2[(df2['gender']=='female') & (df2['score']>80)]
print(gen)
