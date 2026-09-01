"""
M3's real schema uses native PostgreSQL UUID columns (`id UUID PRIMARY KEY
DEFAULT gen_random_uuid()`) everywhere. This type decorator gives us that
exact column type when running against Postgres, while still letting the
test suite run against SQLite locally (SQLite has no native UUID type, so
this falls back to CHAR(36) there - test-only, never used against the real
database).

This is the standard SQLAlchemy recipe for a portable UUID type.
"""
import uuid

from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class GUID(TypeDecorator):
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(PG_UUID(as_uuid=True))
        return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if dialect.name == "postgresql":
            return str(value)
        if not isinstance(value, uuid.UUID):
            return str(uuid.UUID(str(value)))
        return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        if isinstance(value, uuid.UUID):
            return value
        return uuid.UUID(value)
