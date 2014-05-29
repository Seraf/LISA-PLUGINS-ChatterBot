# -*- coding: UTF-8 -*-
from datetime import datetime
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os

class ChatterBot(IPlugin):
    def __init__(self):
        super(ChatterBot, self).__init__()
        self.configuration_plugin = self.mongo.lisa.plugins.find_one({"name": "ChatterBot"})
        self.path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
            inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
        self._ = translation = gettext.translation(domain='chatterbot',
                                                   localedir=self.path,
                                                   fallback=True,
                                                   languages=[self.configuration_lisa['lang']]).ugettext

    def getTime(self, jsonInput):
        now = datetime.now()
        return {"plugin": "ChatterBot",
                "method": "getTime",
                "body": now.strftime(self._('It is %H:%M'))
        }

    def sayHello(self, jsonInput):
        return {"plugin": "ChatterBot",
                "method": "sayHello",
                "body": self._('Hello. How are you ?')
        }