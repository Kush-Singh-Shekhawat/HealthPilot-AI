from database.db import Base, engine

# Import all models so SQLAlchemy registers them
import database.models


def init_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")