from pydub import AudioSegment

def split_audio_at_time(audio_file, split_time, output_file1, output_file2):
    # 加载音频
    audio = AudioSegment.from_file(audio_file)
    # 分割音频
    split_time_ms = split_time * 1000  # 将秒转换为毫秒
    audio_segment1 = audio[:split_time_ms]  # 从开始到指定时间的音频
    audio_segment2 = audio[split_time_ms:]  # 从指定时间到结束的音频
    # 导出分割后的音频
    audio_segment1.export(output_file1, format="mp3")  # 可以根据需要更改格式
    audio_segment2.export(output_file2, format="mp3")  # 可以根据需要更改格式
