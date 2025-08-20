import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Scopes: Docs + create files in your Drive
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]

TOKEN_PATH = "token.json"
CREDS_PATH = "credentials.json"

def get_credentials():
    creds = None

    # Reuse saved tokens if present
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # If no creds or invalid, get/refresh them
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh silently (no browser needed)
            creds.refresh(Request())
        else:
            # First-time auth: open browser, handle redirect locally
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=3000, prompt="consent")

        # Save for next runs
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())

    return creds

# def main():
    # creds = get_credentials()

    # Use Docs API
    # docs_service = build("docs", "v1", credentials=creds)
    # doc = docs_service.documents().create(
        # body={"title": "artist re"}
    # ).execute()

    # doc_id = doc.get("documentId")
    # print(f"Created Doc: https://docs.google.com/document/d/{doc_id}")

# if __name__ == "__main__":
    # main()