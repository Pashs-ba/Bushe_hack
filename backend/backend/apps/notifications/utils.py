from typing import Iterable

from .models import Notification


def notify_users(users: Iterable[Notification], title: str, text: str = ""):
    """
    Send a notification to a group of users.

    Args:
        users: Iterable of users to send the notification to.
        text: Text of the notification.
        title: Title of the notification.
    """
    msgs = [Notification(user=user, title=title, text=text) for user in users]
    Notification.objects.bulk_create(msgs)


def send_message_to_user(user: Notification, title: str, text: str = ""):
    """
    Send a notification to a user.

    Args:
        user: User to send the notification to.
        text: Text of the notification.
        title: Title of the notification.
    """
    Notification.objects.create(user=user, title=title, text=text)
