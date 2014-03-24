Title: Vim中构造递增序列
Slug: make-an-increasing-list-in-vim
Date: 2012-05-28 18:58:17
Category: Tips
Tags: vim

近日写爬虫遇到了个有趣的小需求：在构造初始URL列表的时候发现URL序列中的某个子串是个递增序列。上千行的数据自然不能手动一一键入，做为vim党首先要思考有没有什么简便的解决途径。

## 递增与递减

vim中有这样一对Key-map:`<C-a>`和`<C-x>`：`<C-a>`用于将下一个数字递增1，`<C-x>`用于将下一个数字递减1。

与大多数的vim命令一样，键入数字后再接命令则表示重复执行多次该命令。比如`5<C-a>`将下一个数字递增5。

## 宏

vim的宏机制便于我们即时地创造、组合复杂的命令。

    :::shell
    qa
    % do something... %
    q

`q`用于开始或结束一段宏的录制，`a`代表触发这段宏的名字。

录制好后，按`@a`就开始执行`do something`的部分。

## 构造列表

例如有如下列表需要构造：

    :::shell
    http://www.a.com/blog.php?page=1
    http://www.a.com/blog.php?page=2
    http://www.a.com/blog.php?page=3
    ...

可以输入第一行后录制一段宏：

    :::shell
    qa
    Y
    p
    <C-a>
    q

在这之后只要`1000@a`就可以生成数值递增到1000的列表了。

