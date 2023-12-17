import requests
from elena.domain.ports.logger import Logger
from elena.domain.ports.notifications_manager import NotificationsManager


class TelegramNotificationsManager(NotificationsManager):
    _logger: Logger
    _http_api_token: str
    _chat_id: int

    def _send(self, msg):
        url = f"https://api.telegram.org/bot{self._http_api_token}/sendMessage?chat_id={self._chat_id}&text={msg}"
        requests.get(url)

    def init(self, config: dict, logger: Logger):
        self._logger = logger
        self._http_api_token = config["TelegramNotificationsManager"]["http_api_token"]
        self._chat_id = config["TelegramNotificationsManager"]["chat_id"]

    def high(self, notification: str):
        msg = f"‼️ {notification}"
        self._logger.info(msg)
        self._send(msg)

    def medium(self, notification: str):
        msg = f"⚠️ {notification}"
        self._logger.info(msg)
        self._send(msg)

    def low(self, notification: str):
        msg = f"{notification}"
        self._logger.info(msg)
        self._send(msg)
