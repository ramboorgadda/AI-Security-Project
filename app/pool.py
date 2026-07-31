import asyncpg
from app.config import Config

_pool: asyncpg.Pool | None = None

async def init_pool() -> asyncpg.Pool:
    global _pool
    if _pool is None:
        config = Config()
        _pool = await asyncpg.create_pool(dsn=config.database_url)
    return _pool