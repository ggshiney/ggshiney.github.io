Title: Arch Linux配置双屏
Slug: config-dual-monitor-for-archlinux
Date: 2012-11-14 20:27:19
Category: Walkthrough
Tags: ArchLinux

## 前言

实验室设备更新，捡来块有VGA+DVI双接口的Nvdia显卡。自己的老机器用的是集成显卡，便打算给自己的机器升级配置双显示屏。


## 配置双屏显示

### 安装新显卡

现在的显卡都是PCI-E接口的了。尽管PCI-E接口的显卡设备即插即用，但是仍需要在BIOS配置一下主显示设备。

顺道科普了一下BIOS中有关显卡的选项：

* IGD(Integrated Graphic Device): 集成显卡
* PCI(Peripheral Component Interconnect): PCI显卡
* PEG(PCI Express Graphics): PCI-E显卡

那就选择以PEG为主显示设备。

### 驱动

我的ArchLinux已经配置了xfce桌面环境，先装个NVIDIA驱动。

ArchLinux中列出所有的PCI设备：

    lspci

看到硕大的NVIDIA，确认是Nvdia的显卡，接着找找驱动。ArchLinux中的显卡驱动都是以`xf86-video`开头的。

    pacman -Ss xf86-video

发现`xf86-video-nouveau`是N卡的驱动，安装之。

    pacman -S xf86-video-nouveau

### 配置双屏显示

一切就绪后两个显示器显示相同，如果需要扩展显示桌面，还需要进行一番配置。

`randr`(X Resize, Rotate and Reflect Extension)可以控制桌面的显示输出效果，如镜像、旋转等。`xrandr`是`randr`的命令行接口。

首先查看当前显示状态，列出X显示设备：

    xrandr -q

输出如下

    Screen 0: minimum 320 x 200, current 2880 x 900, maximum 8192 x 8192
    VGA-1 connected 1440x900+1440+0 (normal left inverted right x axis y axis) 408mm x 255mm
       1440x900       59.9*+   75.0  
       1280x1024      75.0     70.0     60.0  
       1280x960       60.0  
       1366x768       60.0  
       1360x768       60.0  
       1280x800       74.9     59.8  
       1152x864       75.0  
       1280x768       74.9     59.9  
       1024x768       75.1     70.1     60.0  
       1024x576       60.0  
       832x624        74.6  
       800x600        72.2     75.0     60.3     56.2  
       848x480        60.0  
       640x480        72.8     75.0     66.7     60.0  
       720x400        70.1  
    DVI-I-1 connected 1440x900+0+0 (normal left inverted right x axis y axis) 408mm x 255mm
       1440x900       59.9*+   75.0  
       1280x1024      75.0     70.0     60.0  
       1280x960       60.0  
       1366x768       60.0  
       1360x768       60.0  
       1280x800       74.9     59.8  
       1152x864       75.0  
       1280x768       74.9     59.9  
       1024x768       75.1     70.1     60.0  
       1024x576       60.0  
       832x624        74.6  
       800x600        72.2     75.0     60.3     56.2  
       848x480        60.0  
       640x480        72.8     75.0     66.7     60.0  
       720x400        70.1  


看到我的两个显示器对应着`VGA-1`和`DVI-I-1`，接下来设置两个显示器位置

    xrandr --output DVI-I-1 --auto --output VGA-1 --auto --right-of DVI-I-1

### 自动启动

~~可以把这条命令通过 `Settings Manager` => `Sessioin and Startup` =>  `Application Autostart` 加入到xfce的自动启动列表中。~~

上面加入xfce自动启动列表后在系统重启后出现花屏。

可以把预览好位置的配置加入配置文件`/etc/X11/xorg.conf`，以实现自动启动。

    Section "Monitor"
        Identifier  "VGA-1"
        Option      "Primary" "true"
    EndSection

    Section "Monitor"
        Identifier  "DVI-I-1"
        Option      "RightOf" "VGA-1"
    EndSection

## 参考

[https://wiki.archlinux.org/index.php/DualScreen](https://wiki.archlinux.org/index.php/DualScreen)

[http://ianmarmour.com/2012/01/22/setting-up-dual-monitors-on-xfce-arch-linux/](http://ianmarmour.com/2012/01/22/setting-up-dual-monitors-on-xfce-arch-linux/)


