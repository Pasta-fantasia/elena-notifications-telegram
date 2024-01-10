# elena-notifications-telegram

Notifications implementation for Telegram

## Telegram configuration

1. Create a telegram group in Which you will receive Elena related messages
2. Set up the telegram Bot:
   1. Search `BotFather` chat in Telegram
   2. Send `/newbot` command and give it a name and username
   3. Store the HTTP API token
3. Get the chat ID of the group:
   1. Add the bot to the group you created in step 1
   2. Send this message to the group: `/my_id <@your_bot_username>`
   3. Go to `https://api.telegram.org/bot<YourBOTToken>/getUpdates` and get the chat ID from the response.
   4. If you didn't receive any message, send again the step 3.2. message to the group and try again.
   5. Copy the chat ID and store it from field `result.message.chat.id`
4. Edit your `secrets.yaml` file in `ELENA_HOME` directory with the values you got in steps 2 and 3:
   ```yaml
   NotificationsManager:
     class: elena_notifications_telegram.adapters.notifications_manager.telegram_notifications_manager.TelegramNotificationsManager
     http_api_token: PUT_HERE_YOUR_TELEGRAM_BOT_API_TOKEN
     chat_id: PUT_HERE_YOUR_TELEGRAM_CHAT_ID
   ```
   
## Installation for developing

- On Pycharm clone elena and elena_notifications_telegram.
- Create a virtual env on elena_notifications_telegram and from the Pycharm terminal (making sure that the venv is active) run `make install`
- To run integration test, on `/test/integration/test_home` copy the sample file `secrets-sample.yaml` to `secrets.yaml` and configure your Telegram access configuration as explained before (it doesn't need real exchange info)
