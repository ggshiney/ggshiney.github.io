Title: Tar in Mac OS X
Slug: tar-in-mac-os-x
Date: 2012-10-31 20:21:59
Category: Tips
Tags: Mac OS

近来在做[OpenHatch](http://openhatch.org/)，新手任务里面提到了tar命令在Mac OS X下的一个小tip。

通常在Mac OS X下会产程很多以`._`开始的隐藏文件，在打tar包的时候往往也会包含进去。如果要把这些隐藏文件排除在外则，可以增加一个环境变量`COPYFILE_DISABLE=true`。
