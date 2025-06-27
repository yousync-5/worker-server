# finalizer.py
import subprocess
import os

def convert_to_shorts_format(input_path: str, output_dir: str = "results") -> str:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "final_shorts.mp4")

    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf", "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"쇼츠 변환 실패: {e}")
