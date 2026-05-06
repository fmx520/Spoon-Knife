from .booking import book_tee_time
from .config import BotSettings


def main() -> None:
    settings = BotSettings()
    success = book_tee_time(settings)

    if success:
        print("Booking workflow completed (placeholder).")
    else:
        print("No suitable tee time found. Check your configuration.")


if __name__ == "__main__":
    main()
