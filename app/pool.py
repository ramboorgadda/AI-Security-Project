import asyncpg
from app.config import Config

_pool: asyncpg.Pool | None = None

async def init_pool() -> asyncpg.Pool:
    global _pool
    if _pool is None:
        config = Config()
        _pool = await asyncpg.create_pool(dsn=config.database_url)
    return _pool
async def get_pool() -> asyncpg.Pool:
    if _pool is None:
        raise RuntimeError("Database pool has not been initialized. Call init_pool() first.")
    return _pool
async def close_pool() -> None:
    global _pool    
    if _pool:   
        await _pool.close()
        _pool = None
        