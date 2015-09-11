"""
So this is where all the SQL commands live
"""

CREATE_SQL = ("""
CREATE TABLE component_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(255) UNIQUE
);
""",
"""
CREATE TABLE components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number VARCHAR(255),
    sku TEXT,
    type INTEGER,
    status INTEGER,
    FOREIGN KEY (type) REFERENCES component_type(id)
);
""",
"""
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_number INTEGER,
    motherboard INTEGER,
    power_supply INTEGER,
    cpu INTEGER,
    hard_drive INTEGER,
    proj_case INTEGER,
    memory INTEGER,
    FOREIGN KEY (motherboard) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (cpu) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (power_supply) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (hard_drive) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (proj_case) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (memory) REFERENCES components(id) ON DELETE CASCADE
);
""")

ADD_COMPONENT_TYPE = """INSERT INTO component_type (type) VALUES ('{text}')
"""

GET_COMPONENT_TYPE="""SELECT * FROM component_type WHERE type='{text}'"""

DELETE_COMPONENT_TYPE = """DELETE FROM component_type WHERE type='{text}'
"""

SELECT_ALL_COMPONENTS = """
SELECT * FROM components INNER JOIN component_type
 ON components.type = component_type.id;
 """

# Project SQL
ADD_PROJECT = "INSERT INTO projects (product_number) VALUES ('{text}')"

DELETE_PROJECT = """
DELETE FROM projects WHERE product_number='{text}'
"""

GET_PROJECT_BY_STATUS = """
"""

DROP_SQL = ("DROP TABLE projects",
            "DROP TABLE components",
            "DROP TABLE component_type")
