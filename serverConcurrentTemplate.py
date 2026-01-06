from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Literal, Optional
from dotenv import load_dotenv
#from gradio_client import AsyncClient  # pip install gradio_client
#from helFunction import generate_report_sync
#from helFunctionConcurrent import generate_report_sync_concurrent
from anyio import to_thread  # pip install anyio
import os
from openai import OpenAI
from dynamic_prompt_structure import generate_dynamic_report_prompt_structure
from googleSheetsMain import get_credentials, get_credentials_service
from googleapiclient.discovery import build
from get_template_prompt_structure import get_template_prompt_structure
from helFunctionConcurrentTemplate import generate_report_sync_concurrent_template
from dynamic_prompt_structure import generate_dynamic_report_prompt_structure
from helFunctionConcurrent import generate_report_sync_concurrent
from get_artist_stage import get_artist_stage
from get_template_prompt_structure_latest import get_template_prompt_structure_latest
import psycopg2
from psycopg2.extras import Json
from psycopg2 import OperationalError, Error as PsycopgError
from google import genai
from google.genai import types

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)




app = FastAPI()

# Only allow your frontends
origins = [
    "http://localhost:3001",
    "https://artist-report-generator-frontend.vercel.app",
    "https://reverb.corecollectif.com",
    "https://core-collectif-web-app.vercel.app"
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



class ReportRequestLatest(BaseModel):
    chosen_artist: str
    report_focus: Literal["track_release", "album_release", "fanbase_and_growth_analysis", "catalogue_revival"] #"track_release", "album_release", "fanbase_and_growth_analysis", "catalogue_revival"
    custom_additional_request: Optional[str]
    chartmetric_id: int


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

@app.post("/reportGeneratorCustomFocus")
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
    prompt_structure_text, prompt_structure_array = get_template_prompt_structure(report_focus, chosen_artist)
    print(f"value of prompt_structure_text, prompt_structure_array: { prompt_structure_text, prompt_structure_array}")
    #relace here, with temlate logiv

    #pass down prompt structure as function param, then need to add overall_answers to prompt structure in mainFunction.py, before sending to model
    

    try:
        # Run your (blocking/async-mixed) pipeline in a thread
        result_text = await to_thread.run_sync(
            generate_report_sync_concurrent_template, chosen_artist, prompt_structure_array, prompt_structure_text
        )

        # Mirror your old behavior (Node returned result.data[0]); here we just return the text.
        # If your frontend expects JSON, wrap it:
        return result_text

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate report: {e}")
    


@app.post("/reportGeneratorLatest")#endpoint for new Reverb variant, with 4 report choices, and a custom prompt extension
async def report_generator(payload: ReportRequestLatest) -> Any:
    chosen_artist = payload.chosen_artist
    report_focus = payload.report_focus
    custom_additional_prompt = payload.custom_additional_request
    chartmetric_id = payload.chartmetric_id

    print(f"chosen_artist is: {chosen_artist}")
    print(f"report_focus is: {report_focus}")
    print(f"custom_additional_prompt is: {custom_additional_prompt}")
    print(f"chartmetric_id is: {chartmetric_id}")  

    if not chosen_artist or not report_focus:
        raise HTTPException(status_code=404, detail="either chosenArtist or purposeOutline do not exist or both")

    
    

    #first need to get artist stage
    try:
        artist_stage = get_artist_stage(chartmetric_id)
    except ValueError as e:
        print(f"artist_stage could not be found with this chartmetric_id from internal CC Google Sheet : {chartmetric_id}")
        raise HTTPException(
        status_code=404,
        detail=f"artist_stage could not be found for chartmetric_id={chartmetric_id}: {e}"
    )

    
    report_question = report_focus + f"for the artist {chosen_artist}"
    print(f"report_question is: {report_question}")

    #Need to change this to use the new, current, templates, and pass artist_stage to get right stage key
    prompt_structure_text, prompt_structure_array = get_template_prompt_structure_latest(report_focus, chosen_artist, artist_stage)
    print(f"value of prompt_structure_text, prompt_structure_array: { prompt_structure_text, prompt_structure_array}")
    #relace here, with temlate logiv

    #then pass custom prompt addition to final report generation

    #pass down prompt structure as function param, then need to add overall_answers to prompt structure in mainFunction.py, before sending to model
    
    ##commenting everything out, for new attempt

    #need to get all data from database
    # Fetch variables
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    DBNAME = os.getenv("DBNAME")

    data_for_report = None


    try:
        with psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
            ) as connection:
            with connection.cursor() as cursor:
                print("Connection successful!")
                
                ##first, use the artist_reference table to find internal artist id, using chartmetric id
                chartmetric_id_str = str(chartmetric_id)
    
                # query
                sql = """SELECT id FROM artist_reference 
                   WHERE artistid = %s AND metric = 'chartMetrics'"""
                cursor.execute(sql, (chartmetric_id_str,))
                result = cursor.fetchone()

                if result is None: ##need to handle error, and sent back to frontend, if artist cannot be found
                    raise HTTPException(
                        status_code=404,
                        detail=f"No artist_reference match for chartmetric_id={chartmetric_id}",
                    )
        
                print(f"internal_id should be: {result}")
                internal_id = (result[0])
                print(f"internal_id after str: {internal_id}")

                ## 2 - Use internal id to access artist's data for every row
                sql = """SELECT * FROM artist_metrics
                  WHERE artistsid = %s"""
                cursor.execute(sql, (internal_id,))
                artist_metrics_result = cursor.fetchall()
                print(f"artist data fetched from artist metrics: {artist_metrics_result}")

                if not artist_metrics_result:
                    raise HTTPException(
                        status_code=404,
                        detail=f"No artist_metrics for internal_id={internal_id})"
                    )

                artist_metrics = artist_metrics_result[0]

                data_for_report = f"The metrics of the artist are: {artist_metrics}"

                ## 3a - get tracks of artists
                sql = """SELECT * FROM track_reference
                  WHERE artistid = %s"""
                cursor.execute(sql, (internal_id,))
                artist_tracks_results = cursor.fetchall()

                print(f"artist_tracks are: {artist_tracks_results}")
        
                #need to handle for if there are no tracks for artist

                ## 3b - get track metrics for these tracks
                tracks_and_metrics = []

                for (isrc, track_name, internal_id, date) in artist_tracks_results:
                    print(f"track is: {isrc, track_name, internal_id, date}")

                    #use isrc to query track_metrics for track
                    sql = """SELECT * FROM track_metrics
                      WHERE isrc = %s"""
                    cursor.execute(sql, (isrc,))
            
                    track_metrics_for_track = cursor.fetchall()
                    print(f"track_metrics_for_track {track_name} are: {track_metrics_for_track}")

                    track_metrics = {
                        "track": track_name,
                        "track_metrics": track_metrics_for_track
                    }
                    tracks_and_metrics.append(track_metrics)
                    print("added track metrics and track !")
        
                print(f"value of tracks_and_metrics are: {tracks_and_metrics}")

                data_for_report += f"And these are the tracks of the artist, and their metrics: {tracks_and_metrics}"
        
                ## 4 - get social media for the artist
                sql = """SELECT * FROM social_posts
                  WHERE artist_id = %s"""
                cursor.execute(sql, (internal_id,))
                social_media_results = cursor.fetchall()

                if not social_media_results:
                    raise HTTPException(
                        status_code=404,
                        detail=f"no social_media results found for internal id {internal_id}"
                    )

                print(f"social_media_results for artist are: {social_media_results}")

                data_for_report += f"and these are the social media posts of/about the artist: {social_media_results}"
        
                #then generate report
                client = genai.Client()
        
                contents_prompt = prompt_structure_text + f"""Your sole data source should be: {data_for_report}""" + f"""The artist is: {chosen_artist}""" + f"""and the user has this additional request: {custom_additional_prompt}""" + "simply return the report, no preliminary comment."
        
                report = client.models.generate_content(
                    model="gemini-3-pro-preview",
                    contents=contents_prompt,
                )

                print(f"response from report generation is: {report.text}")
                return report.text
    
    except HTTPException:
        # Important: let your intentional HTTP errors pass through unchanged
        raise

    except OperationalError as e:
        # DB down / connection issues
        raise HTTPException(status_code=503, detail=f"Database unavailable: {e}")

    except PsycopgError as e:
        # SQL error, cursor issues, etc.
        raise HTTPException(status_code=500, detail=f"Database query failed: {e}")

    except Exception as e:
        # Truly unexpected
        raise 
    
    

if __name__ == "__server__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

# Run: uvicorn serverConcurrentTemplate:app --host 0.0.0.0 --port 3012 --reload > output.log 2>&1

#extra comment for new git add 

#use a virtual env to mangage conflict in versions
#create with, python -m venv .venv
#source .venv/Scripts/activate
#pip install -r requirements.txt
#uvicorn serverConcurrentTemplate:app --reload

#uvicorn serverConcurrentTemplate:app --host 0.0.0.0 --port 3011  > output.log 2>&1

#need to run this, to disable utf8 format issue, to you can see terminal outu at the end
#PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python -X utf8 -m uvicorn serverConcurrentTemplate:app --host 0.0.0.0 --port 3011 2>&1 | tee -a output.log
