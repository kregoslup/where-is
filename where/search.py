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

    def _get_pattern_dict(self, path):
        patterns = dict()
        for dir in os.listdir(path):
            stripped = ''.join(x for x in dir if dir.isalpha())
            patterns[stripped] = dir
        return patterns

    def _search(self):
        xdg_conf = self._get_pattern_dict(self.XDG_CONFIG_HOME)
        matches = [re.match(self.name, x) for x in xdg_conf if re.match(self.name, x)]
        if matches:
            return matches, xdg_conf

        # conf_path = os.path.join(self.XDG_CONFIG_HOME, self.name)
        # if os.path.exists(conf_path):
        #     files = os.listdir(conf_path)
        #     for ext in self.CONF_EXTS:
        #         for file in files:
        #             if file.endswith(ext):
        #                 return os.path.join(conf_path, file)

    def get_result(self):
        if self.search_type == self.TYPE_CONF:
            self.result = self._search()

    def format_result(self):
        return "Configuration file path is : {}".format(self.result)
