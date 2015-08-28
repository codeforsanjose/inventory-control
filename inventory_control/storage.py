"""
This is the Storage engine. It's how everything should talk to the database
layer that sits on the inside of the inventory-control system.
"""

import MySQLdb

from inventory_control.database import sql


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

    def _create_tables(self):
        """
        Create all files
        :return:
        """
        self.cursor.execute(sql.CREATE_SQL)
        self.cursor.close()
        self.db.commit()
        self.cursor = self.db.cursor()

    def get_components(self, component_type):
        """
        Get all components of a certain type
        :param component_type:
        :return:
        """

    def _drop_tables(self):
        """
        Dump all the tables
        :return:
        """
        self.cursor.execute(sql.DROP_SQL)
        self.cursor.close()
        self.db.commit()
        self.cursor= self.db.cursor()