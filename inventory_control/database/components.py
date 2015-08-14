"""
So this is where all the SQL commands for the Component Stuff exists
"""

CREATE_SQL = """
CREATE TABLE components (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sku TEXT,
    type INT,
    status INT
);

CREATE TABLE component_type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type TEXT
);
"""

SELECT_ALL_COMPONENTS = """
SELECT * FROM components INNER JOIN component_type
 ON components.type = component_type.id;
 """


DROP_SQL = """
DROP TABLE components;
DROP TABLE component_type;
"""
