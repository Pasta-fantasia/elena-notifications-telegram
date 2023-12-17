import pathlib
from test.elena.domain.services.fake_exchange_manager import \
    FakeExchangeManager

from elena.adapters.bot_manager.local_bot_manager import LocalBotManager
from elena.adapters.config.local_config_reader import LocalConfigReader
from elena.adapters.logger.local_logger import LocalLogger
from elena.domain.model.bot_config import BotConfig
from elena.domain.model.bot_status import BotStatus
from elena.domain.ports.exchange_manager import ExchangeManager
from elena.domain.ports.logger import Logger
from elena.domain.ports.strategy_manager import StrategyManager
from elena.domain.services.elena import Elena
from elena.domain.services.generic_bot import GenericBot


class TelegramNotificationTest(GenericBot):
    def init(
        self,
        manager: StrategyManager,
        logger: Logger,
        exchange_manager: ExchangeManager,
        bot_config: BotConfig,
        bot_status: BotStatus,
    ):  # type: ignore
        super().init(manager, logger, exchange_manager, bot_config, bot_status)


        # Verify that the exchange is in sandbox mode!!!!
        if not self.exchange.sandbox_mode:
            raise Exception(
                "Exchange is not in sandbox mode, this strategy is ment for testing only!"
            )

    def next(self) -> BotStatus:
        self._logger.info("%s strategy: processing next cycle ...", self.name)

        # 1 - INFO

        return self.status


def test_elena():
    home = pathlib.Path(__file__).parent.parent.parent.__str__()
    config = LocalConfigReader(home).config
    logger = LocalLogger(config)
    bot_manager = LocalBotManager(config, logger)
    exchange_manager = FakeExchangeManager(config, logger)

    sut = Elena(
        config=config,
        logger=logger,
        bot_manager=bot_manager,
        exchange_manager=exchange_manager,
    )

    sut.run()
