# youtube_auth.py

from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_tokens():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    creds = flow.run_local_server(port=8080)
    
    # 토큰 저장
    with open("tokens.json", "w") as f:
        f.write(creds.to_json())

if __name__ == "__main__":
    get_tokens()
