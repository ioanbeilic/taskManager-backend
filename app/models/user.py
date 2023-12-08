from sqlalchemy import UUID, Boolean, Column, DateTime, String, func
from app.config.database import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        unique=True,
        server_default=func.uuid_generate_v4(),
    )
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    uhdated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(150))
    email = Column(String(255), unique=True, index=True)
    mobile = Column(String(20), index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
