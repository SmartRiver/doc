# MYSQL Ubuntu中的安装配置

## 下载与安装

```html
  #安装命令
  sudo apt-get install mysql-server
```

## 开启远程访问

1.修改数据库中user的host

```html
  # 使用mysql -u root -p登录到数据库，然后依次执行下面语句
  # xxxxxx表示root用户的密码
  use mysql;
  update user set host = '%' where user ='root';
  grant all privileges on *.* to 'root'@'%' identified by 'xxxxxx';
  flush privileges;
```

2.修改my.conf的中的ip绑定

```html
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

3.重启mysql 服务

```html
  sudo /etc/init.d/mysql restart
  或者
  service mysql restart
```

## 测试访问

1.检查3306端口是否开启

```html
  netstat -an | grep 3306
  #正常的
  tcp6       0      0 :::3306                 :::*                    LISTEN
```

2.判断远程连接是否成功

```html
  #从另外的机器访问3306端口
  telnet remote_server_ip 3306
  #remote_server_ip指你的安装mysql的主机地址
  如果连接不成功，则去服务器检查防火墙、安全策略，比如阿里云服务器看看安全组策略是否开启3306端口
```

## 常见问题

1、找不到mysqld.sock

```html

Q: Can't connect to lcoal MYSQL server though sock '/var/run/mysqld/mysqld.sock
R: MySQL下mysql.sock丢失丢失的原因一般是因为配置文件不一致的原因，mysqld 错误启动，mysqld_safe会清除一次mysql.sock 。
A:
  1、如果是.sock文件存在但是指向不对，在root权限下修改my.cnf文件（/etc/mysql/my.cnf），指定正确的路径；
  2、如果是.scok文件不存在
    判断一般人解决故障时没有切换到mysql用户，造成权限有问题，无法创建mysql授权表，所以也就无法创建/tmp/mysql.sock 和hostname.pid文件。因此，总结解决方法如下：
    //root 用户也是可以的
    #su mysql
    //到bin目录执行，重建授权表
    $/usr/local/bin/mysql_install_db
    $/usr/local/bin/mysqld_safe &
    //测试
    mysql -uroot -p
    mysq>bye;

    文件已经解决，重新生成新的 /tmp/mysql.sock 和 hostname.pid

```

### 参考资料

[unbuntu mysql安装](http://blog.csdn.net/wuzuodingfeng/article/details/54638999)
