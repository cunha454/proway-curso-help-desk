from datetime import datetime

from sqlalchemy import DateTime, Boolean, String
from sqlalchemy.orm import Mapped, mapped_collumn

from api.app.core.tempo import agora
from core.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_collumn(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_collumn(String(60), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_collumn(String(255), nullable=True)
    ativo: Mapped[bool] = mapped_collumn(Boolean, default=True, nullable=False)
    criado_em: Mapped[datetime] = mapped_collumn(DateTime, default=agora, nullable=False)