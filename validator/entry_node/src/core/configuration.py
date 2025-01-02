import os

from dotenv import load_dotenv
from typing import TypeVar
import httpx
from pydantic import BaseModel
from redis.asyncio import Redis, BlockingConnectionPool
from validator.db.src.database import PSQLDB
from validator.utils.redis import redis_utils as rutils

T = TypeVar("T", bound=BaseModel)

load_dotenv()

from dataclasses import dataclass


@dataclass
class Config:
    redis_db: Redis | BlockingConnectionPool
    psql_db: PSQLDB
    prod: bool
    httpx_client: httpx.AsyncClient


async def load_config_once() -> Config:
    localhost = bool(os.getenv("LOCALHOST", "false").lower() == "true")
    if localhost:
        redis_host = "localhost"
        os.environ["POSTGRES_HOST"] = "localhost"
    else:
        redis_host = os.getenv("REDIS_HOST", "redis")

    psql_db = PSQLDB()
    await psql_db.connect()

    redis_pool = rutils.create_redis_pool(redis_host)

    prod = bool(os.getenv("ENV", "prod").lower() == "prod")

    return Config(
        psql_db=psql_db,
        redis_db=redis_pool,
        prod=prod,
        httpx_client=httpx.AsyncClient(),
    )

_config = None

async def factory_config():
    global _config
    if not _config:
        _config = await load_config_once()
    return _config
