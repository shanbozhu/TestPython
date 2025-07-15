#!/bin/bash
# usage:
# ./start_venv.sh

current_dir=$(pwd)
venv_dir="$current_dir/.venv"

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

# 虚拟环境是否存在
if [ ! -d "$venv_dir" ]; then
  echo "环境不存在，正在创建..."
  uv init . --python 3.10
  uv venv
  if [ $? -eq 0 ]; then
    echo "环境创建成功。"
    rm main.py
  else
    echo "环境创建失败，请重试。"
    exit 1
  fi
fi

# 同步环境
uv sync
if [ $? -eq 0 ]; then
  echo "环境同步完成！！！"
else
  echo "环境同步失败，请重试。"
  exit 1
fi
# 环境启动成功
echo "环境已经启动，可以开始使用 uv run xxx.py 执行 Python 脚本了..."
