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

- 将项目`压缩包`复制到电脑，`解压`后在虚拟环境中执行。

- 虚拟环境：含有`Python解释器`和`依赖模块`。

> 方式一：通过`命令行`

一、通过Python自带的**venv**创建虚拟环境。

1. 进入项目根目录执行：`python -m venv .venv`

2. 激活虚拟环境
	1. Windows执行：`.venv\Scripts\activate`
	2. macOS/Linux执行：`source .venv/bin/activate`

3. 安装模块到虚拟环境：`pip install urllib3`

4. 执行项目的Python脚本。

5. 取消激活虚拟环境：`deactivate`

注：当前虚拟环境中的Python是系统安装Python的引用。

二、通过**conda**创建虚拟环境

1. 进入项目根目录执行：
	1. 指定路径下创建：`conda create --prefix .conda python=3.10`
	2. 默认路径下创建：`conda create --name .conda python=3.10`

2. 激活虚拟环境：`conda activate .conda`

3. 安装模块到虚拟环境：`conda install urllib3`

4. 执行项目的Python脚本。

5. 取消激活虚拟环境：`conda deactivate`

注：当前虚拟环境中的Python是conda下载的Python。

> 方式二：通过`IDEA`

1. 使用`IDEA`软件打开项目目录。`注意：若打开项目目录后，只显示文件不显示目录，左侧栏颜色为黄色，则需要先删除项目目录下的.idea目录，然后重新打开项目目录`

2. 依次点击：
	1. 文件 -> 项目结构... -> 平台设置 -> SDK -> 清理无效的（变红色的）SDK。
	2. 项目设置 -> 项目 -> SDK -> 从磁盘添加 Python SDK... -> Virtualenv环境 或 Conda环境 -> 设置虚拟环境。`此处也可以先用命令行方式创建虚拟环境，然后IDEA添加这个环境。`

3. 点击`IDEA`软件自带的终端，将模块安装到虚拟环境。

4. 执行项目的Python脚本。

> 方式三：通过`VSCode`

1. 使用`VSCode`软件打开项目目录。`注意：若打开项目目录后异常，则需要先删除项目目录下的.vscode目录，然后重新打开项目目录`

2. 依次点击：底部状态栏Python版本号 -> 选择解释器 -> 设置虚拟环境。`此处也可以先用命令行方式创建虚拟环境，然后VSCode添加这个环境。`

3. 点击`VSCode`软件自带的终端，将模块安装到虚拟环境。

4. 执行项目的Python脚本。

参考文档：https://zhuanlan.zhihu.com/p/700249286

### 3. 安装模块或环境

推荐在`虚拟环境`中安装模块

`pip install urllib3 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

`pip install 'urllib3<2.0'`

`pip install urllib3==1.26.19`

`pip install -r requirements.txt`

如果是conda创建的虚拟环境，则安装模块：

`conda install urllib3`

安装整个环境：

1. 指定路径下创建：`conda env create -f environment.yml --prefix .conda`

2. 默认路径下创建：`conda env create -f environment.yml`

### 4. 卸载模块

推荐在`虚拟环境`中卸载模块

`pip uninstall urllib3`

如果是conda创建的虚拟环境，则：

`conda uninstall urllib3`

### 5. 导出模块或环境

必须在`虚拟环境`中导出模块

`pip freeze > requirements.txt`

如果是conda创建的虚拟环境，则导出整个环境：

`conda env export > environment.yml`

### 6. 打包项目

1. 使用`导出模块或环境`中的命令导出项目中的模块或环境。

2. `压缩`当前项目，注意不要包含`.venv`或`.conda`虚拟环境目录。

### 7. 调试项目

`python -m pdb xx.py`

或使用IDE：

收费：`IDEA + Python插件`

免费：`VSCode + Python插件`

---

### 1. 项目管理
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
        <td>pod支持</td>
        <td>不支持。安装多个版本Xcode后可以支持</td>
    </tr>
    <tr>
        <td rowspan="3">Python</td>
        <td>python</td>
        <td>pip</td>
        <td>requirements.txt</td>
        <td>pip不支持。依赖默认是全局安装的，结合venv虚拟环境后可以支持</td>
        <td>不支持。结合pyenv安装多个版本python后可以支持</td>
    </tr>
    <tr>
        <td>python</td>
        <td>conda</td>
        <td>environment.yml</td>
        <td>conda支持</td>
        <td>conda支持</td>
    </tr>
    <tr>
        <td>python</td>
        <td>uv</td>
        <td>pyproject.toml</td>
        <td>uv支持</td>
        <td>uv支持</td>
    </tr>
    <tr>
        <td>TypeScript/JavaScript</td>
        <td>node</td>
        <td>npm</td>
        <td>package.json</td>
        <td>npm支持</td>
        <td>不支持。结合nvm安装多个版本node后可以支持</td>
    </tr>
</table>

### 2. conda常用命令

```
1. 查看已安装的包
conda list
2. 退出环境
conda deactivate
3. 删除环境
conda env remove --name ENV_NAME
conda env remove --prefix /path/to/ENV_NAME
4. 查看所有环境
conda env list
5. 指定渠道
conda install -c conda-forge PACKAGE_NAME
6. 更新 Conda 本身
conda update conda
7. 更新所有已安装的包
conda update --all
8. 清理未使用的包和缓存
conda clean --all
```

### 3. 配置文件

1. **venv**的配置文件requirements.txt

```
certifi==2025.6.15
charset-normalizer==3.4.2
idna==3.10
requests==2.32.4
urllib3==2.5.0
```

2. **conda**的配置文件environment.yml

```
name: /Users/zhushanbo/Desktop/send_im_message/.conda
channels:
  - defaults
dependencies:
  - brotlicffi=1.0.9.2=py313h313beb8_1
  - bzip2=1.0.8=h80987f9_6
  - ca-certificates=2025.2.25=hca03da5_0
  - certifi=2025.6.15=py313hca03da5_0
  - cffi=1.17.1=py313h3eb5a62_1
  - charset-normalizer=3.3.2=pyhd3eb1b0_0
  - expat=2.7.1=h313beb8_0
  - idna=3.7=py313hca03da5_0
  - libcxx=17.0.6=he5c5206_4
  - libffi=3.4.4=hca03da5_1
  - libmpdec=4.0.0=h80987f9_0
  - ncurses=6.4=h313beb8_0
  - openssl=3.0.16=h02f6b3c_0
  - pip=25.1=pyhc872135_2
  - pycparser=2.21=pyhd3eb1b0_0
  - pysocks=1.7.1=py313hca03da5_0
  - python=3.13.5=h2eb94d5_100_cp313
  - python_abi=3.13=0_cp313
  - readline=8.2=h1a28f6b_0
  - requests=2.32.4=py313hca03da5_0
  - setuptools=78.1.1=py313hca03da5_0
  - sqlite=3.45.3=h80987f9_0
  - tk=8.6.14=h6ba3021_1
  - tzdata=2025b=h04d1e81_0
  - urllib3=2.5.0=py313hca03da5_0
  - wheel=0.45.1=py313hca03da5_0
  - xz=5.6.4=h80987f9_1
  - zlib=1.2.13=h18a0788_1
prefix: /Users/zhushanbo/Desktop/send_im_message/.conda
```