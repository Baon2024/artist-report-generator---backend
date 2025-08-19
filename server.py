from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv
#from gradio_client import AsyncClient  # pip install gradio_client
from helFunction import generate_report_sync
from anyio import to_thread  # pip install anyio
import os
from openai import OpenAI
from dynamic_prompt_structure import generate_dynamic_report_prompt_structure

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)


load_dotenv()

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



@app.get("/health")
def health():
    return {"status": "ok"}


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
            generate_report_sync, chosen_artist, prompt_structure
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

# Run: uvicorn server:app --host 0.0.0.0 --port 3011 --reload