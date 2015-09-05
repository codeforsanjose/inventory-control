"""
So this is where all the SQL commands live
"""

CREATE_SQL = """
CREATE TABLE component_type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(255) UNIQUE
);


CREATE TABLE components (
    id INT PRIMARY KEY AUTO_INCREMENT,
    serial_number VARCHAR(255),
    sku TEXT,
    type INT,
    status INT,
    FOREIGN KEY (type) REFERENCES component_type(id)
);

CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_number INT,
    motherboard INT,
    power_supply INT,
    cpu INT,
    hard_drive INT,
    proj_case INT,
    memory INT,
    FOREIGN KEY (motherboard) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (cpu) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (power_supply) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (hard_drive) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (proj_case) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (memory) REFERENCES components(id) ON DELETE CASCADE
);
"""

ADD_COMPONENT_TYPE = """INSERT IGNORE INTO component_type (type) VALUES ('{text}')
"""

GET_COMPONENT_TYPE="""SELECT * FROM component_type WHERE type='{text}'"""

DELETE_COMPONENT_TYPE = """DELETE FROM component_type WHERE type='{text}'
"""

SELECT_ALL_COMPONENTS = """
SELECT * FROM components INNER JOIN component_type
 ON components.type = component_type.id;
 """


DROP_SQL = """
DROP TABLE projects;
DROP TABLE components;
DROP TABLE component_type;
"""
