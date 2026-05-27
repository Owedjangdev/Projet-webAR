from app.db.database import Base, engine
from app import models


def main():
    Base.metadata.create_all(bind=engine)
    print("Tables creees avec succes.")


if __name__ == "__main__":
    main()
