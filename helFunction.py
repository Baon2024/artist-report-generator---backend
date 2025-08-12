from mainFunction import main as _main
import asyncio

def generate_report_sync(chosen_artist: str, purpose_outline: str) -> str:
    """
    Runs your async `main()` in a fresh event loop (safe in a worker thread).
    Returns the two-pager document text.
    """
    return asyncio.run(_main(chosen_artist, purpose_outline))