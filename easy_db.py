import os
import mysql.connector

tit = """
|---------------------------------------------------------------------------------|
||-------------------------------------------------------------------------------||
||                                                                               ||
||                                                                               ||
||            ███████╗░█████╗░░██████╗██╗░░░██╗  ██████╗░██████╗░                ||
||            ██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝  ██╔══██╗██╔══██╗                ||
||            █████╗░░███████║╚█████╗░░╚████╔╝░  ██║░░██║██████╦╝                ||
||            ██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░  ██║░░██║██╔══██╗                ||
||            ███████╗██║░░██║██████╔╝░░░██║░░░  ██████╔╝██████╦╝                ||
||            ╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═════╝░                ||
||                                                                               ||
||                                  V 1.0 (BETA)                                 ||    
||                                                                               ||
||                                                                               ||
||-------------------------------------------------------------------------------||
|---------------------------------------------------------------------------------|                    
                    """

os.system("clear")
print(tit)
server = input(" Servidor a user (localhost o un servidor en la nube) >> ")
us = input("[+] Usuario >> ")
passwd = input("[+] Contraseña >> ")
conexion = mysql.connector.connect(
    host=f"{server}",
    user=f"{us}",
    password=f"{passwd}"
)
mysql_cursor = conexion.cursor()
main = True
while main:
    os.system("clear")
    print(tit)   
    print("""
------------------------------------------------------------------------------------------
| Bienvenido a Easy DB. Este Script proporciona a la gente una forma sencilla de manejar |
| una base de datos.                                                                     |
------------------------------------------------------------------------------------------
""")
    print("""
--------------------------------------
| [a] Crear una Base de Datos.       |
|                                    |
| [b] Acceder a una Base de datos.   | 
--------------------------------------
    """)
    opt = input(" >> ")
    if opt == "a":
        new_db = input(" Nombre de la nueva Base de Datos >> ")
        os.system("clear")
        mysql_cursor.execute(f"CREATE DATABASE {new_db};")
        print(f"[+] Base de datos {new_db} creada!!!")
        a = input(" Presione ENTER para continuar >> ")
        os.system("clear")
    
    elif opt == "b":
        mysql_cursor.execute("SHOW DATABASES;")
        for x in mysql_cursor:
            print(x)
        database = input("[+] Seleccione la base de datos a usar >> ")
        mysql_cursor.execute(f"USE {database};")
        activate = True
        while activate:
            main = False
            os.system("clear")
            print(tit)
            print("""   
-------------------------------
| [1] Ver Tablas.             |
|                             |
| [2] Crear Tabla.            |
|                             |
| [3] Borrar Tabla.           |
|                             |
| [4] Insertar/Eliminar datos.|
-------------------------------
            """)
            opt2 = input(f"[{database}]~$ ")
            if opt2 == "1":
                mysql_cursor.execute("SHOW TABLES;")
                for x in mysql_cursor:
                    print(x)
                a = input("[+] Presione ENTER para continuar >> ")
                    
            elif opt2 == "2":
                new_table = input("[+] Escriba el nombre de la Nueva Tabla >> ")
                sele1 = True
                while sele1:
                    os.system("clear")
                    print(tit)
                    activate = False
                    print("""
--------------------------------------------------------------------
| 1  columna | 2 columnas  |  3 columnas | 4 columnas | 5 columnas |
--------------------------------------------------------------------

Para retroceder escriba 'return'.
                    
                    """)
                    num = input("[+] >> ")
                    if num == "1":
                        column1 = input("[1] Primera columna >> ")
                        mysql_cursor.execute(f"""
                        CREATE TABLE {new_table} (
                            {column1} VARCHAR(1000)
                        );
                        """)
                        mysql_cursor.execute(f"DESCRIBE {new_table};")
                        for x in mysql_cursor:
                            print(x)
                        print("[+] Tabla creadad!!!")
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif num == "2":
                        column1 = input("[1] Primera columna >> ")
                        column2 = input("[2] Segunda columna >> ")
                        mysql_cursor.execute(f"""
                        CREATE TABLE {new_table} (
                            {column1} VARCHAR(1000),
                            {column2} VARCHAR(1000)
                        );
                        """)
                        mysql_cursor.execute(f"DESCRIBE {new_table};")
                        for x in mysql_cursor:
                            print(x)
                        print("Tabla Creada!!!")
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif num == "3":
                        column1 = input("[1] Primera columna >> ")
                        column2 = input("[2] Segunda columna >> ")
                        column3 = input("[3] Tercera columna >> ")
                        mysql_cursor.execute(f"""
                        CREATE TABLE {new_table} (
                            {column1} VARCHAR(1000),
                            {column2} VARCHAR(1000),
                            {column3} VARCHAR(1000)
                        );
                        """)
                        mysql_cursor.execute(f"DESCRIBE {new_table};")
                        for x in mysql_cursor:
                            print(x)
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif num == "4":
                        column1 = input("[1] Primera columna >> ")
                        column2 = input("[2] Segunda columna >> ")        
                        column3 = input("[3] Tercera columna >> ")
                        column4 = input("[4] Cuarta columna >> ")
                        mysql_cursor.execute(f"""
                        CREATE TABLE {new_table} (
                            {column1} VARCHAR(1000),
                            {column2} VARCHAR(1000),
                            {column3} VARCHAR(1000),
                            {column4} VARCHAR(1000)
                        );
                        """)
                        mysql_cursor.execute(f"DESCRIBE {new_table};")
                        for x in mysql_cursor:
                            print(x)
                        print("Tabla creada !!!")
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif num == "5":
                        column1 = input("[1] Primera columna >> ")
                        column2 = input("[2] Segunda columna >> ")
                        column3 = input("[3] Tercera columna >> ")
                        column4 = input("[4] Cuarta columna >> ")
                        column5 = input("[5] Quinta columna >> ")
                        mysql_cursor.execute(f"""
                        CREATE TABLE {new_table} (
                            {column1} VARCHAR(1000),
                            {column2} VARCHAR(1000),
                            {column3} VARCHAR(1000),
                            {column4} VARCHAR(1000),
                            {column5} VARCHAR(1000)
                        );
                        """)
                        mysql_cursor.execute(f"DESCRIBE {new_table};")
                        for x in mysql_cursor:
                            print(x)
                        print("Tabla creada!!!")
                        a = input("[+] Presione ENTER para continuar >> ")
                    
                    elif num == "return":
                        sele1 = False
                        activate = True
                    
                    else:
                        os.system("clear")
                    
            elif opt2 == "3":
                table_del = input("[+] Seleccione la tabla a eliminar >> ")
                mysql_cursor.execute(f"DROP TABLE {table_del};")
                mysql_cursor.execute("SHOW TABLES;")
                for x in mysql_cursor:
                    print(x)
                print("Tabla eliminado!!!")
                a = input("[+] Presione ENTER para continuar >> ")
                    
            elif opt2 == "4":
                os.system("clear")
                print(tit)
                table_sel = input("[+] Seleccione la tabla >> ")
                activate3 = True
                while activate3:
                    activate = False
                    os.system("clear")
                    print(tit)
                    print("""
------------------------------------------------------------------------
|               SELECCIONE UNA DE ESTAS OPCIONES                       |
------------------------------------------------------------------------
|         [ + ]  AÑADIR          |          [ - ]  ELIMINAR            |
------------------------------------------------------------------------

Si desea volver escriba 'return'.
                    """)
                    opt4 = input(f"[{database}]~$ ")
                    if opt4 == "+":
                        print(" ")
                        print("-------------------------------------------->")
                        print(" ")
                        columns = input("[+] Siguiendo la flecha valla escribiendo de la siguiente forma todos los nombres de cada columna (columna1, columna2, columna3) >> ")
                        dates_add = input("[+] Siguiendo el orden de la flecha vallan introducioendo de la siguiente manera los datos a introducir ('dato1', 'dato2', 'dato3') >> ")
                        mysql_cursor.execute(f"INSERT INTO {table_sel} ({columns}) VALUES ({dates_add});")
                        mysql_cursor.execute(f"SELECT * FROM {table_sel};")
                        for x in mysql_cursor:
                            print(x)
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif opt4 == "-":
                        mysql_cursor.execute(f"SELECT * FROM {table_sel};")
                        for x in mysql_cursor:
                            print(x)
                        column = input("[-] Seleccione una columna >> ")
                        date_del = input("[-] Escriba el dato a eliminar >> ")
                        mysql_cursor.execute(f"DELETE FROM {table_sel} WHERE {column}={column};")
                        mysql_cursor.execute(f"SELECT * FROM {table_sel};")
                        for x in mysql_cursor:
                            print(x)
                        a = input("[+] Presione ENTER para continuar >> ")
                            
                    elif opt4 == "return":
                        activate3 = False
                        activate = True
            
            else:
                os.sistem("clear")