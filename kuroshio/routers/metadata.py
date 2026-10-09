"""
Author: Timothy Kornish
CreatedDate: October 8 -2026
Description:
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from auth import CurrentUser
from config import settings
from database import get_db
from schemas import MetadataQueryBaseExecute, MetadataQueryUpdate

router = APIRouter()
