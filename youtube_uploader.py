# youtube_uploader.py

import os
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 파일 경로
VIDEO_FILE = "results/final_shorts.mp4"

# 업로드할 영상의 기본 정보
VIDEO_TITLE = "내가 더빙한 명장면 #Shorts"
VIDEO_DESCRIPTION = "YOUSYNC 자동 업로드 테스트 영상입니다."
VIDEO_CATEGORY_ID = "1"  # Film & Animation
VIDEO_PRIVACY_STATUS = "unlisted"  # 또는 "public", "private"

def upload_to_youtube():
    # 토큰 로드
    creds = Credentials.from_authorized_user_file("tokens.json", ["https://www.googleapis.com/auth/youtube.upload"])

    # 유튜브 API 클라이언트 생성
    youtube = build("youtube", "v3", credentials=creds)

    # 업로드 준비
    media = MediaFileUpload(VIDEO_FILE, mimetype="video/mp4", resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": VIDEO_TITLE,
                "description": VIDEO_DESCRIPTION,
                "tags": ["YOUSYNC", "shorts", "더빙"],
                "categoryId": VIDEO_CATEGORY_ID
            },
            "status": {
                "privacyStatus": VIDEO_PRIVACY_STATUS
            }
        },
        media_body=media
    )

    print("⏫ 유튜브 업로드 시작 중...")
    response = request.execute()
    print("✅ 업로드 완료!")
    print(f"📺 영상 링크: https://youtube.com/shorts/{response['id']}")

if __name__ == "__main__":
    if not os.path.exists(VIDEO_FILE):
        print(f"❌ 영상 파일이 존재하지 않습니다: {VIDEO_FILE}")
    else:
        upload_to_youtube()
