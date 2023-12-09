from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    String,
    Table,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import relationship
from src.config.database import Base
from enum import Enum as PythonEnum


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


# Tabla de asociación para la relación muchos a muchos
user_organization_association = Table(
    "user_organization_association",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id")),
    Column("organization_id", UUID(as_uuid=True), ForeignKey("organizations.id")),
    Column("is_default", Boolean, default=False),
    Column("role", Enum("admin", "member", name="user_roles")),
    # unique user for organization and organization for user
    UniqueConstraint("user_id", "organization_id"),
)


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(150))
    email = Column(String(255), unique=True, index=True)
    mobile = Column(String(20), index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True, default=None)
    organizations = relationship(
        "Organization", secondary=user_organization_association, back_populates="users"
    )


class Organization(BaseModel):
    __tablename__ = "organizations"

    name = Column(String, index=True, unique=True)
    users = relationship(
        "User", secondary=user_organization_association, back_populates="organizations"
    )


user_workspace_association = Table(
    "user_workspace_association",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id")),
    Column("organization_id", UUID(as_uuid=True), ForeignKey("organizations.id")),
    Column("workspace_id", UUID(as_uuid=True), ForeignKey("workspaces.id")),
    Column(
        "role",
        Enum(
            "super_admin",
            "admin",
            "manager",
            "employee",
            "member",
            name="user_roles",
        ),
    ),
)


class Workspace(BaseModel):
    __tablename__ = "workspaces"

    name = Column(String, index=True, unique=True)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="workspaces")
    users = relationship(
        "User", secondary=user_workspace_association, back_populates="workspaces"
    )


class UserRole(PythonEnum):
    super_admin = "super_admin"
    admin = "admin"
    manager = "manager"
    employee = "employee"
    member = "member"
