# from sqlalchemy import text
# from app import db, app

# sql = open("seed_data.sql", "r")
# statement = sql.read()

# with app.app_context():
#     db.session.execute(text(statement))
#     db.session.commit()

# seed.py
from sqlalchemy import text
from extensions import db
from app import create_app

app = create_app()

with app.app_context():
    with open("seed_data.sql", "r") as sql:
        statement = sql.read()
        db.session.execute(text(statement))
        db.session.commit()
        print("✅ Database seeded successfully!")
