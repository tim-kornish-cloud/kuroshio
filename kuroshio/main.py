"""
Author: Timothy Kornish
CreatedDate: October 8 -2026
Description:
"""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.exceptions import HTTPException as StarletteHTTPException

import models
from config import settings
from database import engine, get_db
from routers import metadata, records, users

@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(posts.router, prefix="/api/records", tags=["records"])
app.include_router(posts.router, prefix="/api/metadata", tags=["metadata"])


@app.get("/", include_in_schema=False, name="home")
async def home(request: Request, db: Annotated[AsyncSession, Depends(get_db)]):

    return templates.TemplateResponse(request, "home.html", {"title": "Home"})
