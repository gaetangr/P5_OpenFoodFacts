"""Main launcher of the PurBeurre application."""

from .controller import UserMenu


def main():
    """Entry point of the PurBeurre application."""
    user_menu = UserMenu()
    user_menu.start()


if __name__ == "__main__":
    main()

