# 视图函数：
1. 视图函数的第一个参数必须是request。这个参数绝对不能少。
2. 视图函数的返回值必须是`django.http.response.HttpResponseBase`的子类的对象。