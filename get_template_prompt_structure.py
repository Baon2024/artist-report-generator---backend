


def get_template_prompt_structure(report_focus, chosen_artist):
    print(f"report_focus inside of get_template_prompt_structure is: {report_focus}")

    
    report_templates = {}

    bedroom_artist_text = f"""
# ROLE & TASK
You are a **senior music strategist** hired to deliver a **two-page report for bedroom-artist stage artists** for the artist **{chosen_artist}**.

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
If a section lacks data, keep the section but write “*No platform data available*”.


**You should use the following template**

🎶 Audience Insight Report – Template

Artist  
- **Name:**  
- **Primary location:** → global touring base  
- **One-liner fan archetype:**  

---

Bio & What Stands Out  
- Bullet point 1  
- Bullet point 2  
- Bullet point 3  

---

Audience Behaviour & Segmentation  

Age-Tier Segmentation  
| Age-band | TikTok | Instagram | Spotify | Apple Music |
|----------|--------|-----------|---------|-------------|
| 13-17    | %      | %         | %       | %           |
| 18-24    | %      | %         | %       | %           |
| 25-34    | %      | %         | %       | %           |
| 35-44    | %      | %         | %       | %           |
| 45+      | %      | %         | %       | %           |

Insight:  
- Key mismatch or opportunity  

Action: 
- Tactical recommendation  

---

Superfan Cohort Identification  
- Method: (e.g., top 10% repeat listeners + merch purchasers)  
- Traits: demographics, geo, behaviours, affinities  
- Unifier: psychographic summary  

---

Demographic Skew Alerts  
- Spotify: % male / % female  
- TikTok: % male / % female  
- Instagram: % male / % female  

**Alert:** highlight notable skews + recommended action  

---

Geo-Hotspot Map – “Emerging >50 % YoY, Marketing <10 %”  

| Rank | Market (city, country) | YoY stream growth | Share of marketing spend |
|------|------------------------|-------------------|---------------------------|
| 1    | City, Country          | +%                | %                         |
| 2    | City, Country          | +%                | %                         |

Implication: recommended reallocation or focus  

---

Drop-Off Funnel Diagnostics (Spotify global, last 12 mo.)  

| Stage                | Avg % Remaining | Drop % |
|-----------------------|-----------------|--------|
| First play → 30s      | %               | %      |
| 30s → Save            | %               | % ⚠    |
| Save → Week-2 repeat  | %               | % ⚠    |

High attrition tracks: list examples  
Low attrition tracks: list examples  

---

Proven Growth strategies of similar artists
- examine the strategies used by artists with similar chartmetric scores, or more established artists in the same playlists (if any)
- highlight any successful strategies, and explain how the artist {chosen_artist} could implement them




Language & Lyric Sentiment Impact  
- Summary of sentiment effects on saves/streams  
- Non-music affinities (e.g., surf/skate, retro horror, gear content)  



Content & Release Strategy  

Seasonality Sweet-Spots  
- Peak months & rationale  

Weekend vs Weekday Dynamics  
- Performance breakdown  

Release-Day Social Cadence  
- T-3d: …  
- T-2d: …  
- T-1d: …  
- Release day: …  
- Post-day +1: …  

Catalogue Revival Candidates  
1. Song – metric (+XX ranks / sync / trend)  
2. Song – metric (+XX ranks / sync / trend)  

DSP Editorial vs Algorithmic Share  
- Editorial % | Algorithmic % | Organic %  
- Implications for marketing allocation  



Key Recommendations – 90-Day Action Plan  
1. Action #1  
2. Action #2  
3. Action #3  
4. Action #4  
5. Action #5  

"""
    bedroom_artist_array = [
        "## Artist  \n- **Name:**  \n- **Primary location:** → global touring base  \n- **One-liner fan archetype:**",

        "## Bio & What Stands Out  \n- Bullet point 1  \n- Bullet point 2  \n- Bullet point 3",

        "## Audience Behaviour & Segmentation  \n\n### Age-Tier Segmentation  \n| Age-band | TikTok | Instagram | Spotify | Apple Music |  \n|----------|--------|-----------|---------|-------------|  \n| 13-17    | %      | %         | %       | %           |  \n| 18-24    | %      | %         | %       | %           |  \n| 25-34    | %      | %         | %       | %           |  \n| 35-44    | %      | %         | %       | %           |  \n| 45+      | %      | %         | %       | %           |  \n\n**Insight:**  \n- Key mismatch or opportunity  \n\n**Action:**  \n- Tactical recommendation",

        "## Superfan Cohort Identification  \n- **Method:** (e.g., top 10% repeat listeners + merch purchasers)  \n- **Traits:** demographics, geo, behaviours, affinities  \n- **Unifier:** psychographic summary",

        "## Demographic Skew Alerts  \n- **Spotify:** % male / % female  \n- **TikTok:** % male / % female  \n- **Instagram:** % male / % female  \n\n**Alert:** highlight notable skews + recommended action",

        "## Geo-Hotspot Map – “Emerging >50 % YoY, Marketing <10 %”  \n\n| Rank | Market (city, country) | YoY stream growth | Share of marketing spend |  \n|------|------------------------|-------------------|---------------------------|  \n| 1    | City, Country          | +%                | %                         |  \n| 2    | City, Country          | +%                | %                         |  \n\n**Implication:** recommended reallocation or focus",

        "## Drop-Off Funnel Diagnostics (Spotify global, last 12 mo.)  \n\n| Stage                | Avg % Remaining | Drop % |  \n|-----------------------|-----------------|--------|  \n| First play → 30s      | %               | %      |  \n| 30s → Save            | %               | % ⚠    |  \n| Save → Week-2 repeat  | %               | % ⚠    |  \n\n**High attrition tracks:** list examples  \n**Low attrition tracks:** list examples",

        f"## Proven Growth strategies of similar artists  \n- examine the strategies used by artists with similar chartmetric scores, or more established artists in the same playlists (if any)  \n- highlight any successful strategies, and explain how the artist {chosen_artist} could implement them",

        "## Language & Lyric Sentiment Impact  \n- Summary of sentiment effects on saves/streams  \n- Non-music affinities (e.g., surf/skate, retro horror, gear content)",

        "## Content & Release Strategy  \n\n### Seasonality Sweet-Spots  \n- Peak months & rationale  \n\n### Weekend vs Weekday Dynamics  \n- Performance breakdown  \n\n### Release-Day Social Cadence  \n- T-3d: …  \n- T-2d: …  \n- T-1d: …  \n- Release day: …  \n- Post-day +1: …  \n\n### Catalogue Revival Candidates  \n1. Song – metric (+XX ranks / sync / trend)  \n2. Song – metric (+XX ranks / sync / trend)  \n\n### DSP Editorial vs Algorithmic Share  \n- Editorial % | Algorithmic % | Organic %  \n- Implications for marketing allocation"
        ]
    
    Album_Preparation_text = """1.  Artist X has an album coming out in Y period of time.  Based on their previous releases, please give an overview of their current audience and use this to tell us how to launch a new project.

1) Key highlights
Audience size today (cross-platform).
Momentum: growth % in last 28 days vs prior 28 or any similar period
Top growth region.


3 recommended next steps for release week.
2) Current audience snapshot
Platform mix: share of fans/listeners across Spotify, YouTube, TikTok, Instagram.
Demographics: age, gender, language.
Top countries & cities: rank + share shift since last release.
Similar artist overlap: top 3–5 with strongest crossover.
Recommend where to focus marketing, touring, and content in text format
3) Momentum & timing
Velocity curve or flagging: follower, listener, view counts over 90 → 30 → 7 days. Should be able to show momentum if possible (or lack thereof)
Discovery spikes: big jumps in social/streaming metrics linked to events (collabs, virality, press).
Conversion check: does social growth translate to streams?

Make a recommendation on whether to advance or hold release based on audience energy. If hold, then suggest when is optimal 
4) Historical release performance
Lift curves: streams & follower changes from T-7 to T+28 after each release.
Geo breakouts: which countries/cities moved most after prior drops.
Format comparison: singles vs features vs remixes.
Make a recommendation based on what worked, avoiding anything that has underperformed in the past. 
5) Audience development plan
Market heatmap: top 10 countries/cities for ROI. This can be a list for now. 
Creator influence: TikTok/YouTube creator groups that correlate with past spikes.
Budget split: guidance by platform & geography.
Give a recommendation of where to direct ad spend & organic pushes to the most effective markets.
6) Collab & content angles
Similar-artists overlap to provide a potential collab list.
Content post-mortem: which past formats (shorts, dance trends, live clips) correlated with surges in streaming/following
Packaging ideas: alt versions, local remixes, feature drops aligned to geo hot spots.
Recommendations on what type of content or collaborations might be optimal prior to launch.
7) Kpi targets & alerts
Give a templated targets for T-7, T-0, T+7, T+28 (pre-saves, followers, listeners, saves/stream) so that the artist can track against this 
Alert on trigger thresholds (e.g., “if pre-saves <30% of target by T-3 then boost ads”).

Everyone on the artist team then knows what “success” looks like and they can use this as a blueprint."""



    Album_Preparation_array = [

    f"## Project Context  \n- Artist **{chosen_artist}** has an album in Y period of time  \n- Objective: audience overview + launch plan",

    "## 1) Key highlights  \n- **Audience size (cross-platform):** …  \n- **Momentum (28d vs prior 28d):** …  \n- **Top growth region:** …  \n\n**Release week – 3 next steps**  \n1. …  \n2. …  \n3. …",

    "## 2) Current audience snapshot  \n- **Platform mix:** Spotify % | YouTube % | TikTok % | Instagram %  \n- **Demographics:** age %, gender split, primary languages  \n- **Top countries & cities:** rank + share shift since last release  \n- **Similar artist overlap:** top 3–5 with strongest crossover  \n\n**Focus recommendations**  \n- Marketing: …  \n- Touring: …  \n- Content: …",

    "## 3) Momentum & timing  \n- **Velocity (90→30→7d):** followers, listeners, views  \n- **Discovery spikes:** collabs / virality / press (with dates)  \n- **Conversion check:** does social growth → streams?  \n\n**Go/No-Go**  \n- Recommendation: advance or hold  \n- If hold: suggested optimal timing + rationale",

    "## 4) Historical release performance  \n- **Lift curves:** T-7 → T+28 (streams, followers)  \n- **Geo breakouts:** top movers post-drop  \n- **Format comparison:** singles vs features vs remixes  \n\n**What to repeat / avoid**  \n- Double-down: …  \n- Avoid: …",

    "## 5) Audience development plan  \n- **Market heatmap (ROI):** top 10 countries/cities (list)  \n- **Creator influence:** TikTok/YouTube groups driving past spikes  \n- **Budget split guidance:** by platform & geography  \n\n**Spend & organic plan**  \n- Ads: …  \n- Organic pushes: …",

    "## 6) Collab & content angles  \n- **Collab list:** based on overlap & playlist adjacency  \n- **Content post-mortem:** formats that correlated with surges  \n- **Packaging ideas:** alt versions, local remixes, feature drops  \n\n**Pre-launch content plan**  \n- …",

    "## 7) KPI targets & alerts  \n- **Targets:**  \n  - T-7: pre-saves … / followers … / listeners … / saves/stream …  \n  - T-0: …  \n  - T+7: …  \n  - T+28: …  \n- **Alerts:**  \n  - If pre-saves <30% of target by T-3 → boost ads  \n  - If saves/stream <X by T+3 → adjust creative / targeting  \n\n**Success blueprint:** share with full team"
    ]


    Maintain_Audience_Engagement_text = """

How can artist X keep their audience engaged in between album projects.
1) Key highlights
Current audience retention signals (followers vs. monthly listeners, unsub rates).
Engagement hotspots: platforms or geographies with most consistent activity.
3 actionable strategies to maintain momentum in downtime.
2) Audience activity snapshot
Breakdown of daily/weekly engagement patterns on streaming platforms, YouTube, TikTok, and Instagram.
Geo split of the most “sticky” audiences (who keep streaming older catalog).
Demographic slices that over-index on long-tail engagement (where fans continue to interact with old catalogue long after the release time has passed)
Recommendation of where to double down on content even without new releases (so old catalogue)
3) Catalog consumption analysis

Streams of back/old catalog over last 90 days (growth vs. decay curves).
Find “sticky tracks” , so older songs that still attract new listeners.
Cross-platform catalog depth (are fans listening past top 3 tracks?).


Recommendation to possibly start a marketing campaigns around the evergreen songs to ensure those fans are repeatedly switched on 
4) Content cadence plan
Content types with proven impact (short-form, behind-the-scenes, remixes, live versions). Will need to look at results from old content. 
Suggested cadence (e.g., 2 TikToks per week, 1 YouTube long-form per month). 
Seasonal/holiday tie-ins to keep relevance so will need to look at current date and cross reference with an notable dates coming up.
Make a recommendation on how to use different content pieces based on previous performance to keep fans engaged. 
5) Collaboration & feature strategy
Identify other emerging artists with overlapping audiences. If the artist is mature this also works for revival and to access new audiences. 
Suggest features, remixes, or joint content between projects.
The idea is to leverage collabs to unlock more audiences when no new album cycle is active.
6) KPIs that could be tracks

Monthly listeners: Are they staying within 70–80% of album-cycle peak?
Follower growth (Spotify, Instagram, TikTok): Is it still positive each month?
Top countries: Are the top 3 markets holding steady in streams?
Catalog activity: Share of streams from older songs (signals lasting interest).
It is recommended to look out for:
Sharp drop in monthly listeners (e.g., >20% decline in 30 days).
Flatlining follower growth for 2+ months in a row.
New markets not emerging (audience growth stuck in the same countries).
One song dominates too much (>60% of total streams from one track)

"""

    Maintain_Audience_Engagement_array = [
    "## Project Question  \n- How can artist X keep their audience engaged between album projects?  \n- Goal: maintain momentum during downtime",

    "## 1) Key highlights  \n- **Retention signals:** followers vs monthly listeners, unsub rates  \n- **Engagement hotspots:** platforms/geos with consistent activity  \n\n**3 actionable strategies**  \n1. …  \n2. …  \n3. …",

    "## 2) Audience activity snapshot  \n- **Daily/weekly patterns:** streaming, YouTube, TikTok, Instagram  \n- **Sticky geos:** audiences who keep streaming older catalog  \n- **Demographics:** segments that over-index on long-tail engagement  \n\n**Where to double down (no new releases):**  \n- Old-catalog content priorities and channels",

    "## 3) Catalog consumption analysis  \n- **Back-catalog streams (90d):** growth vs decay curves  \n- **Sticky tracks:** older songs still attracting new listeners  \n- **Catalog depth:** listening beyond top 3 tracks  \n\n**Evergreen campaign rec**  \n- Marketing around enduring songs to re-activate fans",

    "## 4) Content cadence plan  \n- **Proven formats:** short-form, BTS, remixes, live versions  \n- **Suggested cadence:** e.g., 2 TikToks/week, 1 YouTube long-form/month  \n- **Seasonal/holiday tie-ins:** align with notable dates  \n\n**How to use pieces:**  \n- Map formats to channels based on past performance",

    "## 5) Collaboration & feature strategy  \n- **Overlap targets:** emerging or mature artists with shared audiences  \n- **Tactics:** features, remixes, joint content between projects  \n- **Outcome:** unlock new audiences without a full album cycle",

    "## 6) KPIs to track  \n- **Monthly listeners:** 70–80% of album-peak as a hold target  \n- **Follower growth:** Spotify/IG/TikTok positive each month  \n- **Top countries:** top 3 markets steady in streams  \n- **Catalog activity:** share from older songs indicates lasting interest  \n\n**Watch-outs (alerts):**  \n- >20% ML drop in 30 days  \n- Flat follower growth for 2+ months  \n- No new markets emerging  \n- One track >60% of total streams"
 ] 

    Revive_Catalogue_text = """Artist X is not releasing new material but would like to revive their catalogue.  How and when is the best way to do this? 
1) Key highlights
Current catalog strength: % of streams from older tracks
Evergreen songs: top 2–3 tracks that consistently perform.
Recommendation: the 3 most effective levers to revive catalog (e.g., remix, content push, seasonal campaign).
2) Current catalog snapshot
What % of total streams come from tracks more than 1 year old.
And then top performing older tracks ranked by monthly listeners and streams if possible
Which countries still stream catalog heavily can show us which geos to look at.
Audience overlap where similar artists whose audiences cross with catalog listeners (good collab/remix targets).


3) Timing & seasonality
Were there any historical spikes or events/moments when songs saw bumps (e.g., TikTok trend, holiday playlisting, sync placement).
Seasonal trends: which months or periods catalog tracks perform best (holidays, summer, anniversaries).
Recommendation of optimal windows to launch catalog revival campaigns.How do they stay relevant.


4) Suggestions of catalogue revival methods
Identify older tracks with collab potential (similar-artist overlap). This might provide an opportunity for a remix or cover. Acoustic/stripped versions, localized remixes for top markets.
Content strategy: TikTok/shorts challenges, live performance clips, anniversary campaigns.
Catalog bundling: curated “best of” playlists to promote across different platforms.


Make a recommendation based on the best fit of what the artist could do to revive previous music. 
5) Audience development suggestions based on existing data
Idenitfy where catalog activity is strongest today to give us a market heatmap 
Are there TikTok/YouTube creators who previously pushed catalog tracks that we can reach back out to and unlock. 
6) Engagement kpis & things to watch out for

KPIs to track:

Catalogue streams trend: total streams of tracks more than 12 months old (should be flat or rising month-on-month during campaign). If you are reviving a track from within 12 months, data might not be.
Individually track monthly listeners to see which top songs respond best to marketing pushes
New vs returning listeners: ratio for catalog tracks (spikes in new listeners means that catalogue is reaching fresh audiences).
Social correlation: follower growth on TikTok/Instagram during catalog campaigns vs what it was prior to the campaign.

Red flags:

No uplift after campaign push: catalog streams stay flat for 2-4 weeks post campaign. This might mean the wrong tactic, content or even wrong track.
Concentration risk: one track accounts for more than 70% of catalog streams means fragile catalog strategy.
Geographical markets where catalogue is being pushed don’t align with top streaming regions which may present a geo mismatch.
"""
    Revive_Catalogue_array = [
    "## Project Question  \n- Artist X is not releasing new material but wants to **revive their catalogue**  \n- Goal: identify how and when to do it effectively",

    "## 1) Key highlights  \n- **Current catalog strength:** % of streams from older tracks  \n- **Evergreen songs:** top 2–3 consistently performing tracks  \n\n**3 most effective levers**  \n1. Remix  \n2. Content push  \n3. Seasonal campaign",

    "## 2) Current catalog snapshot  \n- **% of total streams:** from tracks >1 year old  \n- **Top older tracks:** ranked by monthly listeners & streams  \n- **Key markets:** countries still streaming catalog heavily  \n- **Audience overlap:** similar artists whose listeners cross over (remix/collab targets)",

    "## 3) Timing & seasonality  \n- **Historical spikes:** TikTok trends, syncs, holiday playlisting, anniversaries  \n- **Seasonal patterns:** months/periods catalog performs best  \n\n**Optimal windows:**  \n- Recommended campaign periods & how to stay relevant",

    "## 4) Catalogue revival methods  \n- **Collab potential:** older tracks suited for remixes or covers  \n- **Content strategy:** TikTok challenges, live clips, anniversaries  \n- **Bundling:** curated 'Best Of' playlists across platforms  \n\n**Recommendation:** most suitable revival approach for the artist",

    "## 5) Audience development suggestions  \n- **Market heatmap:** where catalog activity is strongest  \n- **Creator unlock:** TikTok/YouTube creators who boosted catalog before and could again",

    "## 6) Engagement KPIs & watch-outs  \n- **KPIs:**  \n  - Catalog streams trend (flat or rising MoM)  \n  - Monthly listeners response to pushes  \n  - New vs returning listeners ratio  \n  - Social correlation: TikTok/Instagram growth during campaigns  \n\n**Red flags:**  \n- No uplift 2–4 weeks post-campaign  \n- One track >70% of catalog streams  \n- Geo mismatch between push and top streaming regions"
]

    Fanbase_Analysis_text = """Artist X fanbase analysis: where they are, how to reach them, and how to grow
1) Key highlights
Fanbase size across platforms (Spotify, YouTube, TikTok, Instagram)
Primary online hub (platform with largest share of active audience)
A priority actions directly tied to the strongest/weakest data signals.


2) Fanbase snapshot
Cross-platform audience size such as total followers, listeners, subscribers.
Demographics - age, gender, language of the fanbase.
Top geographies - countries and cities with the most listeners.
Growth trend: change in fanbase size over the last 90 days.


Recommendations could look like:
If one age or language group dominates then can tailor creative and messaging for that demographic.
If growth is concentrated in a few countries then can direct content and ad spend specifically to those markets.


3) Where they live online
What is the mix of audience across Spotify, YouTube, TikTok, Instagram as a percentage share 
How deeply fans interact on each platform as an engagement strength out of 10
Weaker platforms: where growth is slower compared to others. This could tell us where to avoid or stop wasting resources.


Recommend based on data. For example, if Spotify listeners are rising but TikTok followers are flat then can repurpose Spotify highlights into TikTok content.
If YouTube subscribers are growing faster than Spotify listeners, can focus on video drops and use them to drive streaming traffic.


4) How to reach and activate
Content drivers: formats that historically triggered spikes in engagement.
Influencers or creators: individuals who have boosted the artist’s reach in the past.


Recommendation:
If short-form clips correlated with catalog spikes then suggest and commit to a weekly posting schedule similar. 
If a creator collaboration drove noticeable growth then suggest a repeat or scale that partnership with more collabs. 
5. Fanbase growth plan
Geographic opportunities such as emerging countries or cities where engagement is accelerating.
Platform opportunities: underdeveloped channels compared to similar artists.
Collaboration opportunities: artists with overlapping audiences.


If a new country is seeing spikes and breaking into top 10 geographies then launch targeted campaigns in that region.
If there are other artists outperforming on a specific platform then can adapt content formats from those peers.
Audience overlap is strong with another artist, can propose a joint release or content drop. But crossreference to see if they have already done one in the past. 


6) Kpis & watchpoints
KPIs:
Monthly fanbase growth across each platform.
Engagement ratio (saves per stream, likes per view).
Watchpoints:
If monthly growth falls below target, trigger a content or influencer push.
If engagement ratios drop below baseline, test new content formats.
If catalog share declines sharply, refresh older songs with new content hooks.
"""
    Fanbase_Analysis_array = [
    "## Project Question  \n- Artist X fanbase analysis: where they are, how to reach them, and how to grow  \n- Goal: understand audience distribution and growth levers",

    "## 1) Key highlights  \n- **Fanbase size:** cross-platform totals (Spotify, YouTube, TikTok, Instagram)  \n- **Primary hub:** platform with largest active share  \n\n**Priority actions:** based on strongest and weakest signals",

    "## 2) Fanbase snapshot  \n- **Cross-platform size:** total followers, listeners, subscribers  \n- **Demographics:** age, gender, language  \n- **Top geographies:** leading countries and cities  \n- **Growth trend:** 90-day audience change  \n\n**Recommendations:**  \n- Tailor creative if one demo dominates  \n- Target ad spend where growth is concentrated",

    "## 3) Where they live online  \n- **Platform mix:** % audience across Spotify, YouTube, TikTok, Instagram  \n- **Engagement strength:** 1–10 score per platform  \n- **Weaker platforms:** where growth lags  \n\n**Recommendations:**  \n- Repurpose high-performing platform content to weaker ones  \n- Double down on fast-growing channels",

    "## 4) How to reach and activate  \n- **Content drivers:** formats linked to engagement spikes  \n- **Influencers/creators:** individuals who boosted reach before  \n\n**Recommendations:**  \n- Weekly posting if short-form boosted catalog  \n- Repeat or scale creator collabs that worked",

    "## 5) Fanbase growth plan  \n- **Geo opportunities:** emerging markets with accelerating engagement  \n- **Platform opportunities:** underdeveloped channels vs peers  \n- **Collaboration opportunities:** overlapping-audience artists  \n\n**Recommendations:**  \n- Targeted campaigns in new growth regions  \n- Adapt formats from outperforming artists  \n- Propose joint content or releases",

    "## 6) KPIs & watchpoints  \n- **KPIs:**  \n  - Monthly fanbase growth by platform  \n  - Engagement ratio (saves per stream, likes per view)  \n\n**Watchpoints:**  \n- Trigger content/influencer push if growth dips  \n- Test new formats if engagement drops  \n- Refresh catalog content if share declines sharply"
]

    Grow_Fanbase_text = """How can artist X engage, activate and grow their existing fanbase over the next Y period of time?
1) Key highlights
Current fanbase size and how it has grown or declined in recent months.
The strongest platform and geography right now.
2-3 clear actions to focus on for the next Y period.
2) Fanbase snapshot
Total audience across streaming platforms and social channels.
Top countries, cities, and demographics.
Fanbase growth trend over the past 90 days.


Recommendation:
If the data shows most of your growth is coming from a particular country or age group, you should focus your content and ad spend there first rather than spreading your efforts too thin.
3) Engagement status
Current activity levels: how often fans listen, save, or engage with content.
Which platforms show the highest engagement per fan.
Recommendation
If Spotify listeners are streaming your songs multiple times but TikTok engagement is weak, should make Spotify the centerpiece of campaigns and use TikTok mainly to repurpose content rather than expecting organic growth there.
4) Activation levers
The types of content that have historically driven spikes (clips, live versions, behind-the-scenes).
Past collaborations or creator pushes that resulted in measurable lifts
Recommendation:
If the data shows that short-form videos consistently trigger jumps in streaming, commit to releasing a steady flow of these each week. Where a specific creator has been linked to past spikes, you should re-engage them or find similar profiles to collaborate with. If email or community channels show high open rates, use them for exclusive content drops to keep your core fans engaged.
5) Growth opportunities
New geographies where engagement is rising.
Platforms where Artist X is underperforming compared to peers.
Audience overlap with other artists.


Recommendation:
If you see that Brazil has entered your top 10 streaming countries for the first time, launch a targeted campaign there with tailored content or ads. If you notice peers growing much faster on TikTok, analyze their formats and test similar ones with your audience. If the overlap data highlights another artist with strong crossover, you should plan a joint remix, feature, or co-branded content drop.
6) Kpis & watchpoints
KPIs:
Net fanbase growth across each platform during the Y period.
Engagement ratios such as saves per stream or likes per view.
Number of new geographies entering the top 5 fanbase list* 


Watchpoints:
If your monthly growth falls below 2%, you should trigger a creator campaign or paid boost. If engagement ratios fall below your baseline, it’s time to test a different content style. If no new countries or cities appear in your top 5 during the Y period, it suggests your growth is too concentrated and you should revisit your collaboration or geo-targeting strategy.
"""

    Grow_Fanbase_array = [
    "## Project Question  \n- How can artist X engage, activate, and grow their existing fanbase over the next Y period?  \n- Goal: strengthen fan relationships and expand reach in a targeted window",

    "## 1) Key highlights  \n- **Current fanbase size:** and trend over recent months  \n- **Strongest platform & geography:** right now  \n\n**2–3 key actions:**  \n1. …  \n2. …  \n3. …",

    "## 2) Fanbase snapshot  \n- **Total audience:** across streaming platforms and social channels  \n- **Top geographies:** countries, cities, demographics  \n- **Growth trend:** past 90 days  \n\n**Recommendation:**  \n- Focus content/ad spend on dominant countries or age groups rather than spreading too thin",

    "## 3) Engagement status  \n- **Activity levels:** listening frequency, saves, content engagement  \n- **Top platforms:** highest engagement per fan  \n\n**Recommendation:**  \n- If Spotify engagement is strong but TikTok is weak, center campaigns on Spotify and repurpose for TikTok",

    "## 4) Activation levers  \n- **Proven content types:** clips, live versions, BTS  \n- **Past collaboration/creator lifts:** measurable results  \n\n**Recommendation:**  \n- Commit to weekly short-form if it drives spikes  \n- Re-engage high-impact creators or find similar profiles  \n- Use email/community for exclusive drops if open rates are high",

    "## 5) Growth opportunities  \n- **New geographies:** where engagement is rising  \n- **Platform gaps:** underperformance vs peers  \n- **Audience overlaps:** with other artists  \n\n**Recommendation:**  \n- Launch targeted campaigns in new top markets  \n- Test content formats from outperforming peers  \n- Plan remixes, features, or co-branded drops with strong crossover artists",

    "## 6) KPIs & watchpoints  \n- **KPIs:**  \n  - Net fanbase growth per platform (Y period)  \n  - Engagement ratios (saves/stream, likes/view)  \n  - New geographies entering top 5  \n\n**Watchpoints:**  \n- Trigger creator campaign if growth <2%  \n- Test new content if engagement drops  \n- Revisit strategy if no new countries enter top 5"
]


    #report_templates['bedroom artist'] = bedroom_artist_text
    report_templates['bedroom artist'] = { "bedroom artist_text": bedroom_artist_text, "bedroom artist_array": bedroom_artist_array }
    report_templates['Album Preparation'] = { "Album Preparation_text": Album_Preparation_text, "Album Preparation_array": Album_Preparation_array }
    report_templates['Maintain Audience Engagement'] = { "Maintain Audience Engagement_text": Maintain_Audience_Engagement_text, "Maintain Audience Engagement_array": Maintain_Audience_Engagement_array }
    report_templates['Revive Catalogue'] = { "Revive Catalogue_text": Revive_Catalogue_text, "Revive Catalogue_array": Revive_Catalogue_array }
    report_templates['Fanbase Analysis'] = { "Fanbase Analysis_text": Fanbase_Analysis_text, "Fanbase Analysis_array": Fanbase_Analysis_array }
    report_templates['Grow Fanbase'] = { "Grow Fanbase_text": Grow_Fanbase_text, "Grow Fanbase_array": Grow_Fanbase_array }
    #need to add for each reort temlate

    selected_report_focus_text = report_templates[report_focus][f"{report_focus}_text"]
    selected_report_focus_array = report_templates[report_focus][f"{report_focus}_array"]  
    #selected_report_focus = report_templates[report_focus] #report_focus variable name needs to exactly match name of List members
    print(f"value of selected_report_focus_text is: {selected_report_focus_text}")
    print(f"value of selected_report_array_text is: {selected_report_focus_array}")
    return selected_report_focus_text, selected_report_focus_array 
    