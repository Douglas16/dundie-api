"""Database connection"""
from sqlmodel import Session, create_engine
from .config import settings
#Wrapper do FastAPI para DI
from fastapi import Depends


engine = create_engine(
    settings.db.uri,  # pyright: ignore
    echo=settings.db.echo,  # pyright: ignore
    connect_args=settings.db.connect_args,  # pyright: ignore
)


#Dependencia = funcao evitando acoplamento em vairos imports
#Usando genertor Yield 

def get_session():
    with Session(engine) as session:
        yield session



ActiveSession = Depends(get_session)