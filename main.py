from moviepy.editor import VideoFileClip

def main():
    input_file = "new-sample.mp4"
    output_file = "output_sample.mp4"

    # 读取视频文件
    video = VideoFileClip(input_file)

    # 裁剪视频 - 去掉上面50px的高度
    cropped_video = video.crop(y1=50, y2=video.h)

    # 保持音频和其他部分一致
    cropped_video = cropped_video.set_audio(video.audio)

    # 输出裁剪后的文件
    cropped_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # 释放资源
    video.close()
    cropped_video.close()

if __name__ == "__main__":
    main()
