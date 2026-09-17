from enum import Enum


class Papel(str, Enum):
    ADMIN = "ADMIN"
    ATENDENTE = "ATENDENTE"
    SOLICITANTE = "SOLICITANTE"


class StatusChamado(str, Enum):
    ABERTO = "ABERTO"
    EM_ANALISE = "EM_ANALISE"
    RESOLVIDO = "RESOLVIDO"
    CANCELADO = "CANCELADO"


class PrioridadeDeChamado(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"