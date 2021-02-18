import pandas as pd
import numpy as np
from prettytable import PrettyTable
data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print('--------------统计各科成绩---------------')
x=PrettyTable(["科目","最低分","最高分","平均分","方差","标准差"])
x.add_row(['语文',np.min(df1['语文']),'%.2f'%np.max(df1['语文']),'%.2f'%np.mean(df1['语文']),'%.2f'%np.var(df1['语文']),'%.2f'%np.std(df1['语文'])])
x.add_row(['数学',np.min(df1['数学']),'%.2f'%np.max(df1['数学']),'%.2f'%np.mean(df1['数学']),'%.2f'%np.var(df1['数学']),'%.2f'%np.std(df1['数学'])])
x.add_row(['英语',np.min(df1['英语']),'%.2f'%np.max(df1['英语']),'%.2f'%np.mean(df1['英语']),'%.2f'%np.var(df1['英语']),'%.2f'%np.std(df1['英语'])])
print(x)

print('--------------总分排名-----------------')

df1['总分']=df1.apply(lambda x:x.sum(),axis=1)
df1["名次"] = df1['总分'].rank(ascending=False,method='min')
df1.sort_values('总分',ascending=False,inplace=True)
print(df1)


