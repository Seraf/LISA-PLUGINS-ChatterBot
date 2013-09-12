# -*- coding: UTF-8 -*-
from datetime import datetime
import json, os, inspect
from pymongo import MongoClient
from lisa import configuration

import gettext

path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
    inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
_ = translation = gettext.translation(domain='chat', localedir=path, languages=[configuration['lang']]).ugettext

class ChatterBot:
    def __init__(self, lisa):
        self.lisa = lisa
        self.configuration_lisa = configuration
        mongo = MongoClient(host=self.configuration_lisa['database']['server'],
                            port=self.configuration_lisa['database']['port'])
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