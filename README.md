---
title: "Python 环境搭建指南"
date: 2019-05-20T19:14:49+08:00
draft: false
---

[TOC]

## 一、全局安装 python

`brew install python`  
`python --version`

安装`python`时会自动安装`pip`

- `Python`语言是开源的。`Python`的开源本质是它的实现（`解释器`、`标准库`）以及整个生态系统的开源，而不仅仅是语法规则。
- `标准库`是指由编程语言官方或语言规范定义并提供的一组基础功能库。这些库通常与语言一起分发，不需要额外安装即可使用。标准库旨在提供常见任务的基础支持，使开发者在编程时不必重复造轮子，从而提高效率和代码质量。
- `标准库`是编程语言中不可或缺的一部分，提供了实现常见功能所需的工具集。它包含从基本的数据结构和数学函数到复杂的网络通信和系统交互等内容。标准库的设计直接影响了语言的易用性、性能以及开发效率，是编程语言生态的重要基石。
- `标准库`的标准由编程语言的官方组织、标准化委员会或语言的主要开发者制定。这些组织和开发者根据语言的设计目标、使用场景和用户需求来定义标准库的内容和规范。
- 高级语言（例如`Python`）提供的`标准库`在底层通常会调用`C`语言编写的函数或库。这是因为`C`语言能够直接与操作系统、硬件和系统资源交互，并且具有高效、底层的特性，使其非常适合实现这些底层功能。
- 这种设计结合了`C`的高性能和`Python`的高可读性，既提升了执行效率，又保持了开发的便利性。

## 二、运行项目

- 将项目`压缩包`复制到电脑，`解压`后在虚拟环境中执行。
- 虚拟环境：含有`Python解释器`和`依赖模块`。

### 方式一：通过`命令行`

一、通过 Python 自带的 **venv** 创建虚拟环境。

1. 进入项目根目录执行：`python -m venv .venv`
2. 激活虚拟环境
   1. Windows执行：`.venv\Scripts\activate`
   2. macOS/Linux执行：`source .venv/bin/activate`
3. 安装模块到虚拟环境：`pip install urllib3`
4. 执行项目的 Python 脚本。
5. 取消激活虚拟环境：`deactivate`

注：当前虚拟环境中的 Python 是系统安装 Python 的引用。

二、通过 **conda** 创建虚拟环境

1. 进入项目根目录执行：
   1. 指定路径下创建：`conda create --prefix .venv python=3.10`
   2. 默认路径下创建：`conda create --name .venv python=3.10`
2. 激活虚拟环境：`conda activate .venv`
3. 安装模块到虚拟环境：`conda install urllib3`
4. 执行项目的 Python 脚本。
5. 取消激活虚拟环境：`conda deactivate`

注：当前虚拟环境中的 Python 是 conda 下载的 Python。

三、通过 **uv** 创建虚拟环境

1. 初始化一个 Python 项目：`uv init myproject --python 3.10`
2. 进入项目根目录：`cd myproject`
3. 创建虚拟环境（可选。运行时会自动创建，无需手动创建）：`uv venv`
4. 安装模块：`uv add requests`
5. 安装开发模块：`uv add --dev pytest`
6. 运行 Python 项目：`uv run script.py`

### 方式二：通过`IDEA`

1. 使用`IDEA`软件打开项目目录。  
`注意：若打开项目目录后，只显示文件不显示目录，左侧栏颜色为黄色，则需要先删除项目目录下的 .idea 目录，然后重新打开项目目录`
2. 依次点击：
   1. 文件 -> 项目结构... -> 平台设置 -> SDK -> 清理无效的（变红色的）SDK。
   2. 项目设置 -> 项目 -> SDK -> 从磁盘添加 Python SDK... -> Virtualenv环境 或 Conda环境 -> 设置虚拟环境。  
   `注意：此处也可以先用命令行方式创建虚拟环境，然后 IDEA 添加这个环境。`
3. 点击`IDEA`软件自带的终端，将模块安装到虚拟环境。
4. 执行项目的 Python 脚本。

### 方式三：通过`VSCode`

1. 使用`VSCode`软件打开项目目录。  
`注意：若打开项目目录后异常，则需要先删除项目目录下的 .vscode 目录，然后重新打开项目目录`
2. 依次点击：底部状态栏的 Python 版本号 -> 选择解释器 -> 设置虚拟环境。  
`注意：此处也可以先用命令行方式创建虚拟环境，然后 VSCode 添加这个环境。`
3. 点击`VSCode`软件自带的终端，将模块安装到虚拟环境。
4. 执行项目的 Python 脚本。

参考文档：https://zhuanlan.zhihu.com/p/700249286

## 三、安装模块或环境

1. 如果是 venv 创建的虚拟环境，则安装模块：
   1. `pip install urllib3 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`
   2. `pip install 'urllib3<2.0'`
   3. `pip install urllib3==1.26.19`
   4. `pip install -r requirements.txt`
2. 如果是 conda 创建的虚拟环境，则：
   1. 安装模块：  
   `conda install urllib3`
   2. 安装整个环境：
      - 指定路径下创建：`conda env create -f environment.yml --prefix .venv`
      - 默认路径下创建：`conda env create -f environment.yml`
3. 如果是 uv 创建的虚拟环境，则：
   1. 安装模块：  
   `uv add requests`
   2. 安装整个环境：  
   `uv sync`

## 四、卸载模块

1. 如果是 venv 创建的虚拟环境，则：  
`pip uninstall urllib3`
2. 如果是 conda 创建的虚拟环境，则：  
`conda uninstall urllib3`
3. 如果是 uv 创建的虚拟环境，则：  
`uv remove requests`

## 五、导出模块或环境

1. 如果是 venv 创建的虚拟环境，则导出模块：  
`pip freeze > requirements.txt`
2. 如果是 conda 创建的虚拟环境，则导出整个环境：  
`conda env export > environment.yml`
3. 如果是 uv 创建的虚拟环境，则导出整个环境：  
`pyproject.toml + uv.lock`

## 六、打包项目

1. 使用`导出模块或环境`中的命令导出项目中的模块或环境。
2. `压缩`当前项目，注意不要包含`.venv`虚拟环境目录。

## 七、调试项目

`python -m pdb xx.py`

或使用IDE：  
收费：`IDEA + Python插件`  
免费：`VSCode + Python插件`

---

## 一、项目管理

<table>
    <tr>
        <td><b>语言</b></td>
        <td><b>编译器/解释器</b></td>
        <td><b>包管理工具</b></td>
        <td><b>配置文件</b></td>
        <td><b>依赖隔离</b></td>
        <td><b>编译器/解释器隔离</b></td>
    </tr>
    <tr>
        <td>OC/Swift</td>
        <td>Xcode</td>
        <td>pod</td>
        <td>podfile</td>
        <td>pod 支持</td>
        <td>不支持。安装多个版本 Xcode 后可以支持</td>
    </tr>
    <tr>
        <td rowspan="3">Python</td>
        <td rowspan="3">python</td>
        <td>pip</td>
        <td>requirements.txt</td>
        <td>pip 不支持。依赖默认是全局安装的，结合 venv 虚拟环境后可以支持</td>
        <td>不支持。结合 pyenv 安装多个版本 python 后可以支持</td>
    </tr>
    <tr>
        <td>conda</td>
        <td>environment.yml</td>
        <td>conda 支持</td>
        <td>conda 支持</td>
    </tr>
    <tr>
        <td>uv</td>
        <td>pyproject.toml</td>
        <td>uv 支持</td>
        <td>uv 支持</td>
    </tr>
    <tr>
        <td>TypeScript<br>JavaScript</td>
        <td>node（封装的 V8 引擎）</td>
        <td>npm</td>
        <td>package.json</td>
        <td>npm 支持</td>
        <td>不支持。结合 nvm 安装多个版本 node 后可以支持</td>
    </tr>
    <tr>
        <td>Ruby</td>
        <td>ruby</td>
        <td>gem</td>
        <td>未知</td>
        <td>gem 支持</td>
        <td>不支持。结合 rvm/rbenv 安装多个版本 ruby 后可以支持</td>
    </tr>
</table>

* pod：用于`objective-c`模块安装或卸载。服务于`OC社区`。pod 本身是使用 ruby 编写的软件，通过 gem 进行安装。
* pip：用于`python`模块安装或卸载，安装`python`时会自动安装`pip`。服务于`Python社区`。
* RubyGems：简称`gem`，用于`ruby`编写的软件的安装或卸载，安装`ruby`时会自动安装`gem`。服务于`Ruby社区`。
* npm：用于`node.js`模块安装或卸载，安装`node.js`时会自动安装`npm`。服务于`JavaScript社区`。

## 二、conda 常用命令

```
1. 查看已安装的包
conda list
2. 退出环境
conda deactivate
3. 查看所有环境
conda env list
4. 删除环境
conda env remove --name ENV_NAME
conda env remove --prefix /path/to/ENV_NAME
5. 指定渠道
conda install -c conda-forge PACKAGE_NAME
6. 更新 Conda 本身
conda update conda
7. 更新所有已安装的包
conda update --all
8. 清理未使用的包和缓存
conda clean --all
```

## 三、配置文件

1. **venv** 的配置文件`requirements.txt`
```
certifi==2025.6.15
charset-normalizer==3.4.2
idna==3.10
requests==2.32.4
urllib3==2.5.0
```

2. **conda** 的配置文件`environment.yml`
```
name: /Users/zhushanbo/Desktop/send_im_message/.venv
channels:
  - defaults
dependencies:
  - brotlicffi=1.0.9.2=py310h313beb8_1
  - bzip2=1.0.8=h80987f9_6
  - ca-certificates=2025.2.25=hca03da5_0
  - certifi=2025.6.15=py310hca03da5_0
  - cffi=1.17.1=py310h3eb5a62_1
  - charset-normalizer=3.3.2=pyhd3eb1b0_0
  - expat=2.7.1=h313beb8_0
  - idna=3.7=py310hca03da5_0
  - libcxx=17.0.6=he5c5206_4
  - libffi=3.4.4=hca03da5_1
  - ncurses=6.4=h313beb8_0
  - openssl=3.0.16=h02f6b3c_0
  - pip=25.1=pyhc872135_2
  - pycparser=2.21=pyhd3eb1b0_0
  - pysocks=1.7.1=py310hca03da5_0
  - python=3.10.18=h19e8193_0
  - readline=8.2=h1a28f6b_0
  - requests=2.32.4=py310hca03da5_0
  - setuptools=78.1.1=py310hca03da5_0
  - sqlite=3.45.3=h80987f9_0
  - tk=8.6.14=h6ba3021_1
  - tzdata=2025b=h04d1e81_0
  - urllib3=2.5.0=py310hca03da5_0
  - wheel=0.45.1=py310hca03da5_0
  - xz=5.6.4=h80987f9_1
  - zlib=1.2.13=h18a0788_1
prefix: /Users/zhushanbo/Desktop/send_im_message/.venv
```

3. **uv** 的配置文件`pyproject.toml`
```
[project]
name = "myproject1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.32.4",
]

[dependency-groups]
dev = [
    "pytest>=8.4.1",
]
```
