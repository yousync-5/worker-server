# cutter.py
import subprocess
import os

def cut_video(input_path: str, start_time: str, end_time: str, output_dir: str = "results") -> str:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cut_output.mp4")

    command = [
        "ffmpeg",
        "-ss", start_time,
        "-to", end_time,
        "-i", input_path,
        "-c:v", "copy",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"영상 자르기 실패: {e}")
