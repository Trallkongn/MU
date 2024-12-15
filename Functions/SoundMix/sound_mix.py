from pydub import AudioSegment

def append_audio(original_file, audio_to_append, output_file):
    # 加载原始音频
    original_audio = AudioSegment.from_file(original_file)
    # 加载要拼接的音频
    audio_to_append_segment = AudioSegment.from_file(audio_to_append)
    # 拼接音频
    combined_audio = original_audio + audio_to_append_segment
    # 导出拼接后的音频
    combined_audio.export(output_file, format="mp3")  # 可以根据需要更改格式
