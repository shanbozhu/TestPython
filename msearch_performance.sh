#!/bin/bash

current_dir=$(pwd)
venv_dir="$current_dir/.venv"

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
  if [ -f "$requirements" ]; then
    pip3 freeze > installed_packages.txt
    if [ $? -ne 0 ]; then
      echo "pip freeze 执行失败，请重试。"
      exit 1
    fi
    diff "$current_dir/requirements.txt" "$current_dir/installed_packages.txt" &> /dev/null
    if [ $? -ne 0 ]; then
      echo "虚拟环境中模块缺失，正在安装..."
      pip3 install -r requirements.txt &> /dev/null
      if [ $? -ne 0 ]; then
        echo "虚拟环境中模块安装失败，请重试。"
        exit 1
      fi
    fi
  else
    echo "没有模块列表文件，无法在虚拟环境中批量自动安装模块。Python脚本可能会执行失败！！！"
    echo "若Python脚本执行失败，提示缺少模块，请按照下面步骤手动执行。"
    echo "  1. 执行命令激活虚拟环境：source $venv_dir/bin/activate"
    echo "  2. 在虚拟环境中安装缺失的模块：pip3 install xyz，xyz表示缺失的模块"
    echo "  3. 执行执行Python脚本：$current_dir/msearch_performance.py"
  fi
else
  echo "虚拟环境激活失败，请重试。"
  exit 1
fi
# 执行脚本
echo "正在执行Python脚本..."
$current_dir/msearch_performance.py
echo "Python脚本执行完成。"
# 取消激活虚拟环境
deactivate