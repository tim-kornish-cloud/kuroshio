"""
Author: Timothy Kornish
CreatedDate: October 8 -2026
Description: set up schemas for using in CRUD calls
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

"""
User specific models for creating and modifying a user
"""
class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str

class UserPrivate(UserPublic):
    email: EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
"""
Record query models for executing record queries in salesforce
"""
class RecordQueryBase(BaseModel):
    record: str = Field(min_length=1, max_length=100)
    query: str = Field(min_length=1)

class RecordQueryBaseExecute(RecordQueryBase):
    pass

class RecordQueryUpdate(BaseModel):
    record: str | None = Field(default=None, min_length=1, max_length=100)
    query: str | None = Field(default=None, min_length=1)
"""
Metadata query models for executing metadata queries in salesforce
"""
class MetadataQueryBase(BaseModel):
    record: str = Field(min_length=1, max_length=100)
    query: str = Field(min_length=1)

class MetadataQueryBaseExecute(MetadataQueryBase):
    pass

class MetadataQueryUpdate(BaseModel):
    record: str | None = Field(default=None, min_length=1, max_length=100)
    query: str | None = Field(default=None, min_length=1)
"""
Token and password reset schema for authorization and updating password
"""
class Token(BaseModel):
    access_token: str
    token_type: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(max_length=120)

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)
