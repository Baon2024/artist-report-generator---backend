import requests
from pandas import pandas as pd
import io

csv_url = "https://docs.google.com/spreadsheets/d/16laydkilMaGkpCnRaL_uC-EjW4oPghTlKKWI1E_WvXk/export?format=csv&gid=363229501"



def get_artist_stage(chartmetric_id):

    #chartmetric_id = chartmetric_id.strip()
    #print(f"chartmetric_id after stripping is: {chartmetric_id}")
    
    try:
        r = requests.get(csv_url, timeout=10)
        r.raise_for_status()
        # You can parse CSV if you like:
        rows = [line.split(",") for line in r.text.strip().splitlines()]
        print(f"rows: {rows}")

        df = pd.read_csv(io.StringIO(r.text))
    
        print(f"df is: {df}")

        for row in df:
            print(f"row is: {row}")

    
        chosen_row = df[df["Chartmetric ID"] == chartmetric_id]
        print(f"chosen_row is: {chosen_row}")
        if chosen_row.empty:
            print(f"No artist found with Chartmetric ID {chartmetric_id}")
            # Option 1: raise an error
            raise ValueError(f"No artist found with Chartmetric ID {chartmetric_id}")
        # Option 2: return None or a default
        else: 
            artist_stage = chosen_row["Stage"]
            print(f"artist_stage is: {artist_stage}")
            
            if artist_stage.empty:
                raise ValueError("artist_stage or similar_artists are empty!")

            #need to extract stage and artists from string values
            artist_stage_illoced = artist_stage.iloc[0] if not artist_stage.empty else ""
            if not artist_stage_illoced:
                print("artist_stage_illoced is empty!")
            print(f"artist_stage_illoced is: {artist_stage_illoced}")
            artist_stage_illoced = artist_stage_illoced.strip()
            print(f"artist_stage_illoced after stripping is: {artist_stage_illoced}")

            

            return artist_stage_illoced
    except Exception as e:
        print(f"error: {e}")
