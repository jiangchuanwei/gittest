#!/usr/bin/python
#-*-coding:utf-8-*-

# flask web框架

# web框架有  ：Django flask bottle tormdon

# web页面一般分两种
# 1.静态的 页面不会发生变动的
# 2.动态的 页面数据实时刷新的

# flask  python 开发web网页，数据交互的一个框架


from   flask  import  Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello flask'

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5000)