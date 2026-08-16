from redis.asyncio import Redis

from app.core.config import get_settings

settings = get_settings()

redis_client = Redis.from_url(settings.redis_url, decode_responses=True)


def get_redis_client() -> Redis:
    return redis_client


async def ping_redis() -> bool:
    try:
        return bool(await redis_client.ping())
    except Exception:
        return False
