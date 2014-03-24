Title: Ubuntu配置PPTP VPN
Slug: pptp-vpn-on-ubuntu
Date: 2013-05-13 18:20:12
Category: Walkthrough
Tags: Ubuntu

接手一台新服务器，简单记录一下pptp vpn加ufw防火墙在ubuntu上的设置。
这样学校范围内就能实现手机通过vpn免费上网了。
同样，在校外也可以通过vpn访问校园网资源。

## 配置PPTP

安装pptpd软件包：

    apt-get install pptpd

编辑`/etc/pptpd.conf`配置文件：
修改其中的localip为pptp服务端的vpn网关ip，remoteip为pptp客户端分配的ip地址范围。

    localip 192.168.100.1
    remoteip 192.168.100.101-110

编辑`/etc/ppp/pptpd-options`：
修改ms-dns字段，当使用windows pptp客户端时获取的DNS。
其实我只为了服务一台iphone，这里并不需要设置。

    ms-dns 114.114.114.114

编辑`/etc/ppp/chap-secrets`：
对应的四个字段为客户端连接时使用的用户名、服务、密码、ip。
服务名对应`pptpd-options`中的对应字段值，如默认则为`pptpd`。
ip地址设置`*`为允许任意来源。

    [USERNAME]    pptpd    [PASSWORD]    *

编辑`/etc/sysctl.conf`：开启路由转发。

    net.ipv4.ip_forward=1

通过如下命令使之生效：

    sysctl -p

重启`pptpd`服务：

    service pptpd restart

如果不配置ufw防火墙的话，至此即可实现vpn认证连接。
如需要实现vpn上网，仍需要设置iptables：(如后面配置ufw则不用这一步)
其中`-s`指定的来源地址对应`/etc/pptpd.conf`中的ip网段。

    iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o eth0 -j MASQUERADE

## 配置ufw

如果系统启用了ufw防火墙，还需进一步配置。

编辑`/etc/netword/interfaces`：
设置eth0的ip别名：
address对应`/etc/pptpd.conf`中的设置。

    auto eth0:0
    iface eth0:0 inet static
    address 192.168.100.1
    netmask 255.255.255.0

编辑`/etc/default/ufw`：
修改`DEFAULT_FORWARD_POLICY`字段为`ACCEPT`。

    DEFAULT_FORWARD_POLICY=“ACCEPT”

编辑`/etc/ufw/before.rules`：
加入如下内容至`*filter`规则前，通过iptables实现转发。

    *nat
    :POSTROUTING ACCEPT [0:0]
    -A POSTROUTING -s 192.168.2.0/24 -o eth0 -j MASQUERADE

    COMMIT

ufw中加入允许pptp默认的1723端口：

    ufw allow 1723

最后重启服务：

    service networking restart
    service ufw restart
    service pptpd restart

至此pptp vpn的服务器端配置完毕。

## 参考

[http://silverlinux.blogspot.com/2012/05/how-to-pptp-vpn-on-ubuntu-1204-pptpd.html](http://silverlinux.blogspot.com/2012/05/how-to-pptp-vpn-on-ubuntu-1204-pptpd.html)
