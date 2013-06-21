# -*- coding: UTF-8 -*-
from datetime import datetime
import json
from pymongo import MongoClient
from lisa import configuration

class Chat:
    def __init__(self):
        self.configuration_lisa = configuration
        mongo = MongoClient(self.configuration_lisa['database']['server'], \
                            self.configuration_lisa['database']['port'])
        self.configuration = mongo.lisa.plugins.find_one({"name": "ChatterBot"})

    def getTime(self):
        now = datetime.now()
        return json.dumps({"plugin": "ChatterBot","method": "getTime", \
                           "body": now.strftime("Il est %H heures et %M minutes")})