from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)



prompt_blocks = [
    {
        "blockTitle": "Audience Age-Tier Segmentation (#9)",
        "blockContent": """
Overlay IG/TikTok age shares with Apple Music vs Spotify listener age splits (last 90 days).
Compute over/under-index vs the artist’s total by age bracket to find platform-age mismatches.
Output a table of mismatches and 3–5 recommended actions (content, playlisting, ads) per cohort.""",
        "blockTags": ["segmentation", "age-buckets", "platform-delta", "mismatch-detection"],
        "blockID": 920900001,
    },
    {
        "blockTitle": "Superfan Cohort Identification (#5)",
        "blockContent": """
Score users on recency, frequency, and value (repeat listens, saves, playlist adds, merch/ticket buys, Discord/IG engagement).
Cluster cohorts; extract common traits and channels.
Deliver cohort cards (size, behaviors, channels) and a playbook to nurture each cohort.""",
        "blockTags": ["superfans", "rfv-scoring", "cohorting", "retention"],
        "blockID": 920500002,
    },
    {
        "blockTitle": "Demographic Skew Alerts (#17)",
        "blockContent": """
Compute gender/age share by platform (Spotify, Apple, TikTok, IG) vs artist baseline.
Trigger alerts on notable skews and quantify impact.
Recommend platform-specific targeting tweaks to rebalance or exploit the skew.""",
        "blockTags": ["demographics", "skew-alerts", "gender-age", "targeting"],
        "blockID": 921700003,
    },
    {
        "blockTitle": "Geo-Hotspot Map (#4)",
        "blockContent": """
Join Shazam country/city tags with Spotify top-city streams; add regional marketing spend and YoY growth.
Filter for markets with >50% YoY growth and <10% marketing spend.
Return top 5 market cards with map pins, entry tactics, and budget suggestions.""",
        "blockTags": ["geo", "emerging-markets", "shazam+spotify", "yoy-growth"],
        "blockID": 920400004,
    },
    {
        "blockTitle": "Drop-Off Funnel Diagnostics (#10)",
        "blockContent": """
Build a listener funnel per track: first play → 30s completion → save → week-2 repeat.
Compute stage attrition and highlight stages with >40% drop.
Provide funnel charts and fixes (edits, intros, hooks, promos) by track/cluster.""",
        "blockTags": ["funnel", "attrition", "completion", "repeat-rate"],
        "blockID": 921000005,
    },
    {
        "blockTitle": "Language & Lyric Sentiment Impact (#16)",
        "blockContent": """
Tag lyrics with sentiment/mood classes and correlate with save-rate, completion, and repeat across platforms.
Flag over- and under-indexed moods.
Deliver a matrix of mood × KPI plus a creative brief on winning/losing themes.""",
        "blockTags": ["lyrics", "sentiment", "mood-performance", "save-rate"],
        "blockID": 921600006,
    },
    {
        "blockTitle": "Audience Affinity Themes (derived)",
        "blockContent": """
Extract fan affinities from bios, comments (NLP), followed pages/artists, and hashtag co-occurrence.
Topic-model themes and cross with high-engagement posts to rank.
Output top 5 themes with example posts and recommended angles.""",
        "blockTags": ["affinities", "topic-modeling", "content-themes"],
        "blockID": 929900007,
    },
    {
        "blockTitle": "Seasonality Sweet-Spots (#1)",
        "blockContent": """
Aggregate peak-day counts by month across charts and past release dates.
Compute monthly z-scores; surface months with z > +1 as best release windows.
Provide a calendar with rationale and comparable past wins.""",
        "blockTags": ["seasonality", "release-timing", "chart-peaks"],
        "blockID": 920100008,
    },
    {
        "blockTitle": "Weekend vs Weekday Dynamics (#2)",
        "blockContent": """
Compare average rank changes of Friday releases vs non-Friday, controlling for genre/playlisting.
Flag deltas >10% and quantify risk/variance.
Recommend the optimal release day with supporting evidence.""",
        "blockTags": ["release-day", "friday-effect", "rank-delta"],
        "blockID": 920200009,
    },
    {
        "blockTitle": "Release-Day Social Cadence (#13)",
        "blockContent": """
Cluster social post timestamps around release days vs D1–D7 streams.
Simulate alternative cadences to maximize first-week outcomes.
Deliver an hour-by-hour posting playbook for T-24h to T+72h per channel.""",
        "blockTags": ["social-cadence", "release-playbook", "first-week"],
        "blockID": 921300010,
    },
    {
        "blockTitle": "Catalogue Revival Candidates (#15)",
        "blockContent": """
Detect tracks older than 24 months with >+30 Shazam rank increase in the last 60 days and positive streaming trend.
Prioritize for re-promotion.
Provide a shortlist with creatives, playlist targets, and budget plans.""",
        "blockTags": ["catalogue", "revival", "shazam-spike", "re-promo"],
        "blockID": 921500011,
    },
    {
        "blockTitle": "DSP Editorial vs Algorithmic (#20)",
        "blockContent": """
Split streams by editorial vs algorithmic playlists using metadata.
Compare decay curves (D30/D60), saves, and repeats to quantify long-tail.
Recommend the optimal exposure mix and specific asks for editors/algorithmic seeding.""",
        "blockTags": ["editorial-vs-algo", "playlist-attribution", "long-tail"],
        "blockID": 922000012,
    },
    {
        "blockTitle": "Social-to-Streaming Spike Attribution (derived)",
        "blockContent": """
Align social campaign/post timestamps to streaming time series and run an event study (0–3 day window).
Attribute uplift to posts/campaigns; control for confounders where possible.
Output top converting post types and a replication checklist.""",
        "blockTags": ["attribution", "social→streams", "event-study"],
        "blockID": 929900013,
    },
    {
        "blockTitle": "Discovery-to-Streaming Lift (#3)",
        "blockContent": """
Cross-correlate Shazam peaks with Spotify rank/stream spikes using 0–7 day lags.
Compute viral conversion rates by market and track.
Map effective pathways and provide an amplification playbook.""",
        "blockTags": ["discovery", "shazam↔spotify", "conversion"],
        "blockID": 920300014,
    },
    {
        "blockTitle": "Playlist Crossover Opportunities (#7)",
        "blockContent": """
Identify playlists containing ≥2 tracks by {artist_name}; find recurring co-artists.
Build a co-appearance network and score audience overlap/fit.
Return a collaborator target list with expected uplift and intro angles.""",
        "blockTags": ["playlists", "co-occurrence", "collab-targets"],
        "blockID": 920700015,
    },
    {
        "blockTitle": "TikTok Hook Efficiency (#8)",
        "blockContent": """
Align TikTok view-spike timestamps with the first derivative of Spotify stream curves.
Compute mean uplift per 1M TikTok views by track and creative.
Summarize hook best-practices and post timing guidance.""",
        "blockTags": ["tiktok", "uplift", "hook-testing"],
        "blockID": 920800016,
    },
    {
        "blockTitle": "Tour Routing Optimizer (#11)",
        "blockContent": """
Weight cities by recent Shazam rank × Spotify listener count × ticket history.
Rank the top 15 cities for the next-year plan and propose venue tiers.
Provide a sales forecast and routing rationale.""",
        "blockTags": ["touring", "city-ranking", "routing"],
        "blockID": 921100017,
    },
    {
        "blockTitle": "Ad-Platform Allocation (#12)",
        "blockContent": """
Regress paid-social spend against incremental streams by platform/campaign.
Estimate response curves and recommend the budget split where marginal CPA is lowest.
Deliver an allocation table with ±20% budget scenarios.""",
        "blockTags": ["ads", "budget-split", "marginal-cpa"],
        "blockID": 921200018,
    },
    {
        "blockTitle": "Collaboration Influence Scoring (#19)",
        "blockContent": """
Measure first-week stream uplift for features vs solo tracks, controlling for baseline.
Rank collaborators by average uplift with confidence intervals.
Recommend high-impact partners and future feature strategy.""",
        "blockTags": ["collabs", "uplift-scoring", "features"],
        "blockID": 921900019,
    },
    {
        "blockTitle": "Top Followers & Collab Prospects (derived)",
        "blockContent": """
Aggregate follower graphs by platform; compute influence and audience overlap.
Rank prospects by reach × affinity × engagement and dedupe across platforms.
Return a contact list with suggested pitch and content angle.""",
        "blockTags": ["influencers", "prospects", "outreach"],
        "blockID": 929900020,
    },
]






def generate_dynamic_report_prompt_structure(report_question):
    
    prompt_blocks_condensed = [{ "blockTags": block["blockTags"], "blockID": block["blockID"]} for block in prompt_blocks]
    allowed_ids = [b["blockID"] for b in prompt_blocks]  
    
    message = f"""You need to generate an artist report prompt to answer this question: {report_question}. You must assemble this
    prompt by choosing the tags of the prompt blocks available, which will be used to assemble the prompt. if you want a prompt block
    based on the tag, then you must return the blockID.

    so, your output must be a JSON schema of the following: ["blockID", "blockID", ...] 
    You can return up to 15 blocks, and no less than 10. 

    {prompt_blocks_condensed}
    """

    #make LLM call to get chosen blocks back
    system_msg = (
        "You select prompt blocks by matching their tags to the user question. "
        "Return ONLY a JSON array of blockIDs (integers), 10–15 items, unique, "
        "most relevant first. No extra text."
    )
    
    user_msg = (
        "Question:\n"
        f"{report_question}\n\n"
        "Available blocks (blockID -> tags):\n"
        f"{json.dumps(prompt_blocks_condensed, ensure_ascii=False)}"
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "select_block_ids",
                "description": "Return ONLY the chosen block IDs (10–15 unique).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids": {
                            "type": "array",
                            "items": {"type": "integer", "enum": allowed_ids},
                            "minItems": 10,
                            "maxItems": 15,
                            "uniqueItems": True,
                        }
                    },
                    "required": ["ids"],
                    "additionalProperties": False,
                },
            },
        }
    ]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",  # or a compatible model you have access to
        messages=[{"role": "system", "content": system_msg},
              {"role": "user", "content": user_msg}],
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "select_block_ids"}},
        temperature=0.2,
    )

    tool_call = resp.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    selected_block_ids = args["ids"]
    print("Chosen block IDs:", selected_block_ids)


#now filter out chosen prompt block
    chosen_blocks = []
    for block in prompt_blocks:
        for id in selected_block_ids:
            if id == block["blockID"]:
                chosen_blocks.append(block["blockTitle"])
                chosen_blocks.append(block["blockContent"])

    print(f"chosen_blocks are {chosen_blocks}")

#LLM call to prettyfi the prompt, usinbg user question and chosen blocks
    system_message_prettifier = """use the provided question, and chosen prompt blocks, to generate the finished prompt.

Here's an example of styling: MEGA AUDIENCE INSIGHT & GROWTH PROMPT
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
Title + concept + rationale.

Here's a second example:

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

*Whatever structure you choose to create out of the prompt blocks, leave it unfilled for the real answers*


    """
    system_message_prettifier1 = """
Use the provided question and chosen prompt blocks to generate the finished prompt.

STYLE GUIDE (Outline-Only):
- Produce a **sectioned outline** (headings + 1–2 sentence descriptions).
- Do **NOT** include procedures, steps, algorithms, commands, or analysis verbs.
- Forbidden cue words (case-insensitive): analyze, compute, calculate, detect, measure,
  regress, estimate, cluster, cross-correlate, join, simulate, output, return, provide, deliver.
- Prefer neutral, descriptive phrasing: “Focus”, “Context”, “Emphasis”, “Signals”, “Considerations”, “Deliverables (placeholder)”.
- Leave any data-dependent content unfilled (e.g., “*TBD – requires platform data*”).

OUTPUT:
- Markdown only.
- Structure as a titled prompt with subsections. Each subsection = a block title and a short descriptive blurb.
- No numbered steps. No “how to do it”.

GOOD (outline-only):
## Geo-Hotspot Map
Focus: emerging markets and audience growth signals across cities and regions. Context includes streaming trends, discovery signals, and budget posture. *TBD – requires platform data.*

BAD (procedural):
## Geo-Hotspot Map
Join datasets A and B, filter for >50% YoY, compute z-scores, then rank top 5…

Follow the GOOD pattern.
    """



    user_messsage_prettifier = f"""user question: {report_question}. prompt blocks: {chosen_blocks} """

    resp = client.chat.completions.create(
        model="gpt-4o",  # or a compatible model you have access to
        messages=[{"role": "system", "content": system_message_prettifier1},
                  {"role": "user", "content": user_messsage_prettifier}],
        temperature=0.8,#be more creative?
    )

    answer_text = resp.choices[0].message.content
    print(answer_text)
    with open(f"generatedDynamicReportPromptStructure{report_question[:10]}.txt","w", encoding="utf-8") as file:
        file.write(answer_text)
    return answer_text


#response = generate_dynamic_report_prompt_structure("generate a report about growth markets for Bertie Blackman")

#with open("generatedDynamicReportPromptStructureTemp8Second.txt","w", encoding="utf-8") as file:
    #file.write(response)