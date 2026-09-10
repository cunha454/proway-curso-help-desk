"""Pacote de models. Importar `app.models` registra as tabelas de Base.metadata o que o Alembic precisa para gerar as migrations"""
from api.app.models.usuario import Usuario
from api.app.core.enums import Papel
from api.app.models.categoria import Categoria
from api.app.core.database import Base


__all__ = ["Base", "Categoria", "Papel", "Usuario"]
