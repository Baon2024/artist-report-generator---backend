import google.generativeai as genai
import re
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

genai.configure(api_key="AIzaSyBtpgpnI_kzxPfvlqoDbaYwlOPdxI89qNI")
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)


#artist_name = "Kenan Doğulu"
purpose_outline = f"""
# ROLE & TASK
You are a **senior music strategist** hired to deliver a **two-page Audience Intelligence Brief** for the artist .

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
### Deep-Dive Audience Analysis for teh artist 
(Synthesising Instagram, TikTok & YouTube data within Turkish pop-market context)

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



---BEGIN BRIEF---
<!-- o3 starts populating here -->
---END BRIEF---
"""

#llm call to generate list of questions and prompt
#do so seperrekt







def generate_questions_dynamic(artist_name, prompt):
    #model = genai.GenerativeModel("models/gemini-2.5-pro")
    message = f"""Using the purpose_outline passed to you, you need to generate a series of questions of as many questions as you think are neccessary to fulfill the outline.


The following tools are available to answer the questions you generate: get_tiktok_audience_data, get_instagram_audience_data, get_youtube_audience_data, get_similar_artists, get_charts.
You should generate questions that can axctually be answered with the tools available to you.

You should return the questions in the format: ["question 1", "question 2", "question 3"]. NO NUMBERS, STRICTLY THAT SCHEMA. No more than 10, no less than 7 questions.

Context:
The artist is: {artist_name}
The purpose_outline is: {prompt}

"""  # Generate content
    #response_gemini = model.generate_content(message)
    response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ],
    temperature=0.7
    )

  

    questions = response.output_text
    print(f"response_gemini is: {questions}")
    questions_to_ask = questions
    print(f"questions_to_ask are: {questions_to_ask}")
     
    stripped_questions_to_ask = re.sub(r"^```json\s*|\s*```$", "", questions_to_ask.strip())
    print(f"post-stripping: {stripped_questions_to_ask}")
     
    questions_to_ask_cleaned = json.loads(stripped_questions_to_ask)
    print(f"questions_to_ask_cleaned is: {questions_to_ask_cleaned}")
    return questions_to_ask_cleaned

#generate_questions_dynamic("Kenan Doğulu", purpose_outline)