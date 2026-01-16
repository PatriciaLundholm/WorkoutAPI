from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Postgres-exempel, byt ut user/password/dbname
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/workouts"

# Skapa engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Skapa session-klass (som EntityManager i Java)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bas-klass för modeller
Base = declarative_base()
