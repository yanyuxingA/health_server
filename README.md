# health_server

## 后台架构

- 项目后台采用Django Rest framework框架进行开发
- 数据库使用mysql
- 定时业务使用linux自带的crontab， 定时调用/health/users/export/，完成每日发送邮件



