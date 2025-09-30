#try using existing logic, but add ctx/memory that llamindex allows

#do autonomous llamagents

from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from dotenv import load_dotenv
#from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
#from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.agent.workflow import AgentWorkflow, FunctionAgent, ReActAgent #can also import ReActAgent or FunctionAgent from this 
from llama_index.core.tools import FunctionTool
from llama_index.core.workflow import Context
import os
from functools import lru_cache
import asyncio
import requests
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)
import openai
import tiktoken
import requests
import json
import gradio as gr
from openai import OpenAI 
from helper_function import generate_questions_dynamic
import os
import asyncio
import platform
from typing import List, Optional, Dict, Any, Literal

#from llama_index.llms.google_gemini import GoogleGenAI
#from google.genai import types

load_dotenv()



llm = LlamaOpenAI(
    model="gpt-4o-mini",  # or "gpt-3.5-turbo"
    api_key=os.getenv('OPENAI_API_KEY'),  # You can also set this via the OPENAI_API_KEY environment variable
    streaming=True    
)

llmHigher = LlamaOpenAI(
    model="o3",
    api_key=os.getenv('OPENAI_API_KEY'),
    streaming=True
)

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

openai.api_key = os.getenv("OPENAI_API_KEY")
#use gemini

#set api_key in .env for gemini
#llmGemini = GoogleGenAI(model="gemini-2.5-pro")

#can use search as AI
#google_search_tool = types.Tool(
    #google_search=types.GoogleSearch()
#)#should be able to pass as tool?



@lru_cache(maxsize=1)
def get_chartmetric_access_token_cached() -> str | None:
    print("🔑 Fetching new Chartmetric token")
    return get_chartmetric_access_token_with_refresh()

#@function_tool
def get_chartmetric_access_token_with_refresh() -> str or None:
    """
    Retrieves an access token from Chartmetric. You need to use this before you can use any other function involving chartmetric
    
    """
    #current_state = await ctx.get('state')


    refresh_token = 'izPNc1uMM7A13dvWGs0Gij3rfMTKV0K24ADFfcHviaOPWxc35ZsNuYqlQNb5BVyG'
  

    endpoint = 'https://api.chartmetric.com/api/token'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'refreshtoken': refresh_token
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        if not response.ok:
            raise Exception(f"Token request failed: {response.status_code} {response.reason}")
        
        data = response.json()
        print("Access token retrieved:", data.get('token'),{})

       #if "working_notes" not in current_state:
            #current_state["working_notes"] = {}
        
        access_token = data.get('token')# This is your bearer token for future API calls
        #current_state["working_notes"]["access_token"] = access_token

        #await ctx.set("state", current_state)
        return access_token

    except Exception as e:
        print("Error retrieving Chartmetric access token:", str(e))
        return None



#@function_tool
async def find_artist_id_for_artist(ctx: Context, artist_name: str) -> int:
    """
    Retrieves artist_id for the artist you want to search on the chartmetric system .

    
    """
    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of find_artist_id_for_artist is: {current_state}")
 
    access_token = get_chartmetric_access_token_cached()

    url = f'https://api.chartmetric.com/api/search?q={artist_name}&type=artists'

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    try: 
        response = requests.get(url, headers=headers)
        
        if not response.ok:
            raise Exception(f"artist_id request failed: {response.status_code} {response.reason}")

        data = response.json()
        print("Raw response data:", data)
        
        # Safely access first matched artist
        artists = data.get("obj", {}).get("artists", [])
        
        if not artists:
            print(f"No artists found matching '{artist_name}'.")
            return None
        
        artist_id = artists[0].get('id',{})

        # Update state and persist it
        if "working_notes" not in current_state:
            current_state["working_notes"] = {}

        current_state["working_notes"][f"artist_id_for_{artist_name}"] = artist_id
        await ctx.store.set("state", current_state)  # 🟢 Save the updated state
        print(f"🧠 Updated working_notes in find_artist_id_for_artist: {json.dumps(current_state['working_notes'], indent=2)}")


        return artist_id

    except Exception as e:
        print("Error retrieving Chartmetric artist_id:", str(e))
        return None

#@function_tool
async def get_similar_artists(ctx: Context, artist_id: int) -> dict:
    """
    Retrieve a list of similar artists from Chartmetric based on a given artist ID.

    Parameters:
    - artist_id (int): The Chartmetric artist ID.

    Returns:
    - dict: A dictionary of similar artists (up to 5).

    Notes:
    - Results are stored in working memory under "similar_artists".
    """
    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of get_similar_artists is: {current_state}")

    access_token = get_chartmetric_access_token_cached()  # Assuming this is defined elsewhere
    print("access_token for get_similar_artists api call obatined!")

    url = f"https://api.chartmetric.com/api/artist/{artist_id}/relatedartists?limit=3"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise Exception(f"Related artists request failed: {response.status_code} {response.reason}")

        data = response.json()
        print("data returned from get_similar_artists is:", data)

        
        similar_artists = data.get('obj', {})

        if "working_notes" not in current_state:
            current_state["working_notes"] = {}
        
        current_state["working_notes"]["similar_artists"] = similar_artists
        await ctx.store.set('state', current_state)

        return similar_artists

    except Exception as e:
        print("Error retrieving similar artists:", str(e))
        return None


async def get_youtube_audience_data(ctx: Context, artist_id: str) -> dict:
    """
    Retrieve Youtube audience data for a given artist, using Chartmetric API.

    Parameters:
    - artist_id (int): The Chartmetric artist ID.

    Returns:
    - dict: A dictionary of similar artists (up to 5).

    Notes:
    - Results are saved in working memory.
    """
    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of get_youtube_audience_data is: {current_state}")
    
    access_token = get_chartmetric_access_token_cached()


    print("🚀 Called get_Youtube with artist_id:", artist_id)
    print("🚀 Called get_Youtube with access_token:", access_token)


    url = f"https://api.chartmetric.com/api/artist/{artist_id}/youtube-audience-stats"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        if response.status_code == 404:
            print(f"⚠️ No YouTube data found for artist {artist_id}")
            return {}
        

    data = response.json()
    print(f"data from get_Youtube is: {data}")

    dataObj = data.get('obj',{})

    print("Info from get_tiktok_audience_data is:", dataObj)

    compressed_notable_followers = []
    for follower in dataObj["notable_subscribers"]:
        #pprint(f"follower in dataObj is: {follower}")

        new_data = {}
        
        new_data["custom_name"] = follower.get("custom_name", {})
        new_data["subscribers"] = follower["subscribers"] 
        new_data["engagements"] = follower["engagements"] 

        compressed_notable_followers.append(new_data)
    

    dict_to_return = {"top_countries": dataObj["top_countries"], "audience_gender_by_age": dataObj["audience_genders_per_age"], "audience_genders": dataObj["audience_genders"], "top_followers": compressed_notable_followers,
      "subscribers": dataObj["subscribers"], "avg_likes_per_post": dataObj["avg_likes_per_post"], "avg_commments_per_post": dataObj["avg_commments_per_post"],
      "engagement_rate": dataObj["engagement_rate"]
    
     }

    if "working_notes" not in current_state:
        current_state["working_notes"] = {}
    
    youtube_audience_stats = dict_to_return
    print(f"youtube_audience_stats are: {youtube_audience_stats}")
    current_state["working_notes"][f"youtube_audience_data for artist {artist_id}"] = youtube_audience_stats
    await ctx.store.set('state', current_state)

    return { f"youtube_audience_data for artist {artist_id}": youtube_audience_stats}







async def get_tiktok_audience_data(ctx: Context, artist_id: str) -> dict:
    """
    Retrieve TikTok audience data for a given artist using Chartmetric API.

    Parameters:
    - artist_id (str): The Chartmetric artist ID.

    Returns:
    - dict: TikTok audience breakdown.

    Notes:
    - Results are saved in working memory.
    """
    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of get_tiktok_audience_data is: {current_state}")

    access_token = get_chartmetric_access_token_cached()


    print("🚀 Called get_tiktok_audience_data with artist_id:", artist_id)
    print("🚀 Called get_tiktok_audience_data with access_token:", access_token)

    url = f"https://api.chartmetric.com/api/artist/{artist_id}/tiktok-audience-stats"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        raise Exception(f"API request failed: {response.status_code} {response.reason}")

    data = response.json()
    #print(f"data from get_tiktok_audience_data is: {data}")

    dataObj = data.get('obj',{})

    #print("Info from get_tiktok_audience_data is:", dataObj)

    compressed_notable_followers = []
    for follower in dataObj.get("notable_followers", []):
        #print(f"follower in dataObj is: {follower}")

        new_data = {}
        new_data["username"] = follower["username"]
        new_data["followers"] = follower["followers"] 
        new_data["engagement"] = follower["engagements"] 

        compressed_notable_followers.append(new_data)
    

    dict_to_return = {"top_countries": dataObj["top_countries"], "audience_gender_by_age": dataObj["audience_genders_per_age"], "audience_genders": dataObj["audience_genders"], "top_followers": compressed_notable_followers,
      "followers": dataObj["followers"], "avg_likes_per_post": dataObj["avg_likes_per_post"], "avg_commments_per_post": dataObj["avg_commments_per_post"],
      "engagement_rate": dataObj["engagement_rate"]
    
     }
    if "working_notes" not in current_state:
        current_state["working_notes"] = {}
    
    tiktok_audience_stats = dict_to_return
    #print(f"tiktok_audience_data are: {tiktok_audience_stats}")
    current_state["working_notes"][f"tiktok_audience_data for artist {artist_id}"] = tiktok_audience_stats
    await ctx.store.set('state', current_state)

    return { f"tiktok_audience_data for artist {artist_id}": tiktok_audience_stats}

    #choose which parts to return






#@function_tool
async def get_instagram_audience_data(ctx: Context, artist_id: str) -> dict:
    """
    Retrieve Instagram audience statistics for a given artist using Chartmetric.

    Parameters:
    - artist_id (str): The Chartmetric artist ID.

    Returns:
    - dict: Instagram audience breakdown.

    Notes:
    - Results are saved in working memory.
    """
    #perhaps just have it get access_token inside here
    #access_token = get_chartmetric_access_token_with_refresh()

    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of get_instagram_audience_stats is: {current_state}")

    access_token = get_chartmetric_access_token_cached()


    print("🚀 Called get_instagram_audience_stats with artist_id:", artist_id)
    print("🚀 Called get_instagram_audience_stats with access_token:", access_token)
    
    url = f"https://api.chartmetric.com/api/artist/{artist_id}/instagram-audience-stats"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        raise Exception(f"API request failed: {response.status_code} {response.reason}")

    data = response.json()
    #print(f"data from api call is: {data}")
    #print("Info from platform Instagram is:", data.get("obj"))
    

    if "working_notes" not in current_state:
        current_state["working_notes"] = {}
    
    instagram_audience_stats = data.get('obj', {})
    current_state["working_notes"][f"instagram_audience_data for artist {artist_id}"] = instagram_audience_stats
    await ctx.store.set('state', current_state)

    return { f"instagram_audience_data for artist {artist_id}": instagram_audience_stats}

import logging, sys
# Configure logging once, at app startup
logging.basicConfig(
    level=logging.INFO,  # can be DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]  # logs to stdout
)

logger = logging.getLogger("charts")

async def get_charts(ctx: Context, artist_id: int, chart_type: str, from_date: str, until_date: str) -> dict:
    """
    Retrieve chart data for a given artist using Chartmetric API.

    Parameters:
    - artist_id (str): The Chartmetric artist ID.
    - chart_type: The platform chart and sub-choice. Choose one from:
        [
            "spotify_viral_daily", "spotify_viral_weekly", "spotify_top_daily", "spotify_top_weekly",
            "applemusic_top", "applemusic_daily", "applemusic_albums",
            "itunes_top", "itunes_albums",
            "shazam", "beatport",
            "youtube", "youtube_tracks", "youtube_videos", "youtube_trends",
            "amazon"
        ]
    - from_date(str): the earliest date for the chart data being returned. Must be in format YYYY-MM-DD. For example, "2025-03-01"
    - until_date(str): the latest date for the data being returned. Must be in format YYYY-MM-DD. For example, "2025-03-01"

    Returns:
    - dict: Chart entries containing album name, rank, and peak info.

    Notes:
    - Results are saved in working memory.
    """

    valid_chart_types = [
    "spotify_viral_daily", "spotify_viral_weekly", "spotify_top_daily", "spotify_top_weekly",
    "applemusic_top", "applemusic_daily", "applemusic_albums",
    "itunes_top", "itunes_albums", "shazam", "beatport",
    "youtube", "youtube_tracks", "youtube_videos", "youtube_trends", "amazon"
    ]
    
    if chart_type not in valid_chart_types:
        raise ValueError(f"Invalid chart_type '{chart_type}'. Must be one of: {valid_chart_types}")

    current_state = await ctx.store.get('state')
    print(f"value of current_state on load inside of get_chart is: {current_state}")

    #https://api.chartmetric.com/api/artist/:id/:type/charts

    access_token = get_chartmetric_access_token_cached()


    print("🚀 Called get_charts with artist_id:", artist_id)
    print("🚀 Called get_charts with access_token:", access_token)

    ##shoukd make dates of the chart dynamic later
    ##need to give chart options in function description clearly


    url = f"https://api.chartmetric.com/api/artist/{artist_id}/{chart_type}/charts?since=${from_date}&until=${until_date}"
    print("🚀 dynamic data url for get charts should be:", url)

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        print(f"❌ Request failed with status {response.status_code}: {response.text}")
        return {}
        

    data = response.json()
    #print(f"data from get_charts is: {data}")
    print("🚀 data call to get_charts successfully made!")

    logger.info(f"returned stuff from get charts is {data}")

    dataObj = data.get('obj',{})
    #print(f"dataObj is {dataObj}")
    dataObjEntries = dataObj.get('data',{})
    dataObjEntries2 = dataObjEntries.get('entries',{})
    #print(f"dataObjEntries2 is {dataObjEntries2}")
    
    relevant_details = []
    for entry in dataObjEntries2:
        print(f"entry is: {entry}")
        stuffToSave = { "album": entry["name"], "pre-rank": entry["pre_rank"], "peak": entry["peak_rank"], "peak_day": entry["peak_date"], "rank": entry["rank"] }
        print(f"stuff to save is: {stuffToSave}")
        relevant_details.append(stuffToSave)
    
    print(f"value of relevant_dtails is: {relevant_details}")

    if "working_notes" not in current_state:
        current_state["working_notes"] = {}
    
    if f"charts_data for {artist_id}" not in current_state["working_notes"]:
        current_state["working_notes"][f"charts_data for {artist_id}"] = {}
    
    current_state["working_notes"][f"charts_data for {artist_id}"][chart_type] = relevant_details
    await ctx.store.set('state', current_state)

    return {
    "artist_id": artist_id,
    "chart_data": relevant_details
}

async def get_playlists(
    ctx: Context,
    artist_id: int,
    platform: Literal["spotify", "applemusic", "deezer", "amazon", "youtube"],
    status:   Literal["current", "past"],
    sort_column: Optional[str] = None,
    sort_direction: Optional[Literal["asc", "desc"]] = None,
    flags: Optional[List[str]] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Retrieve current or past playlists for an artist from Chartmetric.

    Parameters:
    - artist_id (int): Chartmetric artist ID.
    - platform (str): One of ["spotify", "applemusic", "deezer", "amazon", "youtube"].
    - status (str): "current" or "past".
    - sort_column (str, optional): Sort key; validated per platform+status combination.
      Defaults are inferred from Chartmetric docs when omitted.
    - sort_direction (str, optional): "asc" or "desc". If omitted, Chartmetric default is used.
    - flags (List[str], optional): Platform-specific filters. Valid by platform:
        spotify: ["editorial","personalized","chart","thisIs","newMusicFriday","radio",
                  "fullyPersonalized","brand","majorCurator","popularIndie","indie","audiobook"]
        applemusic: ["editorial","editorialBrand","chart","radio","musicBrand","nonMusicBrand",
                     "indie","personalityArtist"]
        deezer: ["editorial","deezerPartner","chart","hundredPercent","brand","majorCurator",
                 "popularIndie","indie"]
        amazon: [] (no flags supported)
        youtube: [] (flags unsupported by docs)
    - limit (int, optional): Pagination limit if supported by endpoint.
    - offset (int, optional): Pagination offset if supported by endpoint.

    Returns:
    - dict: {
        "artist_id": int,
        "platform": str,
        "status": str,
        "sort_column": str,
        "flags": List[str],
        "results": [ { "playlist_id": ..., "name": ..., ... }, ... ]
      }

    Notes:
    - Saves results into ctx.store["state"]["working_notes"]["playlists for <artist_id>"][f"{platform}:{status}"].
    - Requires `get_chartmetric_access_token_cached()` to be available in scope.
    """

    VALID_PLATFORMS = {"spotify","applemusic","deezer","amazon","youtube"}
    VALID_STATUS = {"current","past"}

    if platform not in VALID_PLATFORMS:
        raise ValueError(f"Invalid platform '{platform}'. Must be one of {sorted(VALID_PLATFORMS)}.")
    if status not in VALID_STATUS:
        raise ValueError(f"Invalid status '{status}'. Must be one of {sorted(VALID_STATUS)}.")

    # Allowed flags per platform (from docs)
    PLATFORM_FLAGS = {
        "spotify": {"editorial","personalized","chart","thisIs","newMusicFriday","radio",
                    "fullyPersonalized","brand","majorCurator","popularIndie","indie","audiobook"},
        "applemusic": {"editorial","editorialBrand","chart","radio","musicBrand","nonMusicBrand",
                       "indie","personalityArtist"},
        "deezer": {"editorial","deezerPartner","chart","hundredPercent","brand","majorCurator",
                   "popularIndie","indie"},
        "amazon": set(),
        "youtube": set(),  # docs list no flag parameters for YouTube
    }

    # Valid sort columns per platform+status, with defaults (from docs)
    SORT_OPTIONS = {
        ("amazon","current"): {"valid": {"added_at","countries","name","peak_position","track"},
                               "default": "added_at"},
        ("applemusic","current"): {"valid": {"added_at","name","peak_position","position","track"},
                                   "default": "added_at"},
        ("applemusic","past"): {"valid": {"added_at","name","peak_position","position","removed_at","track"},
                                "default": "removed_at"},
        ("deezer","current"): {"valid": {"added_at","fdiff_month","followers","name","peak_position","track"},
                               "default": "added_at"},
        ("deezer","past"): {"valid": {"added_at","fdiff_month","followers","name","peak_position","removed_at","track"},
                            "default": "removed_at"},
        ("spotify","current"): {"valid": {"added_at","code2","fdiff_month","followers","name","peak_position","position","track"},
                                "default": "followers"},
        ("spotify","past"): {"valid": {"added_at","code2","fdiff_month","followers","name","peak_position","position","removed_at","track"},
                             "default": "followers"},
        ("youtube","current"): {"valid": {"added_at","name","peak_position","track","vdiff_month","views"},
                                "default": "added_at"},
        ("youtube","past"): {"valid": {"added_at","name","peak_position","removed_at","track","vdiff_month","views"},
                             "default": "removed_at"},
    }

    sort_cfg = SORT_OPTIONS.get((platform, status))
    if not sort_cfg:
        raise ValueError(f"No sort configuration found for platform='{platform}', status='{status}'.")

    resolved_sort = sort_column or sort_cfg["default"]
    if resolved_sort not in sort_cfg["valid"]:
        raise ValueError(
            f"Invalid sort_column '{resolved_sort}' for {platform} {status}. "
            f"Valid: {sorted(sort_cfg['valid'])}"
        )

    # Validate flags
    flags = flags or []
    invalid_flags = [f for f in flags if f not in PLATFORM_FLAGS[platform]]
    if invalid_flags:
        raise ValueError(
            f"Invalid flags for {platform}: {invalid_flags}. "
            f"Valid flags: {sorted(PLATFORM_FLAGS[platform])}"
        )

    access_token = get_chartmetric_access_token_cached()
    print(f"🎧 get_playlists → artist_id={artist_id}, platform={platform}, status={status}, sort={resolved_sort}, flags={flags}")

    base_url = f"https://api.chartmetric.com/api/artist/{artist_id}/{platform}/{status}/playlists"

    # Build query params
    params: Dict[str, Any] = {
        "sortColumn": resolved_sort
    }
    if sort_direction in {"asc","desc"}:
        params["sortDirection"] = sort_direction

    # Flags are boolean query params when supported
    for f in flags:
        params[f] = True

    # Pagination if exposed by the endpoint (harmless if ignored)
    if isinstance(limit, int) and limit > 0:
        params["limit"] = limit
    if isinstance(offset, int) and offset >= 0:
        params["offset"] = offset

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(base_url, headers=headers, params=params)
    if not response.ok:
        print(f"❌ get_playlists failed [{response.status_code}]: {response.text}")
        return {
            "artist_id": artist_id,
            "platform": platform,
            "status": status,
            "sort_column": resolved_sort,
            "flags": flags,
            "results": [],
            "error": f"{response.status_code}: {response.text}",
        }

    data = response.json()
    items = data.get("obj", []) or []

    # Normalize results
    results = []
    for item in items:
        playlist = item.get("playlist", {}) or {}
        if not playlist:
            continue
        pid = playlist.get("playlist_id")
        if not pid:
            # no id → skip
            continue

        norm: Dict[str, Any] = {
            "playlist_id": pid,
            "name": playlist.get("name"),
            "owner": playlist.get("owner") or playlist.get("curator"),
            "followers": playlist.get("followers"),
            "position": playlist.get("position"),
            "peak_position": playlist.get("peak_position"),
            "added_at": playlist.get("added_at"),
            "removed_at": playlist.get("removed_at"),
            "track": playlist.get("track"),
            "views": playlist.get("views"),
            "countries": playlist.get("countries"),
            "code2": playlist.get("code2"),
            "url": playlist.get("url") or playlist.get("link"),
            "raw": playlist,  # keep raw in case you need platform fields
        }
        results.append({k: v for k, v in norm.items() if v is not None})

    # Save to working memory in ctx
    current_state = await ctx.store.get("state") or {}
    if "working_notes" not in current_state:
        current_state["working_notes"] = {}

    key_space = f"playlists for {artist_id}"
    if key_space not in current_state["working_notes"]:
        current_state["working_notes"][key_space] = {}

    save_key = f"{platform}:{status}"
    current_state["working_notes"][key_space][save_key] = {
        "params": {
            "sort_column": resolved_sort,
            "sort_direction": sort_direction,
            "flags": flags,
            "limit": limit,
            "offset": offset,
        },
        "results": results,
    }
    await ctx.store.set("state", current_state)

    print(f"✅ get_playlists returned {len(results)} playlists.")
    return {
        "artist_id": artist_id,
        "platform": platform,
        "status": status,
        "sort_column": resolved_sort,
        "flags": flags,
        "results": results,
    }


async def get_artist_news(
    ctx: Context,
    artist_id: int,
    *,
    limit: Optional[int] = None,          # 0–50 (Chartmetric default: 10 if omitted)
    weight: Optional[int] = None,         # 0–10 (Chartmetric default: 5 if omitted)
    min_stars: Optional[int] = None,      # convenience: 1 star == weight 2
    request_timeout: int = 20,
) -> Dict[str, Any]:
    """
    Retrieve recent news or milestone events for a given artist from the Chartmetric API.

    Parameters:
    - ctx (Context): LlamaIndex Context object for accessing persistent state (`ctx.store`).
    - artist_id (int): The Chartmetric artist ID.
    - limit (int, optional): Number of news items to return.  
      Range: 0–50 (inclusive). Default: 10 if omitted.
    - weight (int, optional): Importance/weight score for filtering news items.  
      Range: 0–10 (inclusive). Default: 5 if omitted.  
      Higher weight → more significant events.
    - min_stars (int, optional): Convenience parameter.  
      1 star = weight 2.  
      If provided and `weight` is not set, `weight` will be derived as `min_stars * 2`,  
      clamped to 0–10.
    - request_timeout (int, optional): Timeout in seconds for the API request. Default: 20.

    Returns:
    - dict: {
        "artist_id": int,
        "params": { "limit": int, "weight": int, "min_stars": int },
        "results": [
            {
                "news_id": str,
                "type": str,
                "sub_type": str,
                "formatted_date": str,
                "image_url": str,
                "stars": int,
                "summary": {
                    "template": str,
                    "data": dict
                },
                "metadata": dict,
                "raw": dict
            },
            ...
        ]
      }

    Notes:
    - Results are also saved to `ctx.store["state"]["working_notes"]["news for <artist_id>"]["latest"]`.
    - Requires `get_chartmetric_access_token_cached()` to be defined in scope.
    - If both `min_stars` and `weight` are provided, `weight` takes precedence.
    - API endpoint: `GET https://api.chartmetric.com/api/artist/{artist_id}/news`
    """

    # ----- derive weight from stars (2 weight == 1 star) -----
    if min_stars is not None and weight is None:
        try:
            ms = int(min_stars)
        except Exception:
            raise ValueError("min_stars must be an integer")
        # clamp 0..10
        weight = max(0, min(10, ms * 2))

    # ----- validate -----
    if limit is not None:
        if not isinstance(limit, int):
            raise ValueError("limit must be an integer between 0 and 50")
        if not (0 <= limit <= 50):
            raise ValueError("limit must be between 0 and 50 (inclusive)")
    if weight is not None:
        if not isinstance(weight, int):
            raise ValueError("weight must be an integer between 0 and 10")
        if not (0 <= weight <= 10):
            raise ValueError("weight must be between 0 and 10 (inclusive)")

    # ----- token -----
    try:
        access_token = get_chartmetric_access_token_cached()
        if asyncio.iscoroutine(access_token):
            access_token = await access_token
    except NameError:
        raise RuntimeError("get_chartmetric_access_token_cached() is not defined in scope.")
    except Exception as e:
        raise RuntimeError(f"Failed to obtain Chartmetric token: {e}") from e

    print(f"📰 get_artist_news → artist_id={artist_id}, limit={limit}, weight={weight} (min_stars={min_stars})")

    # ----- request -----
    base_url = f"https://api.chartmetric.com/api/artist/{artist_id}/news"
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if weight is not None:
        params["weight"] = weight

    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        resp = requests.get(base_url, headers=headers, params=params, timeout=request_timeout)
    except requests.RequestException as e:
        err = f"request_error: {e.__class__.__name__}: {e}"
        print(f"❌ get_artist_news failed [{err}]")
        return {
            "artist_id": artist_id,
            "params": {"limit": limit, "weight": weight, "min_stars": min_stars},
            "results": [],
            "error": err,
        }

    if not resp.ok:
        print(f"❌ get_artist_news failed [{resp.status_code}]: {resp.text}")
        return {
            "artist_id": artist_id,
            "params": {"limit": limit, "weight": weight, "min_stars": min_stars},
            "results": [],
            "error": f"{resp.status_code}: {resp.text}",
        }

    # ----- parse -----
    try:
        data = resp.json()
    except ValueError:
        return {
            "artist_id": artist_id,
            "params": {"limit": limit, "weight": weight, "min_stars": min_stars},
            "results": [],
            "error": "invalid_json: response was not JSON",
        }

    items = (data.get("obj") if isinstance(data, dict) else data) or []
    if not isinstance(items, list):
        items = []

    results: List[Dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        news_id = item.get("id")
        if news_id is None:
            continue

        norm = {
            "news_id": news_id,
            "type": item.get("type"),
            "sub_type": item.get("subType"),
            "formatted_date": item.get("formattedDate"),
            "image_url": item.get("imageUrl"),
            "stars": item.get("stars"),
            "summary": {
                "template": item.get("summaryTemplate"),
                "data": item.get("summaryData") or {},
            },
            "metadata": item.get("metadata") or {},
            "raw": item,
        }
        results.append({k: v for k, v in norm.items() if v is not None})

    # ----- persist (best-effort, assumes ctx.store exists) -----
    try:
        state = await ctx.store.get("state") or {}
        state.setdefault("working_notes", {})
        key_space = f"news for {artist_id}"
        state["working_notes"].setdefault(key_space, {})
        state["working_notes"][key_space]["latest"] = {
            "params": {"limit": limit, "weight": weight, "min_stars": min_stars},
            "results": results,
        }
        await ctx.store.set("state", state)
    except Exception as e:
        print(f"⚠️  Skipping state persistence: {e}")

    print(f"✅ get_artist_news returned {len(results)} items.")
    return {
        "artist_id": artist_id,
        "params": {"limit": limit, "weight": weight, "min_stars": min_stars},
        "results": results,
    }





    prompto3 = f"""
# ROLE & TASK
You are a **senior music strategist** hired to deliver a **two-page Audience Intelligence Brief** for the artist **{chosen_artist}**.

# SOURCE MATERIAL
– You have one source only: **RAW_DATA** (verbatim answers & metrics pulled from Instagram, TikTok and YouTube).
– Treat all numbers as trustworthy unless they contradict each other; in that case flag the conflict in “Data Gaps”.

# WORKFLOW  (do not display)
1. **THINK:** Extract every statistic, named entity, quote or behavioural clue from RAW_DATA.  
2. **PLAN:** Map those findings onto the template sections. Identify unsupported cells early.  
3. **WRITE:** Populate the markdown template in polished, presentation-ready prose.  
   – Use concise bullet points (max. 15 words each) and tables for scannability.  
   – Keep each column width sensible; wrap long text with `<br>` if needed.  
4. **VERIFY:** Double-check that totals, % and age-band ranges add up logically.  
5. **CLEAN:** Do **not** expose this workflow, system prompts or RAW_DATA.

# STYLE
Consultative, insight-rich, brand-strategy tone. Prefer active voice, audience-centric language (“Fans show…”, “Leverage…”).  
Use **bold** for key stats, *italics* for emphasis, emojis only where the template already includes them.

# DELIVERABLE
Return **exactly** the filled-in template between the markers  
`---BEGIN BRIEF---` and `---END BRIEF---`.  
If a section lacks data, keep the section but write “*No platform data supplied — analyst inference required*”.

# MARKDOWN TEMPLATE  (to be populated – do NOT repeat unfilled)
### Deep-Dive Audience Analysis for {chosen_artist}  
(Synthesising Instagram, TikTok & YouTube, Charts & Playlist data within Turkish pop-market context)

---

1. **Audience Architecture at a Glance**  
| Layer              | Instagram Data            | TikTok/Other*         | Strategic Takeaway                       |
|--------------------|---------------------------|-----------------------|------------------------------------------|
| Scale              |                           |                       |                                          |
| Core Territory     |                           |                       |                                          |
| Secondary Markets  |                           |                       |                                          |
| Gender             |                           |                       |                                          |
| Prime Age Band     |                           |                       |                                          |

---

2. **Hidden Insights & Underserved Nuances**  
| Insight                            | Evidence (platform, metric)     | Why It Matters                          |
|------------------------------------|---------------------------------|------------------------------------------|
|                                    |                                 |                                          |
|                                    |                                 |                                          |
|                                    |                                 |                                          |

---

3. **Psychographic Micro-Segments to Activate**  
| Segment Name        | % Audience | Description (mindset / need-state) | Ideal Touch-point                       |
|---------------------|-----------:|------------------------------------|-----------------------------------------|
|                     |            |                                    |                                         |
|                     |            |                                    |                                         |

---

4. **Content & Channel Implications**  
| Funnel Stage   | Priority Channel(s) | Format & Narrative Hook              |
|----------------|---------------------|--------------------------------------|
| Discovery      |                     |                                      |
| Consideration  |                     |                                      |
| Community      |                     |                                      |
| Conversion     |                     |                                      |

---

5. **Monetisation & Partnership Levers**  
- 
- 
- 
- 

---

6. **Risks & Mitigations**  
| Risk                                   | Potential Impact       | Mitigation Play                          |
|----------------------------------------|------------------------|------------------------------------------|
|                                        |                        |                                          |
|                                        |                        |                                          |

---

7. **Data Gaps & Next Steps**  
- 
- 
- 

---

📦 **RAW_DATA** (for internal use only – do NOT show in the brief)
{overall_answers}

---BEGIN BRIEF---
<!-- o3 starts populating here -->
---END BRIEF---
"""


#and that code which allows logging of every step of the memory/thought process

#keep teh cahce of chartmetric api, attached to function that gets api_key, which is inserted into each relevant api
#find_artist_id_for_artist_tool = FunctionTool.from_function(find_artist_id_for_artist)
#get_instagram_audience_stats_tool = FunctionTool.from_function(get_instagram_audience_stats)
#get_similar_artists = FunctionTool.from_function(get_similar_artists)


# Wrap your function
#find_artist_id_for_artist_tool = FunctionTool(fn=find_artist_id_for_artist)
#get_instagram_audience_stats_tool = FunctionTool(fn=get_instagram_audience_stats)
#get_similar_artists_tool = FunctionTool(fn=get_similar_artists)

manager_agent = ReActAgent(
    name="ManagerAgent",
    description="Manager agent decides which other agents to use, and is decision maker",
    system_prompt=(
        "You are the manager agent. You do not collect data yourself. You delegate.\n"
        "HARD ROUTING RULES (must follow exactly):\n"
        "- If the question is about social media audience data (TikTok, Instagram, YouTube) or artist news: delegate to SocialMediaDataAgent.\n"
        "- If the question is about chart positions, chart history, streaming rankings, or playlists: delegate to StreamingChartAgent.\n"
        "- If the question is about similar artists: delegate to SimilarityAgent.\n"
        "If the first delegation errors, retry the SAME agent once; if it still fails, return the error."
        "\n\nExamples:\n"
        "Q: 'What is the recent news about Kenan Doğulu?' → SocialMediaDataAgent\n"
        "Q: 'How is Kenan Doğulu doing on playlists this week?' → StreamingChartAgent\n"
        "Q: 'Give me IG/TikTok/YouTube audience for Kenan Doğulu' → SocialMediaDataAgent\n"
        "Q: 'Who is similar to Kenan Doğulu?' → SimilarityAgent\n"
    ),
    llm=llm,
    can_handoff_to=["SocialMediaDataAgent", "SimilarityAgent", "StreamingChartAgent"]
)

streaming_chart_agent = ReActAgent(
    name="StreamingChartAgent",
    description="agent to retrieve streaming chart and playlist data for the artist being researched",
    system_prompt=("You are a research agent that retrieves streaming chart and playlist data information about an artist"),
    llm=llm,
    tools=[get_charts, find_artist_id_for_artist, get_playlists],
    can_handoff_to=["ManagerAgent", "SimilarityAgent", "SocialMediaDataAgent"]
)


social_media_data_agent = ReActAgent(#try with Function Agents first, change to ReAct agents if needed/performance is poor.
    name="SocialMediaDataAgent",
    description="agent to source data about artists from social media data, using chartmetric api",
    system_prompt=(
    "You are a research agent that uses social media data to analyze artist audiences via Chartmetric.\n"
    "- Always use **both** Instagram and TikTok and Youtube data as your default behavior when analyzing artists.\n"
    "- Do NOT choose one over the other unless explicitly told to focus on one.\n"
    "- Always call 'get_instagram_audience_stats' AND 'get_tiktok_audience_data' AND 'get_youtube_audience_data' when gathering audience data.\n"
    "- Do NOT assume artist names. Only use 'find_artist_id_for_artist' with real artist names provided by the user.\n"
    "- If the user needs information about similar artists, HAND OFF to the SimilarityAgent — do NOT attempt it yourself.\n"
    "- Your tools are only for Instagram and TikTok and Youtube data.\n"
)
,
    llm=llmHigher,
    tools=[get_instagram_audience_data, find_artist_id_for_artist, get_tiktok_audience_data, get_youtube_audience_data, get_artist_news],
    can_handoff_to=["ManagerAgent", "SimilarityAgent", "StreamingChartAgent"]#allow it to handoff to all other agents
)



similarity_agent = ReActAgent(
    name="SimilarityAgent",
    description="agent to find similar artists to the artist being research, using chartmetric api",
    system_prompt=("You are a research agent that looks for similar artists to the artist you are researching, in order to understand how the artist can copy the growth of similar artists who are larger."
    "you can handoff to SocialMediaDataAgent, in order to find information about the followers of similar artists"
    ),
    llm=llm,
    tools=[get_similar_artists, find_artist_id_for_artist],
    can_handoff_to=["ManagerAgent", "SocialMediaDataAgent", "StreamingChartAgent"]
)





import asyncio
from contextlib import suppress

MAX_CONCURRENCY = 15
TASK_TIMEOUT_S = 1800

async def mainFunctionConcurrentTemplate(chosen_artist, prompt_structure_array, prompt_structure_text):
    #response = await workflow.run(user_msg="What is Bertie Blackman's Chartmetric artist ID?"
#, ctx=ctx) python llamaOaAgent.py
    #chosen_artist = "Kenan Doğulu"
    print("mainFunctionConcurrent hit!!!")

    print(f"selected_report_focus_array inside of mainFuncionConcurrent.py is: {prompt_structure_array}")
    #response = await workflow.run(user_msg="What is Bertie Blackman's Chartmetric artist ID?"
#, ctx=ctx) python llamaOaAgent.py
    #chosen_artist = "Kenan Doğulu"

    #llm call to generate dynamic questions, and prompt
    questions_to_ask = generate_questions_dynamic(chosen_artist, prompt_structure_text)

    #create clone, try instead iteratimg through each section of the prompt/purpose_outline
    #cut otu questions to ask, and just feed completed analysis for each sub-section into one final LLM call to synthesise and format
    #could even add an assessment of whether section analysis meets benhcmark, and exclude it from final report if not. 
    #and once working, reveb uo number of prompt blocks at the earlier stage. 
    
    overall_answers = ""
    overall_answers2 = {}

    all_states = {}

    sem = asyncio.Semaphore(MAX_CONCURRENCY)

    async def run_one(index: int, user_msg: str):
        print(f"starting questions {index + 1}")

        overall_answers2[index] = {"Thoughts": "", "Answer": ""}
        nonlocal overall_answers
        thoughts_chunks = []
        answer = ""

        # create/re-create workflow with new question as user_msg
        workflow = AgentWorkflow(
            agents=[similarity_agent, social_media_data_agent, manager_agent, streaming_chart_agent],
            root_agent=manager_agent.name,
            initial_state={
                "working_notes": {},
                "user question": user_msg,
                "users language": "English"
            }
        )

        # run the workflow with context
        ctx = Context(workflow)

        handler = workflow.run(user_msg=user_msg, ctx=ctx)
        current_agent = None
        current_tool_calls = ""

        async for event in handler.stream_events():
            if (
                hasattr(event, "current_agent_name")
                and event.current_agent_name != current_agent
            ):
                current_agent = event.current_agent_name
                print(f"\n{'='*50}")
                print(f"🤖 Agent: {current_agent}")
                print(f"{'='*50}\n")

            elif isinstance(event, AgentOutput):
                content = event.response.content.strip()
                print("📤 Output:", content)

                # New logic: extract Thought and Answer from any position
                clean_answer_combined = ""
                thought, answer = None, None

                if "Thought:" in content:
                    if "Answer:" in content:
                        thought = content.split("Thought:")[1].split("Answer:")[0].strip()
                    else:
                        thought = content.split("Thought:")[1].strip()
                        overall_answers2[index]["Thoughts"] += "\n" + thought
                        clean_answer_combined += f"🧠 Thought: {thought}\n"
                    if thought:
                        thoughts_chunks.append(thought)

                if "Answer:" in content:
                    answer = content.split("Answer:")[-1].strip()
                    overall_answers2[index]["Answer"] = answer
                    clean_answer_combined += f"✅ Answer: {answer}\n"

                if clean_answer_combined:
                    question_header = f"\n### Q{index + 1}: {user_msg}\n"
                    overall_answers += question_header + clean_answer_combined + "\n"

                # If either Thought or Answer was captured, append to overall_answers
                if event.tool_calls:
                    print(
                        "🛠️  Planning to use tools:",
                        [call.tool_name for call in event.tool_calls],
                    )
                elif isinstance(event, ToolCallResult):
                    print(f"🔧 Tool Result ({event.tool_name}):")
                    print(f"  Arguments: {event.tool_kwargs}")
                    print(f"  Output: {event.tool_output}")
                elif isinstance(event, ToolCall):
                    print(f"🔨 Calling Tool: {event.tool_name}")
                    print(f"  With arguments: {event.tool_kwargs}")

        state = await ctx.store.get("state")
        all_states[f"Q{index+1}"] = {
            "question": user_msg,
            "state": state
        }

        return {
            "index": index,
            "question": user_msg,
            "thoughts": "\n".join(thoughts_chunks).strip(),
            "answer": (answer or "").strip(),
            "state": state,
        }

    

    async def bounded_run(index: int, user_msg: str):
        async with sem:
            return await asyncio.wait_for(run_one(index, user_msg), timeout=TASK_TIMEOUT_S)

    # Launch all questions concurrently, but respect MAX_CONCURRENCY
    tasks = [
        asyncio.create_task(bounded_run(i, q))
        for i, q in enumerate(questions_to_ask)
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"value of tasks is: {tasks}")
        
    print(f"overall_answers is: {overall_answers}")
    print(f"overall_answers2 is: {overall_answers}")

    #final_state = await ctx.store.get("state")
        
    with open(f"ctx_memory_all_answersDynamic.json", "w") as f:
        json.dump(all_states, f, indent=2)
    
    #can then keep just the last thought of each question index

    def count_tokens(text, model="gpt-4o"):
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    
    total_tokens = count_tokens(overall_answers)
    print(f"Total tokens of overall_answers: {total_tokens}")

    
# Build a single string
    flattened = "\n\n".join(
        f"Q{idx + 1}: {qa['Thoughts']}\n{qa['Answer']}" 
        for idx, qa in overall_answers2.items()
    )

    total_tokens2 = count_tokens(flattened)
    print(f"Total tokens of overall_answers2: {total_tokens2}")

    with open(f"overall_answersGemini.txt","w", encoding="utf-8") as file:
        file.write(overall_answers)
    
    with open(f"overall_answers2Gemini.txt","w", encoding="utf-8") as file:
        json.dump(overall_answers2, file, ensure_ascii=False, indent=2)



    #now send overall_answers to LLM
   

  

    prompto3ChrisChart = f"""🎯 MEGA AUDIENCE INSIGHT & GROWTH PROMPT
Prompt Title: Deep Audience Intelligence & Growth Blueprint for [ARTIST_NAME]

System Role (Set Once):
You are a senior music data strategist trained in multi-platform audience intelligence, behavioral segmentation, and growth marketing. You operate like a hybrid of a data analyst, music marketer, and product strategist. Your job is to extract unique insights, detect overlooked opportunities, and build a data-driven growth plan for the artist based on a rich dataset of streaming, chart, and social data.

🔍 INPUT DATA:
Structured streaming data (Spotify, Apple Music, iTunes, Shazam) with rank movement, peak days, velocity, and decay.

Social media + CRM metrics (TikTok, IG, YouTube, Reels, Stories, Email, Merch, Tour Sales, etc.).

Any artist metadata you can derive (track names, album release cycles, remix info, sentiment cues, genre tags, collaborators).

🧠 TASK
Split your approach into three distinct cognitive layers, executed in sequence:

✅ LAYER 1: ANALYTICAL DEEP DIVE
Understand the data in its rawest form.

Detect patterns in streaming velocity, seasonal performance, and Shazam conversion.

Surface anomalies — outlier peaks, remix vs original inconsistencies, platform skews.

Build segmentations across:

Demographics (inferred via geo and platform)

Behavioral (engagement, replay rate, completion, skip/save behavior)

Content type affinity (e.g., club mix vs acoustic vs emotional lyrics)

Identify:

Top 3–5 most influential formats (content, platform, track type)

2–3 examples of platform crossover lags (e.g., Shazam peak → Spotify delay)

Fanbase decay curves (where and when attention drops off)

🧠 LAYER 2: STRATEGIC REASONING
Generate hypotheses and opportunity clusters.

Audience Gaps:

Where is the artist underperforming?

What similar audiences (adjacent genres, demos, cities) are reachable?

Cluster Fans into Personas based on behavior + geo:
Example labels:

“Shazam-driven club-goers in Southern Europe”

“Loyal iTunes buyers over 40 in Central Asia”

“Spotify Weekly repeaters with remix preference in Berlin”

For each persona cluster, answer:

What drives their behavior?

Where can we find more like them?

Which platform(s) matter most?

Propose 3–4 testable hypotheses about:

Timing strategies

Collaboration types

Format performance

Messaging tones (e.g. romantic, nostalgic, rebellious)

🚀 LAYER 3: GROWTH & CAMPAIGN STRATEGY
Turn intelligence into a tactical plan.

Recommend:

3 platform strategies, tailored to audience types (e.g. TikTok + Reels = Hook virality vs Apple = intimacy/purchase)

3 content types likely to resonate with segments (e.g. stripped vocals for Gen Z on IG vs remix packs for DJs)

2 partnership ideas — either influencer-led, playlist curators, or collab artists with overlapping fanbases

Suggest distribution timing:

What day, week, and month clusters have historically driven best results?

Layer this with social engagement cycles.

Design 1 bold, data-informed “Big Bet” campaign:

Could be a geo-targeted drop, genre mashup collab, remix competition, or a multi-platform narrative series.

🧪 OUTPUT FORMAT:
markdown
Copy
Edit
# Artist Audience Intelligence & Growth Blueprint: [Artist Name]

## 1. Overview
Short summary of overall patterns, growth arcs, and platform behaviors.

## 2. Key Segments
- Persona 1: “...” → Description, platforms, geo, behavior
- Persona 2: ...
- Persona 3: ...

## 3. Strategic Observations
- Opportunity gaps
- Surprising over/under performance
- Hypotheses

## 4. Marketing Recommendations
### A. Platform Strategy
[List of 3, each with logic and examples]

### B. Content Types to Emphasize
[List of 3, with reasoning per segment]

### C. Influencer/Partnership Strategy
[2 ideas with audience alignment logic]

## 5. Big Bet Growth Campaign
Title + concept + rationale

Your data is {overall_answers}
"""





    
    ##cut down Thought input, so only last one returned with Answer from


    #count tokens anyway, for later usage:
    total_tokens = count_tokens(prompt_structure_text)
    print(f"Total tokens of prompt: {total_tokens}")

    max_tokens = 16384 - total_tokens - 200
    
    final_prompt = prompt_structure_text + f"""Your sole data source should be: {overall_answers}""" + f"""The artist is: {chosen_artist}"""
    
    response = client.responses.create(
    model="o3",
    input=[
        {
            "role": "developer",
            "content": [
                {
                    "type": "input_text",
                    "text": (
                        "You are a precise music industry data analyst. "
                        "Be structured, factual, and preserve all stats given."
                    )
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": final_prompt
                }
            ]
        }
    ],
    text={
        "format": {
            "type": "text"
        }
    },
    reasoning={
        "effort": "medium",
        "summary": "auto"
    },
    tools=[],
    store=True
    )

    
    print(response.output_text)
    two_pager_document = response.output_text
    

    #Gemini version
    #enai.configure(api_key="AIzaSyBtpgpnI_kzxPfvlqoDbaYwlOPdxI89qNI")
    #model = genai.GenerativeModel("models/gemini-2.5-pro")

# Generate content
    #responseGemini = model.generate_content(f"You are a precise music industry data analyst. Be structured, factual, and preserve all stats given. use: {final_prompt}")
    #two_pager_gemini = responseGemini.text


    #print(responseGemini.text)

    
    #for question in formal_questions:
    #print(f"overall_answer2 is {overall_answers2}")

    with open(f"{chosen_artist}DynamicQuestionsOpenAI.txt","w", encoding="utf-8") as file:
        file.write(two_pager_document)
    
    return two_pager_document

if platform.system() == "Windows":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass


#if __name__ == "__main__":
    #response = asyncio.run(main())
    #then pass to llm to assemble formal response to formal questions

# FunctionAgent works for LLMs with a function calling API.
# ReActAgent works for any LLM.



#can check logs:
#async for ev in handler.stream_events():
    #if isinstance(ev, ToolCallResult):
        #print("")
        #print("Called tool: ", ev.tool_name, ev.tool_kwargs, "=>", ev.tool_output)
    #elif isinstance(ev, AgentStream):  # showing the thought process
        #print(ev.delta, end="", flush=True)

