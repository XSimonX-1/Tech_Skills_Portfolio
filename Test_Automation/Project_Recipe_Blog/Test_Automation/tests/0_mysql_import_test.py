from database.database_methods import exec_sql_file
import os

exec_sql_file(os.path.join(os.path.dirname(__file__), "../dump2.sql"))
