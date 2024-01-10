import pathlib
from os import path
from unittest.mock import Mock

from elena.domain.ports.logger import Logger
from elena.domain.ports.storage_manager import StorageManager
from elena.domain.services.elena import (get_config_manager,
                                         get_notifications_manager)


def test_telegram_notifications_manager():
    config_manager = get_config_manager(
        config_manager_class_path="elena.adapters.config.local_config_manager.LocalConfigManager",
        config_manager_url=path.join(
            pathlib.Path(__file__).parent.parent.parent, "test_home"
        ),
    )
    config = config_manager.get_config()
    logger = Mock(spec=Logger)
    sut = get_notifications_manager(config, logger, Mock(spec=StorageManager))

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
