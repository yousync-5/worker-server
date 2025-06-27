import subprocess
import os

def download_youtube_video(url: str, save_dir: str = "downloads") -> str:
    os.makedirs(save_dir, exist_ok=True)
    output_template = os.path.join(save_dir, "%(title).80s.%(ext)s")

    command = [
        "yt-dlp",
        "-f", "mp4",
        "-o", output_template,
        url
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception("yt-dlp 다운로드 실패") from e

    # 다운로드된 파일명을 찾아서 반환 (제일 최근 수정된 파일)
    downloaded_files = sorted(
        [os.path.join(save_dir, f) for f in os.listdir(save_dir)],
        key=os.path.getmtime,
        reverse=True
    )
    return downloaded_files[0]  # 최신 파일 반환