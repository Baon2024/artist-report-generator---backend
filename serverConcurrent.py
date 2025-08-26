from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv
#from gradio_client import AsyncClient  # pip install gradio_client
from helFunction import generate_report_sync
from helFunctionConcurrent import generate_report_sync_concurrent
from anyio import to_thread  # pip install anyio
import os
from openai import OpenAI
from dynamic_prompt_structure import generate_dynamic_report_prompt_structure
from googleSheetsMain import get_credentials, get_credentials_service
from googleapiclient.discovery import build


load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)




app = FastAPI()

# Only allow your frontends
origins = [
    "http://localhost:3009",
    "https://artist-report-generator-frontend.vercel.app",
    "https://reverb.corecollectif.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

class ReportRequest(BaseModel):
    chosenArtist: str
    reportFocus: str

class GeneratedReport(BaseModel):
    artistReport: str
    chosenArtist: str
    reportFocus: str


@app.get("/health")
def health():
    return {"status": "ok"}


##server endoint to generate google doc from generated reort, and return it to user
@app.post("/reportGoogleDoc")
async def report_google_doc(payload: GeneratedReport) -> Any:
    artist_report = payload.artistReport
    print(f"artist_report is: {artist_report}")
    chosen_artist = payload.chosenArtist
    print(f"chosen_artist is: {chosen_artist}")
    report_focus = payload.reportFocus
    print(f"report_focus is: {report_focus}")

    #need to create google doc, get credentials first
    #creds = get_credentials()
    creds = get_credentials_service()

    # Use Docs API
    docs = build("docs", "v1", credentials=creds)
    doc = docs.documents().create(
        body={"title": f"report on {report_focus} for {chosen_artist}"}# get reort name from combo of artist and theme
    ).execute()

    doc_id = doc.get("documentId")
    doc_url =  f"https://docs.google.com/document/d/{doc_id}"
    print(f"Created Doc: https://docs.google.com/document/d/{doc_id}") 

    cursor = 1
    requests = []

    def insert(text: str):
        nonlocal cursor, requests
        start = cursor
        requests.append({
            "insertText": {"location": {"index": cursor}, "text": text}
        })
        cursor += len(text)
        return start, cursor

    def style_paragraph(start: int, end: int, named_style: str):
        requests.append({
            "updateParagraphStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "paragraphStyle": {"namedStyleType": named_style},
            "fields": "namedStyleType"
            }
        })
    

    s, e = insert(f"{chosen_artist}: {report_focus}\n")
    style_paragraph(s, e, "TITLE")

    # 4) Subtitle (optional)
    s, e = insert("Audience Intelligence & Growth Outline\n")
    style_paragraph(s, e, "SUBTITLE")

    # 5) Spacer
    insert("\n")

    # 6) Body (your whole string)
    #    Keep it simple: normal paragraphs. Make sure it ends with a newline.
    body_text = artist_report.rstrip() + "\n"
    s, e = insert(body_text)
    # (Optional) explicitly set as NORMAL_TEXT
    style_paragraph(s, e, "NORMAL_TEXT")

    # 7) Execute
    docs.documents().batchUpdate(
        documentId=doc_id, body={"requests": requests}
    ).execute()


    return doc_url

    


@app.post("/reportGenerator")
async def report_generator(payload: ReportRequest) -> Any:
    chosen_artist = payload.chosenArtist
    print(f"chosen_artist is: {chosen_artist}")
    report_focus = payload.reportFocus
    print(f"report_focus is: {report_focus}")
    #need a report description passed from frontend - "generate me a report analysing growth markets" 

    if not chosen_artist or not report_focus:
        raise HTTPException(status_code=404, detail="either chosenArtist or purposeOutline do not exist or both")



    #generate dynamic prompt, based on prompt blocks
    

   

    report_question = report_focus + f"for the artist {chosen_artist}"
    print(f"report_question is: {report_question}")

    #add as imported function here
    prompt_structure = generate_dynamic_report_prompt_structure(report_question)

    #pass down prompt structure as function param, then need to add overall_answers to prompt structure in mainFunction.py, before sending to model
    

    try:
        # Run your (blocking/async-mixed) pipeline in a thread
        result_text = await to_thread.run_sync(
            generate_report_sync_concurrent, chosen_artist, prompt_structure
        )

        # Mirror your old behavior (Node returned result.data[0]); here we just return the text.
        # If your frontend expects JSON, wrap it:
        return result_text

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate report: {e}")

if __name__ == "__server__":
    import uvicorn
    port = int(os.getenv("PORT", "3011"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

# Run: uvicorn serverConcurrent:app --host 0.0.0.0 --port 3011 --reload