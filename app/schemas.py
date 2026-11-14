from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class URLBase(BaseModel):
    target_url: HttpUrl = Field(
        ...,
        title="Target URL",
        description="The original long URL you want to shorten.",
    )


class URLCreate(URLBase):
    """What the client sends to create a link."""


class URLInfo(URLBase):
    """What we send back, including the private secret_key."""

    model_config = ConfigDict(from_attributes=True)

    is_active: bool = Field(..., title="Is Active")
    clicks: int = Field(..., title="Click Count")
    key: str = Field(..., title="Short Code")
    secret_key: str = Field(..., title="Secret Management Key")
