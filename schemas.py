from pydantic import BaseModel, HttpUrl, Field

class URLBase(BaseModel):
    """
    Base schema for a URL with strictly documented fields.
    """
    target_url: HttpUrl = Field(
        ..., 
        title="Target URL", 
        description="The original long URL you want to shorten."
    )

class URLCreate(URLBase):
    """Schema for creating a new URL."""
    pass

class URLInfo(URLBase):
    """
    Schema for returning URL info, including the private secret_key.
    This is only returned once upon creation.
    """
    is_active: bool = Field(..., title="Is Active")
    clicks: int = Field(..., title="Click Count")
    key: str = Field(..., title="Short Code")
    secret_key: str = Field(..., title="Secret Management Key")

    class Config:
        from_attributes = True
