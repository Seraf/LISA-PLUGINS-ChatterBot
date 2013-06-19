# -*- coding: UTF-8 -*-
from datetime import datetime
import json
from pymongo import MongoClient
from jarvis import configuration

class Chat:
    def __init__(self):
        self.configuration_jarvis = configuration
        mongo = MongoClient(self.configuration_jarvis['database']['server'], \
                            self.configuration_jarvis['database']['port'])
        self.configuration = mongo.jarvis.plugins.find_one({"name": "ChatterBot"})

    def getTime(self):
        now = datetime.now()
        return json.dumps({"plugin": "ChatterBot","method": "getTime", \
                           "body": now.strftime("Il est %H heures et %M minutes")})