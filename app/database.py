from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Postgres-exempel, byt ut user/password/dbname
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/workouts"

# kopplar python til databasen
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# använder detta för att öppna databas sessioner i varje request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# alla modeller (workout,exercise) ärver från denna
Base = declarative_base()
