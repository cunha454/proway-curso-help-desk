from sqlalchemy import select
from sqlalchemy.orm import Session

from app.repositories.base import RepositorioBase
from app.models.usuario import Usuario


class UsuarioRepository(RepositorioBase[Usuario]):
    def __init__(self, db: Session):
        super().__init__(db, Usuario)

    def consultar_por_email(self, email: str) -> Usuario | None:
        return self.db.scalar(select(Usuario).where(Usuario.email == email))

    def listar_todos(self) -> list[Usuario]:
        statement = select(Usuario)

        statement = statement.where(Usuario.ativo == True)

        return list(self.db.scalars(statement).all())