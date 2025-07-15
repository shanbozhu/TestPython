#!/bin/bash
# usage:
# ./start.sh

current_dir=$(pwd)
venv_dir="$current_dir/.venv"
pyproject_file="pyproject.toml"

# 检查是否安装 uv
cmd="uv"
if ! command -v "$cmd" &>/dev/null; then
  printf "uv 未安装，正在安装...\n" >&2
  if ! curl -LsSf https://astral.sh/uv/install.sh | sh; then
    printf "uv 安装失败，请重试。\n" >&2
    exit 1
  fi
  printf "uv 安装成功。\n"
fi

# 工程配置文件是否存在
if [[ ! -f "$pyproject_file" ]]; then
  echo "配置文件不存在，正在创建..."
  uv init . --python 3.10 &>/dev/null
  if [[ $? -eq 0 ]]; then
    echo "创建成功。"
  else
    echo "创建失败，请重试。"
    exit 1
  fi
fi

# main.py 文件是否存在
if [[ -f "main.py" ]]; then
    rm main.py
fi

# 虚拟环境是否存在
if [[ ! -d "$venv_dir" ]]; then
  echo "环境不存在，正在创建..."
  uv venv &>/dev/null
  if [[ $? -eq 0 ]]; then
    echo "环境创建成功。"
  else
    echo "环境创建失败，请重试。"
    exit 1
  fi
fi

# 同步环境
echo "正在同步环境..."
uv sync &>/dev/null
if [[ $? -eq 0 ]]; then
  echo "环境同步完成！！！"
else
  echo "环境同步失败，请重试。"
  exit 1
fi
# 环境启动成功
echo "环境已经启动！！！"
echo "  可以开始使用 uv add xxx_package 安装 依赖包！！！"
echo "  可以开始使用 uv run xxx.py 执行 Python 脚本！！！"
