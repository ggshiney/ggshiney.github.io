Title: Unix Tool: time
Slug: unix-tool-time
Date: 2012-09-02 19:35:39
Category: shell
Tags: shell

## 统计程序执行时间：time

近来做了些性能测试的工作，基本指标便是某一操作的执行时间。

Unix提供了一个简单获取程序执行时间的小工具`time`。

基本使用方法：

    time <command> [arguments]

简单地说，就是在需要获取时间的程序命令前面加上`time`。统计输出三个执行时间，精确到ms。


不妨看看`sleep`1秒的各项执行统计时间：

    :::shell
    $time sleep 1

    real    0m1.024s
    user    0m0.001s

* real为程序开始执行到执行结束总耗时；
* user为程序在操作系统用户态的cpu执行时间；
* sys为程序在操作系统内核态的cpu执行时间；

由于程序在执行时除了cpu处理指令外往往会产生io或其他开销，这部分耗时都计算在real中，因此user与sys之和往往小于real。

## 两个time命令

实际上在Unix中不仅仅只有一个`time`，可以通过`type`查看到所有`time`命令的类型：

    :::shell
    $type -a time
    time is a shell keyword
    time is /usr/bin/time

可见`time`既是shell的一个shell关键字，同时也是一个外部命令。外部命令`/usr/bin/time`更强大，还可以输出io等统计信息、指定时间输出的格式。

## time输出重定向

time统计信息默认输出到标准错误输出`stderr`，而不是标准输出`stdout`。

外部命令`/usr/bin/time`可以

    :::shell
    $time echo 'hello world' 2> 1
    hello world

    real    0m0.000s
    user    0m0.000s
    sys     0m0.000s

上述两个`time`的输出处理有些区别，这是由于shell在处理

