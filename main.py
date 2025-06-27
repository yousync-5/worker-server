# main.py

import time

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from downloader import download_youtube_video
from cutter import cut_video
from merger import merge_audio
from finalizer import convert_to_shorts_format

app = FastAPI()

class VideoRequest(BaseModel):
    audio_path: Optional[str] = None    # 사용자의 더빙 음성 파일 위치, 미리 서버에 다운로드 되어있어야 한다.
                                        # 추후 음성 파일자체를 넘겨받는 로직으로 변환 필요
    youtube_url: str    # 원본 영상 URL
    start_time: str     # 예: "00:01:20"
    end_time: str       # 예: "00:01:35"


@app.post("/process-video")
async def process_video(request: VideoRequest):
    start_time_measure = time.time()  # 시간 측정 시작
    # 1. 유튜브 영상 다운로드
    try:
        # 1. 유튜브 영상 다운로드
        video_path = download_youtube_video(request.youtube_url)   
        # 2. 지정 구간 영상 자르기
        cut_path = cut_video(video_path, request.start_time, request.end_time)
        # 3. 유저 음성 + 유튜브 영상 음성 합치기
        # merged_path = merge_audio(cut_path, request.audio_path)
        # 4. 쇼츠용 세로 영상 변환
        # final_path = convert_to_shorts_format(merged_path)
        final_path = convert_to_shorts_format(cut_path)

    except Exception as e:
        return {"error": str(e)}

    end_time_measure = time.time()  # 시간 측정 종료
    duration = round(end_time_measure - start_time_measure, 2)  # 소수 둘째 자리까지 측정

    return {
        "message": "쇼츠용 영상 생성 완료",
        "video_path": video_path,
        "cut_video_path": cut_path,
        # "final_video_path": merged_path,
        "shorts_ready_video": final_path,
        "duration_seconds": duration
    }