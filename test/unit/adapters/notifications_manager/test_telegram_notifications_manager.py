from unittest.mock import Mock, patch

from adapters.notifications_manager.telegram_notifications_manager import \
    TelegramNotificationsManager
from elena.adapters.logger.local_logger import LocalLogger


def test_telegram_notifications_manager():
    logger = Mock(spec=LocalLogger)
    config = {
        "TelegramNotificationsManager": {
            "http_api_token": "test_token",
            "chat_id": "test_chat_id",
        }
    }
    sut = TelegramNotificationsManager()
    sut.init(config, logger)

    with patch("requests.get") as mocked_requests_get:
        sut.high("High notification test message")
        sut.medium("Medium notification test message")
        sut.low("Low notification test message")

    assert (
        mocked_requests_get.mock_calls[0]._get_call_arguments()[0][0]
        == "https://api.telegram.org/bottest_token/sendMessage?chat_id=test_chat_id&text=‼️ High notification test message"
    )
    assert (
        mocked_requests_get.mock_calls[1]._get_call_arguments()[0][0]
        == "https://api.telegram.org/bottest_token/sendMessage?chat_id=test_chat_id&text=⚠️ Medium notification test message"
    )
    assert (
        mocked_requests_get.mock_calls[2]._get_call_arguments()[0][0]
        == "https://api.telegram.org/bottest_token/sendMessage?chat_id=test_chat_id&text=Low notification test message"
    )
