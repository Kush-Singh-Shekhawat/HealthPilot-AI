from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import (
    String,
    Integer,
    Float,
    Date,
    DateTime,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.db import Base


# =====================================================
# USER
# =====================================================

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    age: Mapped[int] = mapped_column(Integer, nullable=False)

    gender: Mapped[str] = mapped_column(String(20), nullable=False)

    height: Mapped[float] = mapped_column(Float, nullable=False)

    weight: Mapped[float] = mapped_column(Float, nullable=False)

    blood_group: Mapped[str] = mapped_column(String(10), nullable=False)

    allergies: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    medical_conditions: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    medications: Mapped[list["Medication"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    health_metrics: Mapped[list["HealthMetric"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


# =====================================================
# MEDICATION
# =====================================================

class Medication(Base):
    __tablename__ = "medications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    medicine_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    dosage: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    frequency: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    scheduled_time: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Scheduled",
    )

    notes: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    user: Mapped["User"] = relationship(
        back_populates="medications",
    )


# =====================================================
# HEALTH METRICS
# =====================================================

class HealthMetric(Base):
    __tablename__ = "health_metrics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    record_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    steps: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    calories: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    water: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    sleep: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    weight: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    heart_rate: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    user: Mapped["User"] = relationship(
        back_populates="health_metrics",
    )


# =====================================================
# CONVERSATIONS
# =====================================================

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    question: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    response: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )