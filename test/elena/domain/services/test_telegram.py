import pathlib
from os import path

from elena.adapters.bot_manager.local_bot_manager import LocalBotManager
from elena.adapters.config.local_config_reader import LocalConfigReader
from elena.domain.model.bot_config import BotConfig
from elena.domain.model.bot_status import BotStatus
from elena.domain.ports.exchange_manager import ExchangeManager
from elena.domain.ports.logger import Logger
from elena.domain.ports.metrics_manager import MetricsManager
from elena.domain.ports.notifications_manager import NotificationsManager
from elena.domain.ports.strategy_manager import StrategyManager
from elena.domain.services.elena import Elena
from elena.domain.services.generic_bot import GenericBot
from elena.shared.dynamic_loading import get_instance


class TelegramNotificationTest(GenericBot):


    def init(
        self,
        manager: StrategyManager,
        logger: Logger,
        metrics_manager: MetricsManager,
        notifications_manager: NotificationsManager,
        exchange_manager: ExchangeManager,
        bot_config: BotConfig,
        bot_status: BotStatus,
    ):  # type: ignore
        super().init(
            manager,
            logger,
            metrics_manager,
            notifications_manager,
            exchange_manager,
            bot_config,
            bot_status,
        )

        # Verify that the exchange is in sandbox mode!!!!
        if not self.exchange.sandbox_mode:
            raise Exception(
                "Exchange is not in sandbox mode, this strategy is ment for testing only!"
            )

    def next(self) -> BotStatus:
        self._logger.info("%s strategy: processing next cycle ...", self.name)

        # Send some notification


        return self.status


def test_elena():
    test_home_dir = path.join(pathlib.Path(__file__).parent, "test_home")
    config = LocalConfigReader(test_home_dir).config

    logger = get_instance(config["Logger"]["class"])
    logger.init(config)

    metrics_manager = get_instance(config["MetricsManager"]["class"])
    metrics_manager.init(config, logger)

    notifications_manager = get_instance(config["NotificationsManager"]["class"])
    notifications_manager.init(config, logger)

    bot_manager = LocalBotManager(
        config, logger, metrics_manager, notifications_manager
    )
    exchange_manager = ExchangeManager(config, logger)

    sut = Elena(
        config=config,
        logger=logger,
        metrics_manager=metrics_manager,
        notifications_manager=notifications_manager,
        bot_manager=bot_manager,
        exchange_manager=exchange_manager,
    )

    sut.run()
