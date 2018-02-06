# MYSQL UBUNTU中的安装配置


>## 下载与安装

```
  #安装命令
  sudo apt-get install mysql-server
```

>## 开启远程访问

1. 修改数据库中user的host
```
  # 使用mysql -u root -p登录到数据库，然后依次执行下面语句
  # xxxxxx表示root用户的密码
  use mysql;
  update user set host = '%' where user ='root';
  grant all privileges on *.* to 'root'@'%' identified by 'xxxxxx';
  flush privileges; 
```

2. 修改my.conf的中的ip绑定
```
  # 进入编辑/etc/mysql/mysql.conf.d/mysqld.conf
  vi /etc/mysql/mysql.conf.d/mysqld.conf
  # 修改ip绑定
  # 源文件中为：
  bind-address 127.0.0.1
  # 将其修改为：
  bind-address 0.0.0.0
  # 覆盖保存
  esc:wq 
```
3. 重启mysql 服务
```
  sudo /etc/init.d/mysql restart
  或者
  service mysql restart
```

>## 测试访问
1. 检查3306端口是否开启
```
  netstat -an | grep 3306
  #正常的
  tcp6       0      0 :::3306                 :::*                    LISTEN 
```
2. 判断远程连接是否成功
```
  #从另外的机器访问3306端口
  telnet remote_server_ip 3306
  #remote_server_ip指你的安装mysql的主机地址
  如果连接不成功，则去服务器检查防火墙、安全策略，比如阿里云服务器看看安全组策略是否开启3306端口
```