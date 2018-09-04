#### pandas
##### 读取csv
```python
pd.read_csv('../data/stock_data.csv', encoding='gbk')
#### 常见参数
# encoding 编码 gbk / utf8
# 路径: http/ 本地路径/ftp等
# sep 分隔符 默认逗号
# delimiter 同sep
# header 指定第几行作为头
# names 指定列名 文件中不包含header的行，应该显性表示header=None
# prefix 默认为None，当header为空时，prefix=x 列名为x1 x2 
# dtype 指定数据类型 {‘a’: np.float64, ‘b’: np.int32} 
# skiprows 忽略某几行，从第几行开始
# na_values 默认为None，NAN
# 
```
#### 读取案例
```python
"""cat a.csv
a,b,c,d,message
1,2,3,4,hello"""
pd.read_csv('a.csv')
pd.read_table('a.csv', sep=',')
""" cat b.csv
1,2,3,message
4,5,6,hello
"""
pd.read_csv('a.csv', header=None)
# X.1 X.2 X.3

# 指定column name
names = ['a','b','c','message']
pd.read_csv('b.csv', names = names)
# 指定行名
pd.read_csv('b.csv', names = names, index_col = 'message')
# 空格分割
pd.read_csv('c.csv', sep='\s+')
# 跳过几行
a = pd.read_csv('c.csv', skiprows=[0,2,3])
# 忽略几行（从未尾）
pd.read_csv('c.csv', skip_footer=3)
# 判断是否为NULL
pd.isnull(a)
# 替换缺失值
pd.read_csv('d.csv', na_values=['NULL']
# 读取几行
pd.read_csv('d.csv', nrows=5)
# 按块读取
pd.read_csv('d.csv', chunksize=1000)
```
#### 保存
```python
data = pd.read_csv('c.csv')
data.to_csv('xx.csv')
# 指定分割
data.to_csv('xx.csv', sep='|')
# 打印到屏幕 ,缺失值用NULL
data.to_csv(sys.stdout, sep='|', na_rep='NULL')
# 禁用行、列
data.to_csv('sys.stdout, index=False, header=False)
# 指定列
cols=['a','c','e']
```
#### JSON
```python
# 读取
import json
json.loads(obj)
# 转为json
json.dumps(result)
```
#### 高效存取数据格式 HDF5
```python
pd.HDFStore('xxx.h5)
# key, value ，跟dict很像
```

#### 连接MongoDB
```python
import pymongo
conn = pymongo.Connection('host', port=27017)
```