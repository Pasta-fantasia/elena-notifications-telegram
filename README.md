# elena-notifications-telegram
Notifications implementation for Telegram

1. Make sure to have a secrets.yaml in test/elena/domain/services/test_home (it doesn't need real exchange info)
2. Set your ELENA_HOME to the folder you put that config.yaml 

# Installation for developing
- On Pycharm clone elena and elena_notifications_telegram.
- To test the strategy create a virtual env on elena_notifications_telegram and from the Pycharm terminal (making sure that the venv is active) run
```
pip install --upgrade pip
pip install -U setuptools wheel
pip install -e ../elena
pip install -r requirements.txt
pip install -r requirements_test.txt
```
