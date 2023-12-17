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

    sut.high("High notification")
    sut.medium("Medium notification")
    sut.low("Low notification")

    assert logger.mock_calls[0]._get_call_arguments() == (
        ("High notification '%s'", "High notification"),
        {},
    )
    assert logger.mock_calls[1]._get_call_arguments() == (
        ("Medium notification '%s'", "Medium notification"),
        {},
    )
    assert logger.mock_calls[2]._get_call_arguments() == (
        ("Low notification '%s'", "Low notification"),
        {},
    )
