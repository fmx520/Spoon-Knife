# Create `golf-booking-bot` as a separate GitHub repository

The previous change added bot files inside this repo. This guide moves that work to a standalone repository.

## 1) Create the repo on GitHub
Create a new empty repository named `golf-booking-bot` in your GitHub account (no README/license/gitignore needed).

## 2) Scaffold locally and push
Run these commands locally (replace `YOUR_GITHUB_USERNAME`):

```bash
mkdir -p ~/code/golf-booking-bot
cd ~/code/golf-booking-bot
git init -b main

mkdir -p src tests
cat > README.md <<'MD'
# Golf Booking Bot

A starter repository for building an automated golf tee-time booking bot.

## Goals
- Search available tee times
- Filter by course/date/time/preferences
- Automatically submit bookings
- Notify user of booking confirmation or failures

## Suggested Stack
- Python 3.12+
- Playwright for browser automation
- Pydantic for configuration
- pytest for tests
MD

cat > requirements.txt <<'REQ'
playwright==1.55.0
pydantic==2.11.7
python-dotenv==1.0.1
pydantic-settings==2.10.1
REQ

cat > .gitignore <<'GI'
.venv/
__pycache__/
*.pyc
.env
playwright-report/
GI

cat > src/config.py <<'PY'
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
PY

cat > src/booking.py <<'PY'
from .config import BotSettings, TeeTime


def find_candidate_tee_time(settings: BotSettings) -> TeeTime | None:
    if not settings.course_name or not settings.preferred_date:
        return None

    return TeeTime(
        course=settings.course_name,
        date=settings.preferred_date,
        time=settings.preferred_time_start,
        slots=2,
    )


def book_tee_time(settings: BotSettings) -> bool:
    tee_time = find_candidate_tee_time(settings)
    return tee_time is not None
PY

cat > src/main.py <<'PY'
from .booking import book_tee_time
from .config import BotSettings


def main() -> None:
    settings = BotSettings()
    success = book_tee_time(settings)
    print("Booking workflow completed (placeholder)." if success else "No suitable tee time found.")


if __name__ == "__main__":
    main()
PY

cat > tests/test_booking.py <<'PY'
from src.booking import find_candidate_tee_time
from src.config import BotSettings


def test_find_candidate_tee_time_returns_none_without_required_fields() -> None:
    settings = BotSettings(course_name="", preferred_date="")
    assert find_candidate_tee_time(settings) is None


def test_find_candidate_tee_time_returns_value_with_required_fields() -> None:
    settings = BotSettings(course_name="Pebble Beach", preferred_date="2026-06-01")
    tee_time = find_candidate_tee_time(settings)
    assert tee_time is not None
    assert tee_time.course == "Pebble Beach"
PY

git add .
git commit -m "Initial scaffold for golf booking bot"
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/golf-booking-bot.git
git push -u origin main
```
