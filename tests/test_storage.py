import pytest

from inventory_control import storage

def test_integration_storage():

    config = {'host': 'localhost', 'user': 'wce',
              'password': 'thispasswordisobjectivelyterrible',
              'db': 'inventory_control'}
    engine = storage.StorageEngine(config=config)
    result = engine.cursor.execute("SELECT COUNT(*) FROM test")
    assert result == 1

    try:
        #engine._drop_tables()
        engine._create_tables()
        res = engine.cursor.execute("SELECT * FROM components")
        assert res == 0
        res = engine.cursor.execute("SELECT * FROM projects")
        assert res == 0
    except Exception as ex:
        print(ex)
    finally:
        engine._drop_tables()
