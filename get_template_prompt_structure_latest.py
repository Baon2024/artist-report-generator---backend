


def get_template_prompt_structure_latest(report_focus, chosen_artist, artist_stage):

    print(f"report_focus inside of get_template_prompt_structure is: {report_focus}")
    print(f"artist_stage inside of get_template_prompt_structure is: {artist_stage}")
    
    structure_guides_collection = {
    "Developing": {
        "track_release": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS

This report is intended to help an artist to break their music through the noise and optimise their fanbase for a track release. They want to know actionable strategies and tactics to optimise their spend and find interesting pockets of value to have a successful track release.

For this report, the artist will be compared to 3 similar artists who’s presence they might like to emulate. 

This artist is likely developing and has a small fan presence.


1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an track release. Give a high-level overview of the artist’s current positioning and momentum that will aid this release. The goal is to describe very briefly what the report will entail in relation to the track release.
Include:
•⁠  ⁠2–3 sentences summarizing how the comparable artists are similar and what trends influence.
•⁠  ⁠One key data insight that creates excitement for the release.
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

Confident, data-driven, concise (like a market analyst note).

3. Comparison
Purpose: present a table that shows how the artist is comparable to the other 3 artists specifically focusing on the topic of track releases
Include in the table 
Theme
Common thread related to the theme 
What it shows
Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

4.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for the next track release. This should be based on what may have worked for the other artists.
Include subsections:
•⁠  ⁠Release Strategy (T-timeline):
  - Specific actions broken down by time markers (e.g., T-21, T-14, T-7, etc.).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
  - Example: “Spotify – Fan conversion hub. Update bio and playlists to reflect upcoming track narrative.”
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction worked for their track releases.
Where focus markets are for them and why does that optimise the track release
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting for an track release
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative —write as if advising a really small brand team or the artist, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

6.⁠ ⁠Platform Roles
Purpose: Define what each channel does in this specific campaign system for the track release.
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

7.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend will convert into presaves and preparation for the track release. The audience action pre track release is to drive pre-saves and create excitement. Artists will always have a smartlink for their profiles as a Call-to-action to drive pre-saves
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

8.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics. What are the key metrics that are relevant based on the comparable artists.
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Track Release Context\n- 2–3 sentences on how comparable artists are similar\n- Note key trends influencing this release window\n- One key data insight that creates excitement for the release",
                "## 3. Comparison – Track Release Themes\n| Theme | Common thread | What it shows |\n|-------|---------------|---------------|\n| …     | …             | …             |\n\n- Focus on track release execution patterns\n- Highlight repeatable tactics and ROI angles",
                "## 4. Suggested Action Points – Release Strategy (T-Timeline)\n### Release Strategy\n| Time (T-x) | Action (what to do) | Platform(s) | Intent |\n|-----------|---------------------|-------------|--------|\n| T-21      | …                   | …           | …      |\n| T-14      | …                   | …           | …      |\n| T-7       | …                   | …           | …      |\n| T-0       | …                   | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus\n- Other: role, core audience, content focus",
                "## 5. Strategic Insights\n### Content Insight\n- Storytelling and creative patterns that worked for track releases\n\n### Geo Insight\n- Focus markets and why they optimise the track release\n\n### Fanbase Insight\n- Target fan types (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Key associations, co-signs, or followers that build legitimacy",
                "## 6. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                "## 7. Paid Media & KPIs – Track Release\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Key demographics\n- Priority geos\n- Fan types (high-intent, discovery, nostalgia)\n\n### Ad Objectives by Channel\n- TikTok: prospecting / retargeting\n- IG: prospecting / retargeting\n- YouTube: prospecting / retargeting\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| T-14      | …                         |\n| T-7       | …                         |\n| T-0       | …                         |\n| T+7       | …                         |\n\n**Contingency Plan**\n- If metrics fall short: specific optimisation actions",
                "## 8. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan profile and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Audience distribution by platform\n- Age distribution by platform\n- Notable imbalances or opportunities"
            ]
        },
        "album_release": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS

This report is intended to help an artist to break their music through the noise and optimise their fanbase for an album release. They want to know actionable strategies and tactics to optimise their spend and find interesting pockets of value to have a successful album release.

For this report, the artist will be compared to 3 similar artists who’s presence they might like to emulate. 

This artist is likely developing and has a small fan presence.

1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an album release. Give a high-level overview of the artist’s current positioning and momentum that will aid this release. The goal is to describe very briefly what the report will entail in relation to the album release. Also note who the comparable artists in this report have been.
Include:
•⁠  ⁠2–3 sentences summarizing how the comparable artists are similar and what trends influence.
•⁠  ⁠One key data insight that creates excitement for the release that might have been found from the data of the other artists. 
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

Confident, data-driven, concise (like a market analyst note).

3. Comparison
Purpose: present a table that shows how the artist is comparable to the other 3 artists specifically focusing on the topic of track releases
Include in the table 
Theme
Common thread related to the theme 
What it shows
Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

4.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for the next album release. This should be based on what may have worked for the other artists.
Include subsections:
•⁠  ⁠Release Strategy (T-timeline):
  - Specific actions broken down by time markers (e.g., T-21, T-14, T-7, etc.).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
  - Example: “Spotify – Fan conversion hub. Update bio and playlists to reflect album narrative.”
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Strategic Insights
Purpose: Translate general data of the other comparable artists into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction worked for their album releases.
•⁠  ⁠Geo Insight: Where focus markets are for them and why does that optimise the album release
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting for an album release based on what works for them 
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative — write as if advising a really small brand team or the artist directly, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

6.⁠ ⁠Platform Roles
Purpose: Define what each channel does in this specific campaign system for the album release. 
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

7.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend will convert into presaves and preparation for the album release. The audience action pre album release is to drive pre-saves and create excitement. Artists will always have a smartlink for their profiles as a Call-to-action to drive pre-saves
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

8.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics. What are the key metrics that are relevant based on the comparable artists.
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Album Release Context\n- 2–3 sentences on how comparable artists are similar\n- Note which comparable artists are used and why\n- One key data insight that creates excitement for the album release",
                "## 3. Comparison – Album Release Themes\n| Theme | Common thread | What it shows |\n|-------|---------------|---------------|\n| …     | …             | …             |\n\n- Focus on album-era strategy, pacing and ROI patterns",
                "## 4. Suggested Action Points – Album Release Strategy (T-Timeline)\n### Release Strategy\n| Time (T-x) | Action (what to do) | Platform(s) | Intent |\n|-----------|---------------------|-------------|--------|\n| T-42      | …                   | …           | …      |\n| T-28      | …                   | …           | …      |\n| T-14      | …                   | …           | …      |\n| T-7       | …                   | …           | …      |\n| T-0       | …                   | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus\n- Other: role, core audience, content focus",
                "## 5. Strategic Insights\n### Content Insight\n- Storytelling and creative patterns that worked for album releases\n\n### Geo Insight\n- Focus markets and why they optimise the album release\n\n### Fanbase Insight\n- Which fan types to target (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Associations, co-signs, or followers that create legitimacy",
                "## 6. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                "## 7. Paid Media & KPIs – Album Release\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Key demographics\n- Priority geos\n- Fan types to prioritise (album buyers, deep listeners)\n\n### Ad Objectives by Channel\n- Channel-by-channel objective: prospecting / retargeting / pre-save / pre-add\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| T-28      | …                         |\n| T-14      | …                         |\n| T-0       | …                         |\n| T+7       | …                         |\n| T+28      | …                         |\n\n**Contingency Plan**\n- If metrics fall short: optimisation and reallocation steps",
                "## 8. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan profile and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Audience distribution by platform\n- Age distribution by platform\n- Platform-specific strengths and weaknesses"
            ]
        },
        "fanbase_and_growth_analysis": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS


This is a report that an artist or band will be using to identify who their fanbase is and how they can grow it. 
This report is for mature artists who already have a strong following and now want to grow.

For this report, the artist will be compared to 3 similar artists who’s presence they might like to emulate. 

This artist is likely developing and has a small fan presence.
1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an artist to understand their audience and grow their fanbase through smart marketing by comparing to similar artists that they want to emulate as they grow. Give a high-level overview of the artist’s current positioning. The goal is to describe very briefly what the report will entail in relation to their audience and fanbase growth.
Include:
•⁠  ⁠2–3 sentences summarizing the comparable artist’s previous performance or shift (e.g., a reunion, viral moment, tour success).
⁠A key data insight that justifies how this artist ca grow
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

4. Comparison
Purpose: present a table that shows how the artist is comparable to the other 3 artists specifically focusing on their general audience, social media following, content and fanbase breakdown
Include in the table 
Theme
Common thread related to the theme 
What it shows
Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

4.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for their general social media growth based on what is working for the comparable artists.
Include subsections:
•⁠  ⁠Release Strategy (forward looking, 1 week, 1 month, 3 months):
  - Specific actions broken down by time markers (e.g., W-1-4, W 5-8, W9-12).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction works for the comparable artists that can now be used to grow them.
•⁠  ⁠Geo Insight: Where focus markets are and why to optimise their social media to grow or maintain this audience
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting as part of their fan optimisation plan
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative — write as if advising a label or brand team, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Platform Roles
Purpose: Define what each channel does in the campaign system.
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

6.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend can be used to increase followers on the platforms. The audience action would be to follow the artist and drive engagement. Artists will always have a smartlink for their profiles as a Call-to-action to their music
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

7.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics. What are the key metrics that are relevant based on the comparable artists?
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Fanbase & Growth Context\n- 2–3 sentences on comparable artists’ recent performance or shifts\n- One key data insight that justifies growth potential\n- One line on how this report will guide fanbase growth",
                "## 3. Comparison – Audience & Fanbase\n| Theme | Common thread | What it shows |\n|-------|---------------|---------------|\n| …     | …             | …             |\n\n- Focus on audience size, content style, and fanbase structure",
                "## 4. Suggested Action Points – Social Growth Plan\n### Time-anchored plan (Forward looking)\n| Time window | What to post/do | Platform(s) | Intent |\n|------------|------------------|-------------|--------|\n| W1–4       | …                | …           | …      |\n| W5–8       | …                | …           | …      |\n| W9–12      | …                | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus",
                "## 5. Strategic Insights\n### Content Insight\n- Storytelling and formats that worked for comparable artists\n\n### Geo Insight\n- Focus markets and why they matter for growth\n\n### Fanbase Insight\n- Which fan types to prioritise (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Associations and followers that elevate brand legitimacy",
                "## 6. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                "## 7. Paid Media & KPIs – Fanbase Growth\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Demographics\n- Geo focus\n- Fan types (growth vs depth)\n\n### Ad Objectives by Channel\n- Prospecting vs retargeting per channel\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| W1–4      | …                         |\n| W5–8      | …                         |\n| W9–12     | …                         |\n\n**Contingency Plan**\n- If metrics fall short: optimisation and channel shift",
                "## 8. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan profile and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Audience distribution by platform\n- Age distribution by platform\n- Priority segments to grow"
            ]
        }
    },

    "Established": {
        "track_release": {
            "text": "placeholder - report structure not created yet",
            "array": []
        },
        "album_release": {
            "text": "placeholder - report structure not created yet",
            "array": []
        },
        "fanbase_and_growth_analysis": {
            "text": "placeholder - report structure not created yet",
            "array": []
        }
    },

    "Mature": {
        "track_release": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS

This report is intended to help an artist to break their music through the noise and optimise their fanbase for a track release. They want to know actionable strategies and tactics to optimise their spend and find interesting pockets of value to have a successful track release.

This artist is likely mature and has a loyal following and presence


1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an track release. Give a high-level overview of the artist’s current positioning and momentum that will aid this release. The goal is to describe very briefly what the report will entail in relation to the track release.
Include:
•⁠  ⁠2–3 sentences summarizing the artist’s previous performance or shift (e.g., a reunion, viral moment, tour success).
•⁠  ⁠One key data insight that creates excitement for the release.
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

Confident, data-driven, concise (like a market analyst note).

3.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for the next track release.
Include subsections:
•⁠  ⁠Release Strategy (T-timeline):
  - Specific actions broken down by time markers (e.g., T-21, T-14, T-7, etc.).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
  - Example: “Spotify – Fan conversion hub. Update bio and playlists to reflect upcoming track narrative.”
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

4.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction works for track releases.
•⁠  ⁠Geo Insight: Where focus markets are and why to optimise the track release
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting for an track release
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative — write as if advising a label or brand team, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Platform Roles
Purpose: Define what each channel does in this specific campaign system for the track release.
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

6.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend will convert into presaves and preparation for the track release. The audience action pre track release is to drive pre-saves and create excitement. Artists will always have a smartlink for their profiles as a Call-to-action to drive pre-saves
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

7.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics.
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Track Release for Mature Artist\n- 2–3 sentences on recent performance or shifts (tour, viral, reunion, etc.)\n- One key data insight creating excitement for this track\n- One line on how this track fits into the wider catalogue",
                "## 3. Suggested Action Points – Track Release Strategy\n### Release Strategy (T-Timeline)\n| Time (T-x) | Action (what to do) | Platform(s) | Intent |\n|-----------|---------------------|-------------|--------|\n| T-21      | …                   | …           | …      |\n| T-14      | …                   | …           | …      |\n| T-7       | …                   | …           | …      |\n| T-0       | …                   | …           | …      |\n| T+7       | …                   | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus\n- Other: role, core audience, content focus",
                "## 4. Strategic Insights\n### Content Insight\n- Storytelling and creative approaches that work for track drops\n\n### Geo Insight\n- Focus markets and why they matter for this release\n\n### Fanbase Insight\n- Fan segments to target (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Key associations and co-signs that can be activated",
                "## 5. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                "## 6. Paid Media & KPIs – Track Release\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Demographics\n- Geo focus\n- Fan type (superfans, lapsed, discovery)\n\n### Ad Objectives by Channel\n- Prospecting vs retargeting vs pre-save focus\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| T-21      | …                         |\n| T-14      | …                         |\n| T-7       | …                         |\n| T-0       | …                         |\n| T+7       | …                         |\n\n**Contingency Plan**\n- If metrics fall short: optimisation and reallocation steps",
                "## 7. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan definition and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Platform distribution\n- Age distribution by platform\n- Notable gaps vs. track strategy"
            ]
        },
        "album_release": {
            "text": """🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS

This report is intended to help an artist to maximise the reach of their music optimise their fanbase for an album release. They want to know actionable strategies and tactics to optimise their spend and find interesting pockets of value to have a successful album release.
This artist is likely mature and has a loyal following and presence
1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an album release. Give a high-level overview of the artist’s current positioning and momentum that will aid this release. The goal is to describe very briefly what the report will entail in relation to the album release.
Include:
•⁠  ⁠2–3 sentences summarizing the artist’s previous performance or shift (e.g., a reunion, viral moment, tour success).
•⁠  ⁠One key data insight that creates excitement for the release.
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

Confident, data-driven, concise (like a market analyst note).

3.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for the next album release.
Include subsections:
•⁠  ⁠Release Strategy (T-timeline):
  - Specific actions broken down by time markers (e.g., T-21, T-14, T-7, etc.).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
  - Example: “Spotify – Fan conversion hub. Update bio and playlists to reflect album narrative.”
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

4.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction works for album releases.
•⁠  ⁠Geo Insight: Where focus markets are and why to optimise the album release
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting for an album release
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative — write as if advising a label or brand team, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Platform Roles
Purpose: Define what each channel does in this specific campaign system for the album release.
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

6.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend will convert into presaves and preparation for the album release. The audience action pre album release is to drive pre-saves and create excitement. Artists will always have a smartlink for their profiles as a Call-to-action to drive pre-saves
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table

7.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics.
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Album Release for Mature Artist\n- 2–3 sentences on previous performance or shift (tour, viral, reunion, etc.)\n- One key data insight that creates excitement for the album\n- One line clarifying what this report will cover",
                "## 3. Suggested Action Points – Album Release Strategy\n### Release Strategy (T-Timeline)\n| Time (T-x) | Action (what to do) | Platform(s) | Intent |\n|-----------|---------------------|-------------|--------|\n| T-60      | …                   | …           | …      |\n| T-42      | …                   | …           | …      |\n| T-28      | …                   | …           | …      |\n| T-14      | …                   | …           | …      |\n| T-7       | …                   | …           | …      |\n| T-0       | …                   | …           | …      |\n| T+7       | …                   | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus\n- Other: role, core audience, content focus",
                "## 4. Strategic Insights\n### Content Insight\n- Storytelling and creative approaches that work for album campaigns\n\n### Geo Insight\n- Focus markets and why they matter for the album\n\n### Fanbase Insight\n- Fan types to prioritise (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Brand and artist associations that can be activated",
                "## 5. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                "## 6. Paid Media & KPIs – Album Release\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Demographics\n- Geo focus\n- Fan type focus (superfans, deep catalogue listeners)\n\n### Ad Objectives by Channel\n- Prospecting vs retargeting vs pre-save focus\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| T-60      | …                         |\n| T-42      | …                         |\n| T-28      | …                         |\n| T-14      | …                         |\n| T-0       | …                         |\n| T+7       | …                         |\n| T+28      | …                         |\n\n**Contingency Plan**\n- If metrics fall short: re-optimise, re-sequence, or push back beats",
                "## 7. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan definition and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Platform distribution\n- Age distribution by platform\n- Key strengths and vulnerabilities for album cycle"
            ]
        },
        "catalogue_revival": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS

This report is intended to help mature artists to revive their old catalogue that has been performing well. They want to jump on trends and identify opportunities to reuse old music so that they can increase streaming and double down. They want to know actionable strategies and tactics to optimise their spend and find interesting ways of unlocking old catalogue.
This artist is likely mature and has a loyal following and presence


1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is to enable a mature artist to revive previous tracks that have been doing well. Give a high-level overview of the artist’s current positioning and momentum that old tracks longer than 1 year might be gaining. The goal is to help describe very briefly what they could do to revive old catalogue.
Include:
•⁠  ⁠2–3 sentences summarizing the artist’s old tracks and how there might be a certain shift (e.g., a reunion, viral moment, anniversary).
•⁠  ⁠One key data insight that creates excitement to revive catalogue..
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

Confident, data-driven, concise (like a market analyst note).

3.⁠ Suggested Action Points:  
Purpose: Present a clear recommendations for reviving old tracks with bulleted actions that they can implement
Include subsections:
•⁠  ⁠Revival Strategy 
How can they use their social media platforms to bring hype back for old catalogue
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,”)

Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

4.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction works for old catalogue revival strategies
•⁠  ⁠Geo Insight: Where focus markets are based on the data and why to use this geo for the revival targetting
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting for the catalogue revival
Tone: Analytical but narrative — write as if advising a label or brand team, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

5.⁠ ⁠Touring Recommendations
Purpose: Outline how touring spend can be done optimally to help them better drive love for old catalogue. There can also be recommendations on where the artist should be touring based on spikes in their catalogue and viewership. 
Include:
•⁠  Specific cities and countries that the artist can target for live performances
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type) in those cities
•⁠  how can they best maximise their presence when touring and reviving catalogue

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as bullet points


6.⁠ Data Evidence
Purpose: Prove every recommendation with real metrics.
Include subsections:
⁠  Streaming stats of catalogue Overview:
Trending music: present vs old
- markets where streamers are present
- spikes in listeners and interesting pockets.
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
Tone: Analytical; use numbers as visual anchors.
""",
            "array": [
                "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                "## 2. Summary – Catalogue Revival\n- 2–3 sentences on catalogue history and shifts (anniversaries, virality, etc.)\n- One key data insight that creates excitement to revive catalogue\n- One line on what the report will cover",
                "## 3. Suggested Action Points – Revival Strategy\n### Revival Strategy via Social Platforms\n- TikTok: what to post, format, and intent\n- Instagram: what to post, format, and intent\n- YouTube: what to post, format, and intent\n- Other: what to post, format, and intent\n\nEach bullet should specify:\n- What to post/do\n- Platform(s) used\n- Intent (reactivate audience, deepen nostalgia, etc.)",
                "## 4. Strategic Insights\n### Content Insight\n- Storytelling and creative directions suited to catalogue revival\n\n### Geo Insight\n- Focus markets for revival and why they matter\n\n### Fanbase Insight\n- Fan types to target (high-intent, nostalgic, trend-driven)",
                "## 5. Touring Recommendations\n- Specific cities and countries to target for live performances\n- Audience rationale in those markets (demographics, geo, fan type)\n- How to use shows to revive catalogue (setlists, moments, merch, content capture)",
                "## 6. Data Evidence – Catalogue Revival\n### Streaming Stats of Catalogue\n- Present vs old catalogue performance\n- Markets where catalogue streamers are most active\n- Spikes and interesting pockets\n\n### Audience Overview\n- Social footprint total\n- Superfan definition and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Platform distribution\n- Age distribution by platform\n- Alignment between social and catalogue listeners"
            ]
        },
        "fanbase_and_growth_analysis": {
            "text": """
🧩 STRUCTURAL BREAKDOWN & WRITING INSTRUCTIONS


This is a report that an artist or band will be using to identify who their fanbase is and how they can grow it. 
This report is for mature artists who already have a strong following and now want to grow.

1.⁠ ⁠Header / Artist Overview
Purpose: Give a quick snapshot to act as a header of the report
Include:
Artist name
Genre
primary location.
Social following on all platforms 
Tone: Clean, factual, no sentences

2.⁠ Summary
Purpose: This report is for an artist to understand their audience and grow their fanbase through smart marketing Give a high-level overview of the artist’s current positioning and momentum that will aid their growth. The goal is to describe very briefly what the report will entail in relation to their audience and fanbase growth.
Include:
•⁠  ⁠2–3 sentences summarizing the artist’s previous performance or shift (e.g., a reunion, viral moment, tour success).
⁠A key data insight that justifies the next strategic phase.
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 
3.⁠ Suggested Action Points:  
Purpose: Present a clear, time-anchored plan for their general social media growth.
Include subsections:
•⁠  ⁠Release Strategy (forwaard looking, 1 week, 1 month, 3 months):
  - Specific actions broken down by time markers (e.g., W-1-4, W 5-8, W9-12).
  - Each entry should include:
    - What to post/do
    - Platform(s) used
    - The intent (e.g., “reactivate audience,” “drive pre-saves”)
•⁠  ⁠Platform Focus:
  - For each major platform, list role, core audience, and content type focus.
Tone: Actionable, like a marketing operations brief, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 

4.⁠ ⁠Strategic Insights
Purpose: Translate general data into big-picture guidance.
Include:
•⁠  ⁠Content Insight: What type of storytelling or creative direction works for this type of artist and their existing content
•⁠  ⁠Geo Insight: Where focus markets are and why to optimise their social media to grow or maintain this audience
•⁠  ⁠Fanbase Insight: What kind of fans (high-intent, nostalgic, trend-driven) should the artist be targeting as part of their fan optimisation plan
•⁠  ⁠Credibility Insight: Which associations or followers build brand legitimacy.
Tone: Analytical but narrative — write as if advising a label or brand team, warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 
5.⁠ ⁠Platform Roles
Purpose: Define what each channel does in the campaign system.
Include columns like:
•⁠  ⁠Platform name
•⁠  ⁠Follower count / reach
•⁠  ⁠Campaign role (e.g., “Fan Conversion Hub”)
•⁠  ⁠Type of content used
Tone: Warm, non-technical, soft and direct approach, not overly wordy, approachable
Shouldn't feel like a lesson but also should not feel like a storybook. 
6.⁠ ⁠Paid Media & KPIs
Purpose: Outline how marketing spend can be used to increase followers on the platforms. The audience action would be to follow the artist and drive engagement. Artists will always have a smartlink for their profiles as a Call-to-action to their music
Include:
•⁠  ⁠Budget breakdown - A percentage-based breakdown of ad spend by platform
•⁠  ⁠Audience targeting rationale (demographics, geo, fan type).
•⁠  ⁠Ad objectives per channel (retargeting vs. prospecting).
•⁠  ⁠Primary KPIs (click-through, saves, etc.) - A markdown table with Milestone and Key Performance Indicator.
Contingency Plan: "If metrics fall short..." actions.

Tone: Tactical and ROI-focused; short sentences and percentages are fine. Can be presented as a table




7.⁠ ⁠The Data Evidence
Purpose: Prove every recommendation with real metrics.
Include subsections:
•⁠  ⁠Audience Overview:
- Social footprint total, and who the superfan is  fan conversion %
- core markets, 
- demographics.
  - Use bullet points and short phrases for clarity.
•⁠  ⁠Social Media Fanbase:
  - Breakdown of audience distribution by platform and age.
- Which brands does this artist have the highest affinities for. 
Describe what is meant by affinity and how it is calculated 
Are there any followers of this artist that have a large following
Tone: Analytical; use numbers as visual anchors.
""",
                "array": [
                    "## 1. Header / Artist Overview\n- Artist name\n- Genre\n- Primary location\n- Social following by platform (TikTok, Instagram, YouTube, Spotify, others)",
                    "## 2. Summary – Mature Fanbase & Growth\n- 2–3 sentences on previous performance or shift (tour, viral, reunion, etc.)\n- One key data insight that justifies the next strategic phase\n- One line clarifying what this report will cover for growth",
                    "## 3. Suggested Action Points – Social Growth Plan\n### Forward-looking Release & Content Strategy\n| Time window | What to post/do | Platform(s) | Intent |\n|------------|------------------|-------------|--------|\n| W1–4       | …                | …           | …      |\n| W5–8       | …                | …           | …      |\n| W9–12      | …                | …           | …      |\n\n### Platform Focus\n- TikTok: role, core audience, content focus\n- Instagram: role, core audience, content focus\n- YouTube: role, core audience, content focus\n- Spotify: role, core audience, content focus",
                    "## 4. Strategic Insights\n### Content Insight\n- Storytelling and creative approaches that work for this artist type\n\n### Geo Insight\n- Focus markets and why they matter for sustaining or growing the audience\n\n### Fanbase Insight\n- Fan types to target (high-intent, nostalgic, trend-driven)\n\n### Credibility Insight\n- Associations and brand/artist followers that build legitimacy",
                    "## 5. Platform Roles\n| Platform | Followers / Reach | Campaign role | Content types |\n|----------|-------------------|---------------|---------------|\n| TikTok   | …                 | …             | …             |\n| IG       | …                 | …             | …             |\n| YouTube  | …                 | …             | …             |\n| Spotify  | …                 | …             | …             |\n| Other    | …                 | …             | …             |",
                    "## 6. Paid Media & KPIs – Fanbase Growth\n### Budget Breakdown\n- TikTok Ads: % of total\n- Instagram Ads: % of total\n- YouTube Ads: % of total\n- Other: % of total\n\n### Audience Targeting\n- Demographics\n- Geo focus\n- Fan types (growth vs depth)\n\n### Ad Objectives by Channel\n- Prospecting vs retargeting per channel\n\n### Primary KPIs\n| Milestone | Key Performance Indicator |\n|-----------|---------------------------|\n| W1–4      | …                         |\n| W5–8      | …                         |\n| W9–12     | …                         |\n\n**Contingency Plan**\n- If metrics fall short: optimisation and reallocation steps",
                    "## 7. The Data Evidence\n### Audience Overview\n- Total social footprint\n- Superfan definition and fan conversion %\n- Core markets\n- Demographic breakdown\n\n### Social Media Fanbase\n- Audience distribution by platform\n- Age distribution by platform\n- Top brand affinities and what “affinity” means (incl. method summary)\n- Notable high-follower fans and how to leverage them"
                ]
            }
        }
    }

    
    #structure_guides_collection['track_release'] = { "track_release_text": bedroom_artist_text, "track_release_array": bedroom_artist_array }
    #report_templates['album_release'] = { "album_release_text": Album_Preparation_text, "album_release_array": Album_Preparation_array }
    #report_templates['fanbase_and_growth_analysis'] = { "fanbase_and_growth_analysis_text": Maintain_Audience_Engagement_text, "fanbase_and_growth_analysis_array": Maintain_Audience_Engagement_array }
    #report_templates['catalogue_revival'] = { "catalogue_revival_text": Revive_Catalogue_text, "catalogue_revival_array": Revive_Catalogue_array }
    
    selected_report_focus_text = structure_guides_collection[artist_stage][report_focus]["text"]
    selected_report_focus_array = structure_guides_collection[artist_stage][report_focus]["array"] 
    #selected_report_focus = report_templates[report_focus] #report_focus variable name needs to exactly match name of List members
    print(f"value of selected_report_focus_text is: {selected_report_focus_text}")
    print(f"value of selected_report_array_text is: {selected_report_focus_array}")
    return selected_report_focus_text, selected_report_focus_array 
    
