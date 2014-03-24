Title: Arch Linux添加网络打印机
Slug: add-network-printer-for-archlinux
Date: 2012-11-28 20:19:17
Category: Walkthrough
Tags: ArchLinux

终于，实验室买了台高级打印机，可以配置独立的IP地址，支持网络打印。
索性给我这台Arch Linux也配置上网络打印功能。

## UNIX/Linux下的打印管理工具`CUPS`

[CUPS](http://www.cups.org)(Common UNIX Printing System)，是Apple开发的一套UNIX开源打印系统。
Arch下可可以通过`CUPS`进行打印管理。

安装`CUPS`很简单：

    pacman -S cups libcups

`CPUS`安装好后，需要根据打印机安装相应的driver。
我们的HP打印机对应的驱动包`hplip`，所有的HP打印机都可以使用：

    pacman -S hplip

之后启动`CUPS`守护进程，并把`CUPS`加入启动服务。

    systemctl start cups
    systemctl enable cups

`CUPS`的基本管理功能通过本地web页面进行操作，需要前用户在`sys`组，在这里临时把当前用户加入`sys`：

    usermod -aG sys [USERNAME]

打开浏览器[http://localhost:631](http://localhost:631)，就可以看到`CUPS`的配置页面了。

UI做的比较简洁，直接到`Administration`页面`Add Printer`即可。
配置好后打印时就能看到刚刚添加的打印机了。

## 参考

[https://wiki.archlinux.org/index.php/Cups](https://wiki.archlinux.org/index.php/Cups)
