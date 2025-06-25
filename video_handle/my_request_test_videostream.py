import whisper

# 加载 Whisper 模型（使用 base 模型以平衡速度与准确度）
model = whisper.load_model("base")

# 进行语音识别
result = model.transcribe("/Users/zhushanbo/Desktop/extracted_audio.wav")

# 提取并展示文本内容
transcribed_text = result["text"]
transcribed_text[:1000]  # 显示前 1000 个字符预览
