import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime
import os

# Configuração via Variáveis de Ambiente para segurança
DB_USER = os.getenv('DB_USER', 'seu_usuario')
DB_PASS = os.getenv('DB_PASS', 'sua_senha')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5433')
DB_NAME = os.getenv('DB_NAME', 'macro_db')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# ... (restante do código de ingestão que você já validou)
