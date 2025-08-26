#from mainFunctionConcurrent import main as _main
from mainFunctionConcurrent import mainFunctionConcurrent as _main
import asyncio

def generate_report_sync_concurrent(chosen_artist: str, purpose_outline: str) -> str:
    """
    Runs your async `main()` in a fresh event loop (safe in a worker thread).
    Returns the two-pager document text.
    """
    return asyncio.run(_main(chosen_artist, purpose_outline))