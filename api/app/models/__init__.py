"""Pacote de models. Importar `app.models` registra as tabelas de Base.metadata o que o Alembic precisa para gerar as migrations"""
from app.models.usuario import Usuario
from app.core.enums import Papel
from app.models.categoria import Categoria
from app.models.ticket import Ticket
from app.core.database import Base


__all__ = ["Base", "Categoria", "Papel", "Usuario", "Ticket"]
