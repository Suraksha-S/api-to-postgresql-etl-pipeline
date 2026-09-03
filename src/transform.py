import pandas as pd

from logger import get_logger

obj_logger = get_logger()

def transform_users(lst_users):
    obj_logger.info(f"Starting data transformation.  User count: {len(lst_users)}")

    if not lst_users:
        obj_logger.info("No data available for the transformation")
        return pd.DataFrame()

    df_users = pd.DataFrame(lst_users)
    obj_logger.info(f"Initial dataframe record count {len(df_users)}")

    #Select required fields
    df_users = df_users[["id", "name", "username", "email"]]

    #Rename column
    df_users = df_users.rename(
        columns={
            "id":"user_id"
        }
    )

    #Remove duplicate
    df_users=df_users.drop_duplicates()

    #Remove leading and trailing spaces
    df_users["name"]= df_users["name"].str.strip()
    df_users["username"] = df_users["username"].str.strip()

    #Standardize email format
    df_users["email"] = df_users["email"].str.strip().str.lower()

    #Remove record with missing required value
    df_users = df_users.dropna(
        subset=["user_id", "name", "email"]
    )

    obj_logger.info(f"Transformed dataframe record count {len(df_users)}")

    return df_users