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
