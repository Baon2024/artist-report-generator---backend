import express from "express"
import { Client } from "@gradio/client";
import cors from "cors"
import dotenv from 'dotenv'
import bodyParser from 'body-parser'


const app = express();
const PORT = 3011;
dotenv.config();

// Allow only frontend origin
app.use(cors({ origin: ['http://localhost:3009', 'https://artist-report-generator-frontend.vercel.app/']}));//change to whatever localhost I'm usingy
app.use(bodyParser.json());
app.use(express.json());


app.post('/reportGenerator',async (req, res) => {
  


const chosenArtist = req.body.chosenArtist
console.log("chosenArtist is: ", chosenArtist);

let purposeOutline = `Core Collectif - Audience Insight Report 

Artist name: XXXXXX
Primary location: XXXXXXXX
One liner: (e.g., “Urban TikTok Club Fans”)

Bio + what stands out:
(placeholder)


Audience Behavior & Segmentation
Audience Age‑Tier Segmentation (#9) - Overlay IG/TikTok age data on Apple vs. Spotify splits; surface platform-age mismatches signaling untapped cohorts.


Superfan Cohort Identification (#5) – Who are the superfans? What brings them together and are there similarities between them? 


Demographic Skew Alerts (#17) – Compute gender / age share per platform; are there niches that they are specifically bias towards? 


Geo‑Hotspot Map (#4) – Insight that maybe someone would not have looked at before. Join Shazam country/city tags with Spotify top-city streams; output top 5 emerging markets with >50% YoY growth but <10% marketing spend.


Drop‑Off Funnel Diagnostics (#10) –  Are there specific types of songs that they are dropping off from? Build listener funnel (first play → 30-sec completion → save → repeat week-2). Highlight stages with >40% attrition. Are there specific types of songs that they are dropping off from? 


Language & Lyric Sentiment Impact (#16) – Looking to understand how the audience reacts and engages with specific types of music Correlate positive/negative lyrical sentiment with save-rate across platforms; flag moods that are over- or under-indexed in performance.
Are there any affinities or traits of your fans that suggest you should post social media content around that theme





Content & Release Strategy
Seasonality Sweet‑Spots (#1) – Are there specific times of the month/seasons when the artist should release? Has there been releases in the past that have worked well at specific dates?
Aggregate peak‑day counts by month across charts; surface months where z‑score > +1 to identify best release windows.


Weekend vs Weekday Dynamics (#2) – Compare average rank changes of Friday released tracks vs others; flag deltas greater than 10%.


Release‑Day Social Cadence (#13) – Cluster social post timestamps around release days; suggest schedule that maximizes outcome for creating strong streaming outcomes


Catalogue Revival Candidates (#15) – Are there tracks we should be promoting again?? Detect tracks >24 months old with >30 rank increase in Shazam in past 60 days; mark for re‑promotion.


DSP Editorial vs Algorithmic (#20) – Split streams by editorial vs algorithmic playlists using metadata; quantify which drives longer-tail listening.
Have there been specific spikes in streaming that can be correlated to social media campaign/posts across any of the socials`

if (chosenArtist && purposeOutline) {

const client = await Client.connect("Baon2024/report_generator_dynamic");
const result = await client.predict("/predict", { 		
		chosen_artist: chosenArtist, 		
		purpose_outline: purposeOutline, 
});

console.log(result.data);

res.status(200).json(result.data[0])
} else {
    console.log("either chosenArtist or purposeOutline do not exist or both")
    res.status(404).send("either chosenArtist or purposeOutline do not exist or both")
}

})

app.listen(PORT, console.log(`server is running locally on port ${PORT}`));