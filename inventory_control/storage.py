"""
This is the Storage engine. It's how everything should talk to the database
layer that sits on the inside of the inventory-control system.
"""

import MySQLdb


class StorageEngine(object):
    """
    Instantiate a DB access object, create all the necessary hooks and
    then the accessors to a SQL database.

    """

    def __init__(self, config):
        self.config = config
        self.db = MySQLdb.connect(host=self.config['host'],
                                  user=self.config['user'],
                                  passwd=self.config['password'],
                                  db=self.config['db'])
        self.cursor = self.db.cursor()
