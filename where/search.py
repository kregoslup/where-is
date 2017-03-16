import os
import re


class Search:
    CONF_EXTS = (
        'ini',
        'conf.d',
        'properties',
        'yml',
        'json'
    )
    XDG_DATA_HOME = '~/.local/share'
    XDG_CONFIG_HOME = '~/.config'
    XDG_DATA_DIRS = '/usr/local/share/:/usr/share/'
    XDG_CONFIG_DIRS = '/etc/xdg'
    HOME = '~/'
    GLOBAL_CONF = '/etc'

    TYPE_CONF = 'conf'
    TYPE_LOG = 'conf'

    def __init__(self, name, type=None):
        self.name = ''.join(x for x in name if x.isalnum())
        if not type:
            self.search_type = self.TYPE_CONF
        self.result = None

    def _search(self):
        conf_path = os.path.join(self.XDG_CONFIG_HOME, self.name)
        if os.path.exists(conf_path):
            files = os.listdir(conf_path)
            for ext in self.CONF_EXTS:
                for file in files:
                    if file.endswith(ext):
                        return os.path.join(conf_path, file)

    def get_result(self):
        if self.search_type == self.TYPE_CONF:
            self.result = self._search()

    def format_result(self):
        return "Configuration file path is : {}".format(self.result)
