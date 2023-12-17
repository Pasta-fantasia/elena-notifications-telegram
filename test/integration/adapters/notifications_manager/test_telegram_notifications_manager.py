import pathlib
from os import path
from unittest.mock import Mock

from elena.adapters.config.local_config_reader import LocalConfigReader
from elena.shared.dynamic_loading import get_instance


def test_telegram_notifications_manager():
    test_home_dir = path.join(pathlib.Path(__file__).parent, "test_home")
    config = LocalConfigReader(test_home_dir).config

    logger = Mock()

    sut = get_instance(config["NotificationsManager"]["class"])
    sut.init(config, logger)

    sut.high("High notification test message")
    sut.medium("Medium notification test message")
    sut.low("Low notification test message")

    assert (
        logger.mock_calls[0]._get_call_arguments()[0][0]
        == "‼️ High notification test message"
    )
    assert (
        logger.mock_calls[1]._get_call_arguments()[0][0]
        == "⚠️ Medium notification test message"
    )
    assert (
        logger.mock_calls[2]._get_call_arguments()[0][0]
        == "Low notification test message"
    )
