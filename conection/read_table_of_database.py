from conection.conexion import *
import pandas as pd
def read_table(conexion,table_name):
    query=f"SELECT * FROM "
    try:
        df_trades = pd.read_sql_query(query, conexion)
        return df_trades
    except (Exception, psycopg2.Error) as error:
        print(f"Error al leer la tabla trades:", error)

# Ejemplo de uso
df_trade = read_table(conexion, 'trades')
