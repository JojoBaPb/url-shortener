from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Holds application settings.
    """
    # This tells pydantic-settings to load variables from a .env file
    model_config = SettingsConfigDict(env_file=".env")
    
    # This variable MUST match the one in your .env file
    # Pydantic will automatically validate it as a string.
    database_url: str

# Create a single, reusable instance of the settings
settings = Settings()
