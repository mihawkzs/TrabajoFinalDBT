from airflow.models.connection import Connection
from airflow.utils.db import provide_session
from airflow.settings import Session

@provide_session
def add_snowflake_connection(session: Session):
    conn = Connection(
        conn_id="snowflake_conn",
        conn_type="snowflake",
        host="kt98194.us-east4.gcp",
        schema="dbt_db",
        login="<IsmaelRT>",
        password="Ismael01",
        extra='{"warehouse": "dbt_wh", "role": "dbt_role", "insecure_mode": false}'
    )
    session.add(conn)
    session.commit()

add_snowflake_connection()
