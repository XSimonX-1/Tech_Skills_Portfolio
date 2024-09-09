import mysql.connector
from sqlite3 import OperationalError, ProgrammingError

mysql_blog = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="xxxx",
    database="blog"
)

def get_recipes_number(category_name = '', difficulty_list = [], cost_list = [], max_prep_time = 0) -> int:
    try:
        cursor_blog = mysql_blog.cursor()
        sql_string = ("SELECT count(*) "
                      "FROM recipe AS re ")

        if category_name != '':
            sql_string += f"INNER JOIN category AS ca on re.category_id = ca.category_id and ca.name = '{category_name}' "
        sql_string += "WHERE re.deleted_at is null "

        size = len(difficulty_list)
        if size != 0:
            sql_string += "AND re.difficulty in ("
            for num, diff in enumerate(difficulty_list):
                sql_string += f"'{diff}'"
                if num != size - 1:
                    sql_string += ", "
            sql_string += ") "

        size = len(cost_list)
        if size != 0:
            sql_string += "AND re.cost in ("
            for num, cost in enumerate(cost_list):
                sql_string += f"'{cost}'"
                if num != size - 1:
                    sql_string += ", "
            sql_string += ") "

        if max_prep_time != 0:
            sql_string += f"and re.preparation_time <= {max_prep_time}"

        cursor_blog.execute(sql_string)
        number = cursor_blog.fetchone()
    finally:
        cursor_blog.close()

    return number[0]

def exec_sql_file(sql_file):
    cursor = mysql_blog.cursor()
    print(f"\n[INFO] Executing SQL script file: {sql_file}")
    statement = ""

    with open(sql_file, "r", encoding="UTF-8") as s_file:
        for line in s_file:
            # if line.find("--") == -1:  # ignore sql comment lines
            statement = statement + line
            if line.find(";") > -1:
                try:
                    cursor.execute(statement)
                except (OperationalError, ProgrammingError) as e:
                    print(f"\n[WARN] MySQLError during execute statement \n\tArgs: {str(e.args)}")
                statement = ""


