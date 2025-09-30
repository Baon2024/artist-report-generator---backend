from mainFunctionConcurrentTemplate import mainFunctionConcurrentTemplate as _main
import asyncio

def generate_report_sync_concurrent_template(chosen_artist: str, prompt_structure_array: list, prompt_structure_text: str) -> str:
    """
    Runs your async `main()` in a fresh event loop (safe in a worker thread).
    Returns the two-pager document text.
    """
    return asyncio.run(_main(chosen_artist, prompt_structure_array, prompt_structure_text))