import subprocess

# 定义文件路径
video_path = "/Users/zhushanbo/Desktop/15_1750591017.mp4"
audio_path = "/Users/zhushanbo/Desktop/extracted_audio.wav"

# 使用 ffmpeg 提取音频
command = [
    "ffmpeg", "-i", video_path,
    "-vn",  # no video
    "-acodec", "pcm_s16le",  # 音频编码
    "-ar", "16000",  # 采样率
    "-ac", "1",  # 单声道
    audio_path
]

# 执行命令
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
audio_path  # 返回提取出的音频文件路径
