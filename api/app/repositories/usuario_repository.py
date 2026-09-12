from sqlalchemy.orm import Session

from app.repositories.base import RepositorioBase
from app.models.usuario import Usuario


class UsuarioRepository(RepositorioBase[Usuario]):
    def __init__(self, db: Session):
        super().__init__(db, Session)