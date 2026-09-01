import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.database import Base, engine
from app.routers import auth, users, crops, produce, market_prices, predict, recommend, buyers, profit

# Import every model so SQLAlchemy's metadata knows about all 7 tables
# (matching M3's schema.sql exactly) before create_all runs.
from app.models import (  # noqa: F401
    user, market, crop_listing, market_price, price_prediction,
    buyer_requirement, match,
)

logger = logging.getLogger("farmforward")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # checkfirst=True (SQLAlchemy's default) means this NEVER touches tables
    # that already exist. On Postgres, M3's schema.sql is authoritative and
    # should be run first - this is a safety net, not a competing source of
    # truth. It only matters in practice for SQLite local/test runs, where
    # nothing else creates the tables.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="FarmForward API",
    description="Backend for Farmer Market Linkage & Price Discovery (SIH26132) - "
                "aligned with M3's actual PostgreSQL schema (feature/m3-database).",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Any error we didn't explicitly handle gets logged server-side with
    full detail, but the client only ever sees a generic message - never a
    raw traceback or internal/database detail. Deliberate errors (404/403/
    409/422/etc via HTTPException) are untouched by this."""
    logger.exception("Unhandled error on %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(crops.router)
app.include_router(produce.router)
app.include_router(market_prices.router)
app.include_router(predict.router)
app.include_router(recommend.router)
app.include_router(buyers.router)
app.include_router(profit.router)


@app.get("/health", tags=["Health"], summary="Health check")
def health_check():
    return {"status": "ok", "env": settings.ENV}
