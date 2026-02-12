# Reverb Backend

## Overview

This repository contains the backend for the Reverb application, primarily focusing on generating comprehensive artist reports. The core of the report generation logic resides in `serverConcurrentTemplate.py`, which leverages a templating system and concurrent processing for efficiency. This setup allows for dynamic report generation based on user-defined foci and artist data.

## Key Features

*   **Concurrent Report Generation**: Utilizes `asyncio` and `anyio.to_thread` for efficient, non-blocking execution of report generation tasks.
*   **Template-Driven Reports**: Generates reports based on predefined templates (`get_template_prompt_structure_latest.py`), allowing for consistent and structured output.
*   **Dynamic Prompt Generation**: Constructs prompts dynamically using `dynamic_prompt_structure.py` to tailor report content.
*   **Google Docs Integration**: Automatically creates and populates Google Docs with the generated reports, including formatting for titles, subtitles, and body text.
*   **Supabase Integration (PostgreSQL)**: Accesses artist and track data from a PostgreSQL database (assumed to be Supabase) to enrich the reports.
*   **Langfuse Integration**: Utilizes Langfuse for prompt management, dataset tracking, and tracing of LLM calls, providing observability into the report generation process.
*   **OpenAI/Gemini Integration**: Interfaces with OpenAI and Google Gemini models for natural language understanding and content generation.
*   **CORS Enabled**: Configured to allow cross-origin requests, facilitating integration with various frontend applications.

## Data Access via Supabase (PostgreSQL)

The `serverConcurrentTemplate.py` file connects to a PostgreSQL database (typically a Supabase instance) to retrieve essential data for report generation. The data access flow is as follows:

1.  **Database Connection**: Establishes a secure connection to the PostgreSQL database using environment variables for credentials (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`).
2.  **Artist Identification**: An internal artist ID is retrieved from the `artist_reference` table using the `chartmetric_id` provided in the request.
3.  **Artist Metrics**: Comprehensive metrics related to the artist are fetched from the `artist_metrics` table.
4.  **Track References**: Details for all tracks associated with the artist are retrieved from the `track_reference` table (including ISRC and track names).
5.  **Track Metrics**: For each identified track, specific metrics are pulled from the `track_metrics` table using its ISRC.
6.  **Social Media Data**: Relevant social media posts for the artist are obtained from the `social_posts` table.
7.  **Consolidated Data**: All retrieved data is then compiled into a `data_for_report` dictionary, which serves as input for the LLM-driven report generation.

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd originalReverbBackend
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**: Create a `.env` file in the root directory and populate it with the necessary environment variables:
    ```
    OPENAI_API_KEY="your_openai_api_key"
    DB_USER="your_db_user"
    DB_PASSWORD="your_db_password"
    DB_HOST="your_db_host"
    DB_PORT="your_db_port"
    DB_NAME="your_db_name"
    # Other necessary environment variables for Google Sheets API if using local credentials
    # LANGFUSE_SECRET_KEY="sk-lf-..."
    # LANGFUSE_PUBLIC_KEY="pk-lf-..."
    # LANGFUSE_HOST="https://cloud.langfuse.com"
    ```
    *Note: For Google Docs integration, a service account JSON key is used for authentication, which is typically handled as a secret in deployed environments.*

## Usage

To run the server locally:

```bash
uvicorn serverConcurrentTemplate:app --host 0.0.0.0 --port 3011 --reload
```

For detailed logging to a file (useful for debugging agent decision-making):

```bash
PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python -X utf8 -m uvicorn serverConcurrentTemplate:app --host 0.0.0.0 --port 3011 2>&1 | tee -a output.log
```

The server will be accessible at `http://localhost:3011`.

### Endpoints

*   **`/health` (GET)**: Basic health check endpoint.

*   **`/reportGeneratorLatest` (POST)**: The primary endpoint for the latest Reverb variant, supporting specific report choices, custom prompt extensions, and comprehensive data retrieval from Supabase.


