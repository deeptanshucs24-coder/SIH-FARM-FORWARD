import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.database import Base, engine
from app.routers import auth, users, crops, produce, market_prices, predict, recommend, buyers, profit

# Import every model so SQLAlchemy's metadata knows about all tables
# before create_all runs. Order doesn't matter for the import itself,
# but FK targets must exist as classes by the time create_all is called.
from app.models import (  # noqa: F401
    user, crop, farmer_produce, market, market_price,
    buyer, buyer_requirement, price_prediction, transport_rate,
    recommendation, notification,
)

logger = logging.getLogger("farmforward")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # MVP-speed: create tables directly instead of Alembic migrations.
    # Move to Alembic once the schema stabilizes post-integration.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="FarmForward API",
    description="Backend for Farmer Market Linkage & Price Discovery (SIH26132)",
    version="0.4.0",
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
    """Centralized catch-all: any error we didn't explicitly handle (a bug, a
    database hiccup, etc) gets logged server-side with full detail, but the
    client only ever sees a generic message - never a raw traceback or
    internal implementation detail. Expected, meaningful errors (404/403/409/
    422/etc raised deliberately via HTTPException) are untouched by this and
    still return their normal specific messages."""
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
