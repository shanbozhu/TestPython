### 1. 安装模块

`pip install urllib3 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

`pip install 'urllib3<2.0'`

`pip install urllib3==1.26.19`

`pip install -r requirements.txt`

### 2. 卸载模块

`pip uninstall urllib3`

### 3. 导出模块

`pip freeze > requirements.txt`

### 4. 打包项目

1. 使用`pip freeze > requirements.txt`导出当前项目的所有模块。

2. 压缩当前项目，不包含`.venv`虚拟环境。

### 5. 发布项目

将项目压缩包复制到其他电脑，下面两种方式均可解压后执行

> 方式一：通过IDE

1. 在其他电脑解压后，使用`IDEA`等软件打开项目目录。

2. 点击`配置 Python 解释器`，弹出的对话框中依次点击`依赖`->`模块SDK`->`添加 Python SDK...`，弹出的对话框，为当前项目中创建`新的虚拟环境`。

3. 点击`IDEA`等软件的终端，执行`pip install -r requirements.txt`将对应版本的模块安装到`新的虚拟环境`。

4. 可以成功执行`项目的Python 脚本`。

> 方式二：通过命令行

1. 创建新的虚拟环境
`python -m venv .venv`

2. 激活新的虚拟环境 
   1. Windows执行`.venv\Scripts\activate`
   2. MacOS/Linux执行`source .venv/bin/activate`

3. 安装模块到新的虚拟环境
`pip install -r requirements.txt`

参考文档：https://zhuanlan.zhihu.com/p/700249286