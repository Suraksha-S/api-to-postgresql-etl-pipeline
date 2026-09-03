import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

from logger import get_logger

obj_logger = get_logger()

def load_users(df_users):
    obj_logger.info(f"Starting data load: User count - {len(df_users)}")

    if df_users.empty:
        obj_logger.info("No data available for loading")
        return False

    load_dotenv()

    str_db_host = os.getenv("DB_HOST")
    str_db_port = os.getenv("DB_PORT")
    str_db_name = os.getenv("DB_NAME")
    str_db_user = os.getenv("DB_USER")
    str_db_password = os.getenv("DB_PASSWORD")

    str_connection_string = (
        f"postgresql+psycopg2://{str_db_user}:{str_db_password}"
        f"@{str_db_host}:{str_db_port}/{str_db_name}"
    )

    obj_engine = None

    try:
        obj_engine = create_engine(str_connection_string)

        obj_metadata = MetaData() #This helps SQLAlchemy understand database objects.

        #Read the existing users table structure from PostgreSQL.
        obj_users_tabel = Table(
            "users",
            obj_metadata,
            autoload_with = obj_engine
        )

        lst_users_record = df_users.to_dict(orient="records") #Convert DataFrame to Records

        with obj_engine.begin() as obj_connection:
            for dict_user in lst_users_record:

                obj_statement = insert(obj_users_tabel).values(dict_user)

                obj_statement =  obj_statement.on_conflict_do_update(
                    index_elements = ["user_id"],
                    set_={
                        "name":obj_statement.excluded.name,
                        "username":obj_statement.excluded.username,
                        "email":obj_statement.excluded.email
                    }
                )

                obj_connection.execute(obj_statement)

        obj_logger.info(f"Successfully loaded {len(df_users)} users.")
        return True

    except Exception as obj_error:
       obj_logger.error(f"Error while loading data: {obj_error}")
       return False

    finally:
        if obj_engine is not None:
            obj_engine.dispose()