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

    CONF_PATHS = (
        XDG_CONFIG_HOME,
        GLOBAL_CONF,
        HOME
    )

    LOG_PATHS = (
        '/var/log'
    )

    TYPE_CONF = 'conf'
    TYPE_LOG = 'conf'

    def __init__(self, name, type=None):
        self.name = ''.join(x for x in name if x.isalnum())
        if not type:
            self.search_type = self.TYPE_CONF
        self.result = None

    @classmethod
    def _get_pattern_dict(cls, path):
        patterns = dict()
        for dir in os.listdir(path):
            stripped = ''.join(x for x in dir if dir.isalpha())
            patterns[dir] = stripped
        return patterns

    def _search(self):
        if self.search_type == self.TYPE_CONF:
            confs_path = self.CONF_PATHS
        if self.search_type == self.TYPE_CONF:
            confs_path = self.CONF_PATHS
        for conf_path in confs_path:
            dirs = self._get_pattern_dict(conf_path)
            matches = [re.match(self.name, x) for x in dirs.values() if re.match(self.name, x)]
            if matches:
                return matches, dirs

    def get_result(self):
        matches, dirs = self._search()

    def format_result(self):
        return "Configuration file path is : {}".format(self.result)
