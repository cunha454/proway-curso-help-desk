from typing import Annotated

from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from app.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]