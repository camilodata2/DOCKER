import psycopg2

def conect_data_base(host,port,nombre_db,contraseña,usuario):
    try:
        conexion=psycopg2.connect(
            host=host,
            port=port,
            nombre_db=nombre_db,
            contraseña=contraseña,
            usuario=usuario
        )
        print("la conexion fue exitosa a la base de datos")
        return conexion
    except (Exception,psycopg2.Error) as error:
        print('hubo una falla en la conecion a la base de datos',error)

# Ejemplo de conexion
conexion = conect_data_base('localhost', '5432', 'postgres1', 'camilo43', 'postgres')