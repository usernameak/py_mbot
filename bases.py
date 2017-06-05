import json


class BaseTelegramModule(object):
    """Base class which represents module

    Attributes:
        _telegram_api(:class:`api.TelegramAPI`): Telegram API object which is used in module
        friendly_name(str): friendly name that will be shown in list
        disabled(bool): when this evaluates to ``True``, module is considered disabled

    Args:
        telegram_api(:class:`api.TelegramAPI`): Telegram API object to use in module

    """

    def __init__(self, telegram_api):
        self._telegram_api = telegram_api
        self.friendly_name = None
        self.disabled = False

    def help(self, message, args):
        """Answers to `/help` message

        Args:
            message(:class:`telegram.Message`): received message
            args(list): message arguments

        """
        raise NotImplementedError('This method must be implemented')


class JSONAPI(object):
    """This class represents base for APIs that work with JSON files

    Attributes:
        raw_data: read-only raw data from file

    Args:
        directory(str): directory to use for finding a file
        name(str): name of file without ``.json` extension

    Raises:
        FileNotFoundError: when specified file cannot be found

    """
    def __init__(self, directory, name):
        with open('./{0}/{1}.json'.format(directory, name), 'r') as f:
            self._raw_data = json.load(f)

    def __getitem__(self, item):
        return self._raw_data.get(item.lower(), None)

    @property
    def raw_data(self):
        return self._raw_data
