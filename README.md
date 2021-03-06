本项目为豆瓣电影前250名可视化

实现了柱状图、饼图和词云

<img src='https://github.com/hlf20010508/doubanTop250/raw/master/柱状图.png'/>
<img src='https://github.com/hlf20010508/doubanTop250/raw/master/饼图.png'/>
<img src='https://github.com/hlf20010508/doubanTop250/raw/master/词云.png'/>

本项目有三个子项目

克隆方法
```
git clone --recursive https://github.com/hlf20010508/doubanTop250.git
```

命令请附带--recursive，否则子项目文件夹为空

<br/>

可进入子项目阅读README.md查看详细步骤

<br/>

注意

请务必按照以下步骤运行，否则会出现路径错误

<br/>

进入项目文件夹
```
cd doubanTop250
```

<br/>

进入doubanTop250_scrapy文件夹爬取数据,<a href='https://github.com/hlf20010508/doubanTop250_scrapy/blob/master/README.md'>详细步骤</a>
```
cd doubanTop250_scrapy
scrapy crawl doubanTop250
```
得到top250.txt

<br/>

在mysql服务器中建立一个数据库和一个表，用于接下来的数据导入

<br/>

进入doubanTop250_flask文件夹运行后端,<a href='https://github.com/hlf20010508/doubanTop250_flask/blob/master/README.md'>详细步骤</a>
```
cd ..
cd doubanTop250_flask
python txt_to_xlsx.py
python config.py
python xlsx_to_mysql.py
flask run -h 127.0.0.1 -p 5000
```

<br/>

打开浏览器输入127.0.0.1:5000查看可视化结果

<br/>

doubanTop250_vue用于前端编写，可根据需要在其中更改代码

<a href='https://github.com/hlf20010508/doubanTop250_vue/blob/master/README.md'>详细步骤</a>

doubanTop250_flask中已使用打包好的前端文件
