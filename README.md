## Overview of what matters

The current serrer file is the serverConcurrentTemplate one. This uses functions imported from the similar named mainFunctionConcurrentTemplate, and helFunctionConcurrentTemplate. 
The explanation behind this is that the fastapi server was upgraded to first be concurrent, and then to use a series of templates to generate the report focus and research questions. 
So, I kept the prior versions in case I needed to move back.

The current code will save multiple outputs of the agent systems memory, and generated reports, in the same folder, so it very quickly does get cluttered.

The current LLamaIndex agent system generates answers from muliple concurrent runs, in response to LLM generated questions based on the report focus template passed from the frontend.
An alternative way is to actually just divide the report focus template into sections, and send each section as the body of a question to a run of the agent system. I have implemented an array breakdown
of each template, and did test it by switching the question generation to use this, but the difference in output quality wasnt obvious, so I switched back. But its an easy change to make again, if you prefer.

The final report is actually generated using the combined memory from the runs of all the agents, rather than the answers they return. The reason for this is that the returned answer for each question
was consistently minimalist, and rarely made use of most of the raw relevant data present in the agents memories. Therefore, passing the memory for the final LLM call seemed a better approach. 
