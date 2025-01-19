import yt_dlp


def download_video(url, save_path="."):
    try:
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save as "Title.mp4"
            "format": "bestvideo+bestaudio/best",  # Download best quality
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_directory = input(
        "Enter the directory to save the video (leave empty for current directory): "
    ).strip()
    download_video(video_url, save_path=save_directory or ".")
