from inventory_control import storage


def get_config():
    """
    Create my simple localhost config
    :return:
    """

    config = {'host': 'localhost', 'user': 'wce',
              'password': 'thispasswordisobjectivelyterrible',
              'db': 'inventory_control'}
    return config


def test_integration_storage():

    engine = storage.StorageEngine(config=get_config())

    try:
        engine._create_tables()
        res = engine.cursor.execute("SELECT * FROM components")
        assert res.fetchone() is None
        res = engine.cursor.execute("SELECT * FROM projects")
        assert res.fetchone() is None
    except Exception as ex:
        print(ex)
    finally:
        engine._drop_tables()


def test_integration_component_creation():
    """
    Create a component type, get it, and delete it.
    :return:
    """

    name = 'some_name'
    engine = storage.StorageEngine(config=get_config())
    try:
        engine._create_tables()
        engine.add_component_type(type_name=name)
        result = engine.get_component_type(type_name=name)
        assert result['type'] == name
        engine.remove_component_type(type_name=name)
        result = engine.get_component_type(type_name=name)
        assert result is None
    finally:
        engine._drop_tables()


def test_project():
    """
    Create a project, delete a project, and possibly
    rank them in order

    :return:
    """
    engine = storage.StorageEngine(config=get_config())
    project_number = 1001
    try:
        engine._create_tables()
        engine.add_project(project_number=project_number)
        engine.delete_project(project_number=project_number)
    finally:
        engine._drop_tables()


def test_full_run():
    """
    Create components, add them to the system.
    :return:
    """

    engine = storage.StorageEngine(config=get_config())
    try:
        engine._create_tables()
        engine.add_component_type(type_name='motherboard')
        engine.add_component_type(type_name='cpu')
        engine.add_component_type(type_name='memory')
        engine.add_component_type(type_name='drive')
        engine.add_component(sku='sku00', type_name='motherboard',
                             serial_number='serial00')
        engine.add_component(sku='sku01', type_name='cpu',
                             serial_number='serial01')
        engine.add_component(sku='sku02', type_name='memory',
                             serial_number='serial02')
        engine.add_component(sku='sku03', type_name='drive',
                             serial_number='serial03')
        engine.add_component(sku='sku10', type_name='motherboard',
                             serial_number='serial10')
        engine.add_component(sku='sku11', type_name='cpu',
                             serial_number='serial11')
        engine.add_component(sku='sku12', type_name='memory',
                             serial_number='serial12')
        engine.add_component(sku='sku13', type_name='drive',
                             serial_number='serial13')
        engine.add_project(project_number='project0')
        engine.add_project(project_number='project1')
        engine.add_component_to_project(project_number='project0',
                                        serial_number='serial00')
        engine.add_component_to_project(project_number='project0',
                                        serial_number='serial01')
        engine.add_component_to_project(project_number='project0',
                                        serial_number='serial02')
        engine.add_component_to_project(project_number='project0',
                                        serial_number='serial03')
        engine.add_component_to_project(project_number='project1',
                                        serial_number='serial10')
        engine.add_component_to_project(project_number='project1',
                                        serial_number='serial11')
        result = engine._find_project_by_completeness()
        assert ('project0', 'motherboard') in result
        assert ('project1', 'memory') not in result
        result = engine.find_project_by_completeness()
        assert result == ['project0', 'project1']
    except:
        raise
    finally:
        engine._drop_tables()
