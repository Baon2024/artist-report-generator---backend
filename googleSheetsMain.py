import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import json
import base64
from pathlib import Path
from google.oauth2 import service_account

load_dotenv()



# Scopes: Docs + create files in your Drive
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]

TOKEN_PATH = "token.json"
CREDS_PATH = "credentials.json"

import binascii
b64 = os.getenv("GOOGLE_CREDENTIALS_B64")
print("ENV present:", b64 is not None)
print("B64 length:", len(b64) if b64 else 0)

try:
    raw = base64.b64decode(b64 or "", validate=True)
    print("Decoded bytes:", len(raw))
    # Quick prefix/suffix check (don’t print full secret)
    print("Starts with:", raw[:30])
    print("Ends with:", raw[-30:])
    info = json.loads(raw)
    print("JSON OK. Keys:", list(info.keys()))
except binascii.Error as e:
    print("Base64 invalid (likely truncated/wrapped):", e)
except json.JSONDecodeError as e:
    print("Decoded bytes not valid JSON:", e)


def get_credentials_service():
    path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not path:
        raise RuntimeError("Set GOOGLE_APPLICATION_CREDENTIALS to your secret file path on Render")
    if not os.path.isfile(path):
        raise RuntimeError(f"Credentials file not found at {path}")
    creds = service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    print("Using service account:", creds.service_account_email)
    return creds

def get_credentials_service3():
    path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not path:
        raise RuntimeError("Set GOOGLE_APPLICATION_CREDENTIALS to your service-account JSON path")

    p = Path(path)
    if not p.is_absolute():
        p = (Path(__file__).resolve().parent / p).resolve()
    if not p.is_file():
        raise RuntimeError(f"Credentials file not found at {p}")

    # Base SA creds with the required scopes
    creds = service_account.Credentials.from_service_account_file(str(p), scopes=SCOPES)

    # Optional: impersonate a Workspace user if Domain-Wide Delegation is configured
    subject = os.getenv("GOOGLE_WORKSPACE_USER")  # e.g. "you@inaugural.ai"
    if subject:
        creds = creds.with_subject(subject)
        print(f"Using delegated creds: {creds.service_account_email} as {subject}")
    else:
        print(f"Using service account: {creds.service_account_email}")

    return creds



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

#def main():
    #creds = get_credentials_service3()
    #print("SA email:", creds.service_account_email)
    #print("Project:", creds.project_id)
    #print("Scopes:", getattr(creds, 'scopes', None))

    #drive = build("drive", "v3", credentials=get_credentials_service())
    #about = drive.about().get(fields="user,storageQuota").execute()
    #print("Acting as:", about["user"]["emailAddress"])

    
    

    #Use Docs API
    #docs_service = build("docs", "v1", credentials=creds)
    #doc = docs_service.documents().create(
        #body={"title": "artist re"}
    #).execute()

    #doc_id = doc.get("documentId")
    #print(f"Created Doc: https://docs.google.com/document/d/{doc_id}")

#if __name__ == "__main__":
    #main()