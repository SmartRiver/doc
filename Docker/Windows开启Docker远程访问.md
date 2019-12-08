# Windows开启Docker远程访问

Docker是用于创建容器化应用程序的完整开发平台。 Docker Desktop是在Windows上开始使用Docker的最佳方法。Windows版Docker桌面部分包含有关Docker桌面社区稳定版的信息。

## 下载&安装

* 官网下载地址 [Docker Desktop for Windows](https://download.docker.com/win/stable/Docker%20Desktop%20Installer.exe)

## 开启docker的远程连接

```html
By default, it will listen on unix:///var/run/docker.sock to allow only local connections by the root user. You could set it to 0.0.0.0:2375 or a specific host IP to give access to everybody, but that is not recommended because then it is trivial for someone to gain root access to the host where the daemon is running.

Similarly, the Docker client can use -H to connect to a custom port. The Docker client will default to connecting to unix:///var/run/docker.sock on Linux, and tcp://127.0.0.1:2376 on Windows.
```

docker默认的连接方式都是***sock***连接, 如果需要开启远程连接， 则需要指定 ***0.0.0.0:2375***

* Docker Desktop for Windows的开启方式如下：

  开启docker客户端，右击任务栏的图标：

  ![Enable_remote_access_to_Docker_for_Windows_10-01](https://pronto-core-cdn.prontomarketing.com/354/wp-content/uploads/sites/2/2018/11/Enable_remote_access_to_Docker_for_Windows_10-01.png)

  ![Enable_remote_access_to_Docker_for_Windows_10-02](https://pronto-core-cdn.prontomarketing.com/354/wp-content/uploads/sites/2/2018/11/Enable_remote_access_to_Docker_for_Windows_10-02.png)

  * 你可能看到General设置最后一项Expose daemon on tcp://localhost:2375 without TLS, 别傻了，我试了，这个不一定生效。

  ![Enable_remote_access_to_Docker_for_Windows_10-03](https://pronto-core-cdn.prontomarketing.com/354/wp-content/uploads/sites/2/2018/11/Enable_remote_access_to_Docker_for_Windows_10-06.png)

  * 正确的方法是取消Expose daemon ..., 打开设置左侧Daemon,  切换右侧按钮从Basic 到Advanced, 编辑下面文本域，***增加一条："hosts": [tcp://0.0.0.0:2375]***，如下图：
  
  ![Enable_remote_access_to_Docker_for_Windows_10-04](https://pronto-core-cdn.prontomarketing.com/354/wp-content/uploads/sites/2/2018/11/Enable_remote_access_to_Docker_for_Windows_10-07.png)
  
  到这步docker的远程连接已经开启了，但是还缺最后一步，要给防火墙添加规则，开放2375端口。
  
## 配置防火墙打开2375端口

* 为了确保能远程连接上docker deamon, 你需要执行以下命令

```html
    netsh advfirewall firewall add rule name="docker_daemon" dir=in action=allow protocol=TCP localport=2375
```

## 测试是否成功

* 通过你本机ip 和 2375端口访问测试是否成功。

![Enable_remote_access_to_Docker_for_Windows_10-05](https://pronto-core-cdn.prontomarketing.com/354/wp-content/uploads/sites/2/2018/11/Enable_remote_access_to_Docker_for_Windows_10-08.png)

> 参考文章

[https://www.portainer.io/2018/03/enable-remote-access-docker-windows-10/](https://www.portainer.io/2018/03/enable-remote-access-docker-windows-10/)

[https://docs.docker.com/docker-for-windows/](https://docs.docker.com/docker-for-windows/)

------

希望文中方法对你有用，如果有用，请动动小手点个赞👍！

祝生活愉快！
