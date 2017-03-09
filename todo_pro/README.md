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
#### 说明：

1. 给User增加role权限，实现用户信息查看，密码修改
2. 修改*templates*函数，使用jinja生成页面
3. 待续...


## Version 1.4
---
#### 说明：

1. 增加管理权限验证函数，优化管理路由代码
2. 增加主页入口。
3. 增加Microblog功能。
	添加写微博，删除微博，查看其它用户微博的功能。

4. 添加Model.exp函数。返回除参数外的所有用户
5. 添加微博评论功能。
6. 删除评论功能。评论者和博主均有权限删除，当微博删除时，评论一起删除。
7. 代码待优化...

## Version 1.5
---
#### description
* delete idea config
* tobe continued...

## Version 1.6
---
### description
* remove badwhitespace in request.cookie
* add thread in server
* LF and CR tobe complete...


