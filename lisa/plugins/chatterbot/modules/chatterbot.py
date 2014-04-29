# -*- coding: UTF-8 -*-
from datetime import datetime
import json, os, inspect
from lisa.server.plugins.IPlugin import IPlugin
import gettext

path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
    inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
_ = translation = gettext.translation(domain='chat', localedir=path, languages=[configuration['lang']]).ugettext

class ChatterBot(IPlugin):
    def __init__(self, lisa=None):
        super(ChatterBot, self).__init__()
        self.configuration = mongo.lisa.plugins.find_one({"name": "ChatterBot"})

    def getTime(self, jsonInput):
        now = datetime.now()
        return {"plugin": "ChatterBot",
                "method": "getTime",
                "body": now.strftime(_('time'))
        }

    def sayHello(self, jsonInput):
        return {"plugin": "ChatterBot",
                "method": "sayHello",
                "body": _('Hello. How are you ?')
        }