import asyncio
import logging
logger = logging.getLogger(__name__)

async def with_retry(coro_func, max_retries: int = 3, retry_delay: float = 1.0, backoff: float = 2.0):
    """Call coro_fn() with exponential backoff. Raises the last exception if all retries fail."""
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            return await coro_func()
        except Exception as e:
            last_exc = e
            logger.warning(f"Attempt {attempt} failed with exception: {e}. Retrying in {retry_delay} seconds...")
            await asyncio.sleep(retry_delay)
            retry_delay *= backoff