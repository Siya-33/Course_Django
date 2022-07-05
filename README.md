# 教务信息管理系统

## 引言

数据库的小作业，可以作为一个很基础的页面修改

随便弄了下，熟悉了django的相关操作

代码在函数方面存在部分冗余，尤其是传参部分，应该有更好的实现，或者封装一下

管理员路由跳转方面尚需修改

本来想连Oracle的，但是版本11g不兼容懒得搞了

## 环境

Mysql 8

django=4.0.4

## 运行

进入`settings.py`，设置数据库名称、用户、密码等，连接数据库

`python manage.py makemigrations`

`	python manage.py migrate`

`	python manage.py runserver`

## 实现功能

基本的登录注册和增删查改

学生选课退课和管理员管理课程

## 预览

![image00](https://img1.imgtp.com/2022/07/05/mAxIjWgY.png)

![image01](https://img1.imgtp.com/2022/07/05/mZfH7pL0.png)

![image02](https://img1.imgtp.com/2022/07/05/ezNKFApe.png)