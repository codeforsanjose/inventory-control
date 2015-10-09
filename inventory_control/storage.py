"""
This is the Storage engine. It's how everything should talk to the database
layer that sits on the inside of the inventory-control system.
"""

import sqlite3
import collections

from inventory_control.database import sql


class StorageEngine(object):
    """
    Instantiate a DB access object, create all the necessary hooks and
    then the accessors to a SQL database.

    """

    def __init__(self, config):
        self.config = config
        db_file = self.config.get('db_file', '/tmp/inventory.db')
        self.db = sqlite3.connect(db_file)
        self.cursor = self.db.cursor()

    def _create_tables(self):
        """
        Create all files
        :return:
        """
        for query in sql.CREATE_SQL:
            self.cursor.execute(query)
        self.db.commit()

    def get_components(self, component_type):
        """
        Get all components of a certain type
        :param component_type:
        :return:
        """

    def add_component_type(self, type_name):
        """
        Add a component type that DOESN'T exist in the DB
        :param type_name: Text string of the type.
        :return:
        """
        str = sql.ADD_COMPONENT_TYPE.format(text=type_name)
        self.cursor.execute(str)

    def remove_component_type(self, type_name):
        """
        Given a type name, delete a component type
        that matches it.

        :param type_name: Text field in the DB.
        :return:
        """
        self.cursor.execute(sql.DELETE_COMPONENT_TYPE.format(text=type_name))

    def get_component_type(self, type_name):
        """
        Get a component type based on the type_name

        Returns None if component_type does not exist.

        :param type_name:
        :return:
        """
        self.cursor.execute(sql.GET_COMPONENT_TYPE.format(text=type_name))
        component_type = self.cursor.fetchone()
        if component_type is None:
            return None
        return {'ID': component_type[0], 'type': component_type[1]}

    def add_component(self, sku, type_name, serial_number, status=None):
        """
        Add a new component to the system.

        :param sku: A SKU, a unique product identifier
        :param type_name: A pre-existing component_type
        :param status: Status for the component? Who knows.
        :param serial_number: A serial number for the component if possible
        :return:
        """
        str = sql.ADD_COMPONENT.format(serial_number=serial_number,
                                       sku=sku, type=type_name)
        self.cursor.execute(str)

    def delete_component(self, serial_number=None, id=None):
        """
        Delete a component from the system. This should require
        you to know either the serial number for the component,
        or the DB ID.

        :param serial_number: The serial number of the component
        :param id: The Primary Key ID for the component
        :return:
        """
        raise NotImplementedError()

    def add_project(self, project_number):
        """
        Add a computer project to the DB

        :param project_number: An external identifier. NOT the DB identifier.
        :return:
        """
        str = sql.ADD_PROJECT.format(text=project_number)
        self.cursor.execute(str)

    def delete_project(self, project_number):
        """
        Delete a project from the DB

        :param project_number: External project identifier.
        :return:
        """
        str = sql.DELETE_PROJECT.format(text=project_number)
        self.cursor.execute(str)

    def add_component_to_project(self, project_number, serial_number):
        """
        Given a project number and a serial number, add that component
        with that serial number to that project.

        :param project_number:
        :param serial_number:
        :return:
        """
        query = sql.ADD_COMPONENT_TO_PROJECT.format(
            project_number=project_number,
            serial_number=serial_number
        )
        self.cursor.execute(query)

    def _find_project_by_completeness(self):
        """
        Search for projects and return them by state of completeness
        :return:
        """
        result = self.cursor.execute(sql.GET_PROJECT_BY_STATUS)
        return result.fetchall()


    def find_project_by_completeness(self):
        """
        This is the actual entrypoint which will have to do
        some numerical work.
        :return:
        """

        # TODO: Pull this from get_component_types
        component_types = ['motherboard', 'cpu', 'memory', 'drive',
                           'case']
        results = self._find_project_by_completeness()
        projects = collections.defaultdict(list)
        for x in results:
            if x[1] not in component_types:
                continue
            projects[x[0]].append(x[1])

        projects_by_ncomponents = collections.defaultdict(list)
        for project_id, components in projects.items():
            projects_by_ncomponents[len(components)].append(project_id)

        keys = sorted(projects_by_ncomponents.keys(), reverse=True)
        final_result = []
        for k in keys:
            final_result.extend(projects_by_ncomponents[k])

        return final_result

    def _drop_tables(self):
        """
        Dump all the tables
        :return:
        """
        for query in sql.DROP_SQL:
            self.cursor.execute(query)
        self.db.commit()
