import pandas as pd
#读取数据
df=pd.read_csv('E:\\01_Python\Lesson01\car_complain.csv')
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))

#数据清洗，将别名合并
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)

#统计每个品牌的问题数量，按照品牌投诉数排序
result=df.groupby(['brand'])['id'].agg(['count'])
tags=df.columns[7:]
result2=df.groupby(['brand'])[tags].agg(['sum'])
result2=result.merge(result2, left_index=True, right_index=True, how='left')
result2.reset_index(inplace=True)
result2=result2.sort_values('count',ascending=False)
result2.to_excel("E:\\01_Python\Lesson01\\result2 brand.xlsx",index=False)
print(result2)

#按照某个问题对品牌进行排序
query=('A12', 'sum')
result3=result2.sort_values(query, ascending=False)
print(result3)

#按照车型投诉数进行排序
result1=df.groupby(['car_model'])['id'].agg(['count'])
result4=df.groupby(['car_model'])[tags].agg(['sum'])
result4=result1.merge(result4, left_index=True, right_index=True, how='left')
result4.reset_index(inplace=True)
result4=result4.sort_values('count',ascending=False)
result4.to_excel("E:\\01_Python\Lesson01\\result4 model.xlsx",index=False)
print(result4)
