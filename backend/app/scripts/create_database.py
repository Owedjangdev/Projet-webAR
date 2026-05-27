from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from app.core.config import settings


def main():
    server_url = URL.create(
        drivername="mysql+pymysql",
        username=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
    )

    engine = create_engine(server_url, pool_pre_ping=True)

    with engine.connect() as connection:
        connection.execute(
            text(
                f"CREATE DATABASE IF NOT EXISTS `{settings.db_name}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
        )

    print(f"Base de donnees prete : {settings.db_name}")


if __name__ == "__main__":
    main()
