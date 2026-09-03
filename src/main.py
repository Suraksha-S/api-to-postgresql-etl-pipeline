from extract import extract_users
from transform import transform_users
from load import load_users

from logger import get_logger

obj_logger = get_logger()

def main():
    obj_logger.info("Starting ETL pipeline...")

    #Extract
    lst_users = extract_users()

    # print("Extracted Users:")
    # for dict_user in lst_users:
    #     print(dict_user)

    #Transform
    df_users = transform_users(lst_users)

    obj_logger.info('Transformed users:')
    obj_logger.info(df_users)

    #Load users
    b_load_success = load_users(df_users)

    if b_load_success:
        obj_logger.info("ETL pipeline completed successfully")
    else:
        obj_logger.error("ETL pipeline failed during load stage")

    

if __name__ == "__main__":
    main()