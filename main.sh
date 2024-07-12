#!/bin/bash

current_dir=$(pwd)
venv_dir="$current_dir/.venv"
python_file="your_python_file.py"

# 虚拟环境是否存在
if [ ! -d "$venv_dir" ]; then
  # echo "$venv_dir 虚拟环境不存在，正在创建..."
  echo "虚拟环境不存在，正在创建..."
  python3 -m venv .venv
  if [ $? -eq 0 ]; then
    echo "虚拟环境创建成功。"
  else
    echo "虚拟环境创建失败，请重试。"
    exit 1
  fi
fi

# 激活虚拟环境
source $venv_dir/bin/activate
if [ $? -eq 0 ]; then
  # requirements.txt文件是否存在
  requirements="$current_dir/requirements.txt"
  installed_packages="$current_dir/.installed_packages.txt"
  if [ -f "$requirements" ]; then
    # 导出项目中已安装的模块
    pip3 freeze > "$installed_packages"
    if [ $? -ne 0 ]; then
      echo "项目中已安装的模块导出失败，请重试。"
      exit 1
    fi
    diff "$requirements" "$installed_packages" &> /dev/null
    if [ $? -ne 0 ]; then
      echo "虚拟环境中模块缺失，正在安装..."
      pip3 install -r "$requirements" &> /dev/null
      if [ $? -ne 0 ]; then
        echo "虚拟环境中模块安装失败，请重试。"
        exit 1
      fi
    fi
  else
    echo "没有模块列表文件，无法在虚拟环境中批量自动安装模块。请按照下面步骤手动执行！！！"
    echo "  1. 执行Python脚本：$current_dir/$python_file 根据失败提示查看缺失的模块。"
    echo "  2. 在虚拟环境中安装缺失的模块：pip3 install xyz，xyz表示缺失的模块。"
    echo "  3. 重复步骤1和2安装所有缺失的模块，直至Python脚本执行成功。"
    exit 1
  fi
else
  echo "虚拟环境激活失败，请重试。"
  exit 1
fi
# 虚拟环境启动成功
echo "虚拟环境已经启动，可以开始执行Python脚本了..."
# 执行脚本
# "$current_dir/$python_file"
# 导出项目中已安装的模块
pip3 freeze > "$requirements"
# 取消激活虚拟环境
# deactivate