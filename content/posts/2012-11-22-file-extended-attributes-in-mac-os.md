Title: Mac OS下的文件扩展属性
Slug: file-extended-attributes-in-mac-os
Date: 2012-11-22 20:36:52
Category: Tips
Tags: Mac OS

## 恼人的`@`

在mac下`ls -l`，常常看到9位文件权限后面跟着一个`@`符号，这货是干啥的？

原来，这就是mac文件系统的扩展属性。通过一些mac下的软件、工具操作文件后往往会给文件附加上扩展属性，而只通过`Terminal`进行的一般文件操作则不会附加上这些属性。

但是扩展属性可能导致一些常见的操作在其他文件系统下产生多余文件，比如`tar`。


## 解决之道

既然是扩展属性，总是有方法去掉的。

mac提供了`xattr`进行扩展属性操作。可以先通过`ls -l@`，增加一个`@`参数查看文件有那些扩展属性。

    ls -l@ filename.test

    -rw-r--r--@  1 user  staff    512  1 1 20:20 filename.test
        com.apple.TextEncoding      15

之后可以用`xattr`删除之：

    xattr -d com.apple.TextEncoding filename.test
