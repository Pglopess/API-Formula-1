import pandas as pd
import sqlite3

DB_PATH = "f1.db"

conn = sqlite3.connect(DB_PATH)

# Pilotos
drivers = pd.read_csv("data/drivers.csv")
drivers = drivers[["driverId", "forename", "surname", "nationality", "dob"]].copy()
drivers.columns = ["id", "nome", "sobrenome", "nacionalidade", "nascimento"]
drivers.to_sql("pilotos", conn, if_exists="replace", index=False)

# Corridas
races = pd.read_csv("data/races.csv")
races = races[["raceId", "year", "name", "round"]].copy()
races.columns = ["id", "temporada", "nome", "rodada"]
races.to_sql("corridas", conn, if_exists="replace", index=False)

# Resultados
results = pd.read_csv("data/results.csv")
results = results[["resultId", "raceId", "driverId", "points", "position"]].copy()
results.columns = ["id", "corrida_id", "piloto_id", "pontos", "posicao"]
results.to_sql("resultados", conn, if_exists="replace", index=False)

conn.close()
print("Banco populado com sucesso!")