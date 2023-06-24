from enum import Enum
import hashlib
import hmac
import time
from django.conf import settings


class UserTypes(Enum):
    """User types."""

    ROOT = 0
    MANAGER = 1
    COURIER = 2


ACCOUNT_TYPE_CHOICES = (
    (UserTypes.ROOT.value, "Root"),
    (UserTypes.MANAGER.value, "Менеджер"),
    (UserTypes.COURIER.value, "Курьер"),
)


TG_AUTH_DURATION = 86400 * 3


def verify_telegram_authentication(request_data):
    """
    Check if received data from Telegram is real.

    Based on SHA and HMAC algothims.
    Instructions - https://core.telegram.org/widgets/login#checking-authorization
    """
    request_data = request_data.copy()

    received_hash = request_data["hash"]
    auth_date = request_data["auth_date"]

    request_data.pop("hash", None)
    request_data_alphabetical_order = sorted(request_data.items(), key=lambda x: x[0])

    data_check_string = []

    for data_pair in request_data_alphabetical_order:
        key, value = data_pair
        data_check_string.append(key + "=" + str(value))

    data_check_string = "\n".join(data_check_string)

    secret_key = hashlib.sha256(settings.TELEGRAM_BOT_TOKEN.encode()).digest()
    _hash = hmac.new(secret_key, msg=data_check_string.encode(),
                     digestmod=hashlib.sha256).hexdigest()

    unix_time_now = int(time.time())
    unix_time_auth_date = int(auth_date)

    if unix_time_now - unix_time_auth_date > TG_AUTH_DURATION:
        raise Exception(
            "Authentication data is outdated. Authentication was received more than day ago."
        )

    if _hash != received_hash:
        raise Exception(
            "This is not a Telegram data. Hash from recieved authentication data does not match"
            "with calculated hash based on bot token."
        )

    return request_data
