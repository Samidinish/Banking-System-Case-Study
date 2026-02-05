from db.database import engine
from db.base import Base

import models.customer
import models.account
import models.loan          
import models.credit_card   
import models.employee     


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database and tables created")
