"""
Author: Timothy Kornish
CreatedDate: October 8 -2026
Description:
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import settings
from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)

    record_query: Mapped[list[Record_Query]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )

    metadata_query: Mapped[list[MetadataQuery]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )

    reset_tokens: Mapped[list[PasswordResetToken]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class RecordQuery(Base):
    __tablename__ = "record_query"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    record: Mapped[str] = mapped_column(String(100), nullable=False)
    query: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    author: Mapped[User] = relationship(back_populates="record_query")

class MetadataQuery(Base):
    __tablename__ = "metadata_query"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    record: Mapped[str] = mapped_column(String(100), nullable=False)
    metadata: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    author: Mapped[User] = relationship(back_populates="metadata_query")


class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    user: Mapped[User] = relationship(back_populates="reset_tokens")
