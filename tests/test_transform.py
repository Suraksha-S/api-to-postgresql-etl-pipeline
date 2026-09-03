import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent / "src")
)

from transform import transform_users


def test_transform_users():
    lst_users = [
        {
            "id": 1,
            "name": "  John Doe  ",
            "username": " johndoe ",
            "email": " JOHN@EMAIL.COM "
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "username": "janedoe",
            "email": "JANE@EMAIL.COM"
        }
    ]

    df_result = transform_users(lst_users)

    # Verify record count
    assert len(df_result) == 2

    # Verify column names
    assert list(df_result.columns) == [
        "user_id",
        "name",
        "username",
        "email"
    ]

    # Verify name cleaning
    assert df_result.iloc[0]["name"] == "John Doe"

    # Verify username cleaning
    assert df_result.iloc[0]["username"] == "johndoe"

    # Verify email standardization
    assert df_result.iloc[0]["email"] == "john@email.com"

    def test_transform_empty_users():
        lst_users = []

        df_result = transform_users(lst_users)

        assert df_result.empty


def test_transform_missing_required_values():
    lst_users = [
        {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@email.com"
        },
        {
            "id": 2,
            "name": None,
            "username": "janedoe",
            "email": "jane@email.com"
        }
    ]

    df_result = transform_users(lst_users)

    assert len(df_result) == 1
    assert df_result.iloc[0]["user_id"] == 1


def test_transform_duplicate_users():
    lst_users = [
        {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@email.com"
        },
        {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@email.com"
        }
    ]

    df_result = transform_users(lst_users)

    assert len(df_result) == 1