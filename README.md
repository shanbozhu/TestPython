### 1. 安装python

`brew install python`

`python --version`

安装`python`时会自动安装`pip`

### 2. 执行项目

将项目`压缩包`复制到其他电脑，下面两种方式均可`解压`后在虚拟环境中执行。

虚拟环境：包含当前操作系统安装的`Python解释器副本`和项目依赖的`三方模块`

> 方式一：通过命令行

1. 创建新的虚拟环境
`python -m venv .venv`

2. 激活新的虚拟环境
   1. Windows执行：`.venv\Scripts\activate`
   2. macOS/Linux执行：`source .venv/bin/activate`

3. 安装模块到新的虚拟环境
`pip install -r requirements.txt`

4. 执行项目的Python脚本。

5. 取消激活新的虚拟环境
`deactivate`

> 方式二：通过IDE

1. 使用`IDEA`等软件打开项目目录。
`注意：若打开项目目录后，只显示文件不显示目录，左侧栏颜色为黄色，则需要先删除项目目录下的.idea目录，然后重新打开项目目录`

2. 依次点击：
	1. 文件-》项目结构...-》平台设置-》SDK-》清理无效的（变红色的）SDK。
	2. 项目设置-》项目-》SDK-》从磁盘添加 Python SDK-》Virtualenv环境-》设置虚拟环境。
	`此处也可以先用命令行方式创建新的虚拟环境，然后IDE添加这个环境。`

3. 点击`IDEA`等软件自带的终端，执行`pip install -r requirements.txt`将模块安装到新的虚拟环境。

4. 执行项目的Python脚本。

参考文档：https://zhuanlan.zhihu.com/p/700249286

### 3. 安装模块

推荐在`虚拟环境`中安装模块

`pip install urllib3 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

`pip install 'urllib3<2.0'`

`pip install urllib3==1.26.19`

`pip install -r requirements.txt`

### 4. 卸载模块

推荐在`虚拟环境`中卸载模块

`pip uninstall urllib3`

### 5. 导出模块

必须在`虚拟环境`中导出模块

`pip freeze > requirements.txt`

### 6. 打包项目

1. 使用`pip freeze > requirements.txt`导出当前项目的所有模块。

2. `压缩`当前项目，注意不要包含`.venv`虚拟环境目录。
