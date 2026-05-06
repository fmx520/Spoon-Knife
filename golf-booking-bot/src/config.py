from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    username: str = ""
    password: str = ""
    course_name: str = ""
    preferred_date: str = ""
    preferred_time_start: str = "06:00"
    preferred_time_end: str = "10:00"


class TeeTime(BaseModel):
    course: str
    date: str
    time: str
    slots: int
