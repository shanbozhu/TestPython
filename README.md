### 1. 安装python

`brew install python`

`python --version`

安装`python`时会自动安装`pip`

- `Python`语言是开源的。`Python`的开源本质是它的实现（`解释器`、`标准库`）以及整个生态系统的开源，而不仅仅是语法规则。

- `标准库`是指由编程语言官方或语言规范定义并提供的一组基础功能库。这些库通常与语言一起分发，不需要额外安装即可使用。标准库旨在提供常见任务的基础支持，使开发者在编程时不必重复造轮子，从而提高效率和代码质量。

- `标准库`是编程语言中不可或缺的一部分，提供了实现常见功能所需的工具集。它包含从基本的数据结构和数学函数到复杂的网络通信和系统交互等内容。标准库的设计直接影响了语言的易用性、性能以及开发效率，是编程语言生态的重要基石。

- `标准库`的标准由编程语言的官方组织、标准化委员会或语言的主要开发者制定。这些组织和开发者根据语言的设计目标、使用场景和用户需求来定义标准库的内容和规范。

- 高级语言（例如`Python`）提供的`标准库`在底层通常会调用`C`语言编写的函数或库。这是因为`C`语言能够直接与操作系统、硬件和系统资源交互，并且具有高效、底层的特性，使其非常适合实现这些底层功能。

- 这种设计结合了`C`的高性能和`Python`的高可读性，既提升了执行效率，又保持了开发的便利性。

### 2. 执行项目

将项目`压缩包`复制到电脑，下面三种方式均可`解压`后在虚拟环境中执行。

虚拟环境：含有`Python解释器`和`依赖模块`。

> 方式一：通过`命令行`

一、通过Python自带的**Virtualenv**创建虚拟环境。

1. 进入项目根目录执行：`python -m venv .venv`

2. 激活虚拟环境
	1. Windows执行：`.venv\Scripts\activate`
	2. macOS/Linux执行：`source .venv/bin/activate`

3. 安装模块到虚拟环境：`pip install urllib3`

4. 执行项目的Python脚本。

5. 取消激活虚拟环境：`deactivate`

二、通过**conda**创建虚拟环境

1. 进入项目根目录执行：
	1. 指定路径下创建：`conda create --prefix myenv python=3.10`
	2. 默认路径下创建：`conda create --name myenv python=3.10`

2. 激活虚拟环境：`conda activate myenv`

3. 安装模块到虚拟环境：`conda install urllib3`

4. 执行项目的Python脚本。

5. 取消激活虚拟环境：`conda deactivate`

> 方式二：通过`IDEA`

1. 使用`IDEA`软件打开项目目录。`注意：若打开项目目录后，只显示文件不显示目录，左侧栏颜色为黄色，则需要先删除项目目录下的.idea目录，然后重新打开项目目录`

2. 依次点击：
	1. 文件 -> 项目结构... -> 平台设置 -> SDK -> 清理无效的（变红色的）SDK。
	2. 项目设置 -> 项目 -> SDK -> 从磁盘添加 Python SDK... -> Virtualenv环境 或 Conda环境 -> 设置虚拟环境。`此处也可以先用命令行方式创建虚拟环境，然后IDEA添加这个环境。`

3. 点击`IDEA`软件自带的终端，执行`pip install -r requirements.txt`将模块安装到虚拟环境。

4. 执行项目的Python脚本。

> 方式三：通过`VSCode`

1. 使用`VSCode`软件打开项目目录。`注意：若打开项目目录后异常，则需要先删除项目目录下的.vscode目录，然后重新打开项目目录`

2. 依次点击：底部状态栏Python版本号 -> 选择解释器 -> 设置虚拟环境。`此处也可以先用命令行方式创建虚拟环境，然后VSCode添加这个环境。`

3. 点击`VSCode`软件自带的终端，执行`pip install -r requirements.txt`将模块安装到虚拟环境。

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

### 7. 调试项目

`python -m pdb xx.py`

或使用IDE：

收费：`IDEA + Python插件`

免费：`VSCode + Python插件`
