from db.database import engine
from db.base import Base

import models.customer
import models.account
import models.loan          # 👈 REQUIRED
import models.credit_card   # 👈 REQUIRED
import models.employee      # 👈 REQUIRED


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database and tables created")
