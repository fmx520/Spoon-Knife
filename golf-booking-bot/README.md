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

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
```

## Project Layout
- `src/main.py`: Entrypoint for bot runtime
- `src/config.py`: Environment-based configuration
- `src/booking.py`: Core booking workflow placeholder
- `tests/`: Unit tests

## Next Steps
1. Add target booking website support.
2. Implement authentication flow.
3. Implement tee-time search and booking actions.
4. Add retries, rate limits, and logging.
