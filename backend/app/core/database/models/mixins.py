from datetime import datetime, timezone
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_mixin, mapped_column


@declarative_mixin
class Timestamp:
    created_at = mapped_column(
        DateTime, default=datetime.now(timezone.utc), nullable=False
    )
    updated_at = mapped_column(
        DateTime, default=datetime.now(timezone.utc), nullable=False
    )
