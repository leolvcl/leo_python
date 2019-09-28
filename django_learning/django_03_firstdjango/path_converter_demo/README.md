# 自定义URL（PATH）转换器笔记：

## 需求：
实现一个获取文章列表的demo，用户可以根据`/articles/文章分类/`的方式来获取文章。其中文章分类采用的是`分类1+分类2+分类3...`的方式拼接的，并且如果只有一个分类，那就不需要加号。示例如下：
```
# 1. 第一种：获取python分类下的文章
/articles/python/
# 2. 第二种：获取python和django分类下的文章
/articles/python+django/
# 3. 第三种：获取python和django和flask分类下的文章
/articles/python+django+flask/
以此类推...
```

在“文章分类”参数传到视图函数之前要把这些分类分开来存储到列表中。
比如参数是`python+django`，那么传到视图函数的时候就要变成`['python','django']`。

以后在使用reverse反转的时候，限制传递“文章分类”的参数应该是一个列表，并且要将这个列表变成`python+django`的形式。


## 自定义URL转换器：
之前已经学到过一些django内置的url转换器，包括有int、uuid等。有时候这些内置的url转换器并不能满足我们的需求，因此django给我们提供了一个接口可以让我们自己定义自己的url转换器。

自定义url转换器按照以下五个步骤来走就可以了： 
1. 定义一个类，直接继承自object就可以了。 
2. 在类中定义一个属性regex，这个属性是用来限制url转换器规则的正则表达式。 
3. 实现to_python(self,value)方法，这个方法是将url中的值转换一下，然后传给视图函数的。 
4. 实现to_url(self,value)方法，这个方法是在做url反转的时候，将传进来的参数转换后拼接成一个正确的url。 5. 将定义好的转换器，使用`django.urls.converters.register_converter`方法注册到django中。

示例代码如下：
```python
from django.urls import register_converter

class CategoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self,value):
        # python+django+flask
        # ['python','django','flask']
        result = value.split("+")
        return result

    def to_url(self,value):
        # value：['python','django','flask']
        # python+django+flask
        if isinstance(value,list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("转换url的时候，分类参数必须为列表！")

register_converter(CategoryConverter,'cate')
```
