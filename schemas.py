from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    """Base schema for a URL. Both create and read schemas will share this."""
    target_url: HttpUrl

class URLCreate(URLBase):
    """Schema for creating a new URL."""
    pass

class URLInfo(URLBase):
    """Schema for returning URL info to the user."""
    is_active: bool
    clicks: int
    key: str

    class Config:
        """Tells Pydantic to read data from ORM models."""
        from_attributes = True
