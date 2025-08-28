





def get_template_prompt_structure(report_focus, chosen_artist):
    print(f"report_focus inside of get_template_prompt_structure is: {report_focus}")

    
    report_templates = {}

    bedroom_artist = f"""
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
`---BEGIN BRIEF---` and `---END BRIEF---`.  
If a section lacks data, keep the section but write “*No platform data supplied — analyst inference required*”.

**You should use the following template**

# 🎶 Audience Insight Report – Template

## Artist  
- **Name:**  
- **Primary location:** → global touring base  
- **One-liner fan archetype:**  

---

## Bio & What Stands Out  
- Bullet point 1  
- Bullet point 2  
- Bullet point 3  

---

## Audience Behaviour & Segmentation  

### Age-Tier Segmentation  
| Age-band | TikTok | Instagram | Spotify | Apple Music |
|----------|--------|-----------|---------|-------------|
| 13-17    | %      | %         | %       | %           |
| 18-24    | %      | %         | %       | %           |
| 25-34    | %      | %         | %       | %           |
| 35-44    | %      | %         | %       | %           |
| 45+      | %      | %         | %       | %           |

**Insight:**  
- Key mismatch or opportunity  

**Action:**  
- Tactical recommendation  

---

## Superfan Cohort Identification  
- **Method:** (e.g., top 10% repeat listeners + merch purchasers)  
- **Traits:** demographics, geo, behaviours, affinities  
- **Unifier:** psychographic summary  

---

## Demographic Skew Alerts  
- **Spotify:** % male / % female  
- **TikTok:** % male / % female  
- **Instagram:** % male / % female  

**Alert:** highlight notable skews + recommended action  

---

## Geo-Hotspot Map – “Emerging >50 % YoY, Marketing <10 %”  

| Rank | Market (city, country) | YoY stream growth | Share of marketing spend |
|------|------------------------|-------------------|---------------------------|
| 1    | City, Country          | +%                | %                         |
| 2    | City, Country          | +%                | %                         |

**Implication:** recommended reallocation or focus  

---

## Drop-Off Funnel Diagnostics (Spotify global, last 12 mo.)  

| Stage                | Avg % Remaining | Drop % |
|-----------------------|-----------------|--------|
| First play → 30s      | %               | %      |
| 30s → Save            | %               | % ⚠    |
| Save → Week-2 repeat  | %               | % ⚠    |

**High attrition tracks:** list examples  
**Low attrition tracks:** list examples  

---

## Proven Growth strategies of similar artists
- examine the strategies used by artists with similar chartmetric scores, or more established artists in the same playlists (if any)
- highlight any successful strategies, and explain how the artist {chosen_artist} could implement them


---

## Language & Lyric Sentiment Impact  
- Summary of sentiment effects on saves/streams  
- Non-music affinities (e.g., surf/skate, retro horror, gear content)  

---

## Content & Release Strategy  

### Seasonality Sweet-Spots  
- Peak months & rationale  

### Weekend vs Weekday Dynamics  
- Performance breakdown  

### Release-Day Social Cadence  
- T-3d: …  
- T-2d: …  
- T-1d: …  
- Release day: …  
- Post-day +1: …  

### Catalogue Revival Candidates  
1. Song – metric (+XX ranks / sync / trend)  
2. Song – metric (+XX ranks / sync / trend)  

### DSP Editorial vs Algorithmic Share  
- Editorial % | Algorithmic % | Organic %  
- Implications for marketing allocation  

---

## Key Recommendations – 90-Day Action Plan  
1. Action #1  
2. Action #2  
3. Action #3  
4. Action #4  
5. Action #5  

"""


    report_templates['bedroom artist'] = bedroom_artist


    selected_report_focus = report_templates[report_focus] #report_focus variable name needs to exactly match name of List members
    print(f"value of selected_report_focus is: {selected_report_focus}")
    return selected_report_focus 
    