# merger.py

import subprocess
import os

def merge_audio(video_path: str, user_audio_path: str, output_dir: str = "results") -> str:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "merged_output.mp4")

    if not os.path.exists(user_audio_path):
        raise Exception(f"사용자 음성 파일을 찾을 수 없습니다: {user_audio_path}")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", user_audio_path,
        "-filter_complex",
        "[0:a]volume=0.3[a1];[1:a]volume=1.0[a2];[a1][a2]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"오디오 병합 실패: {e}")
