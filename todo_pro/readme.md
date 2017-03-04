### 未做安全测试：

* 爬虫
* 不合法输入


## Version 1.1
----

> 版本改动说明：

1. 将请求form中得到的id，uid默认值改为-1，同时处理save函数相关语句
2. 重定向*redirect* 302 Cache-Control
3. 给*redirect*和*header_with_headers*的headers参数设置None默认值，不能设为空字典
4. 给ToDo增加创建时间和更新时间,*add*和*update*函数
5. 待续... 

## Version 1.2
---
#### 说明：

1. 改善登录页面，成功后重定向到主页。
2. 改善注册页面。
3. 改写*current_user*返回User对象
4. 增加登录验证函数，优化路由函数代码
5. 待续...


## Version 1.3
---
### 说明：

1. 给User增加role权限，实现用户信息查看，密码修改
2. 修改*templates*函数，使用jinja生成页面
3. 待续...
