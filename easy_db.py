import os
import sys
import time
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
||                                  V 2.0 (BETA)                                 ||
||                                                                               ||
||                           Creado por THE_IKERO90                              ||
||                                                                               ||
||-------------------------------------------------------------------------------||
|---------------------------------------------------------------------------------|                    
                    """

os.system("clear")
print(tit)
server = input("[+] Servidor a usar (localhost o un servidor en la nube) >> ")
user = input("[+] Usuario >> ")
passwd = input("[+] Contraseña >> ")
conexion = mysql.connector.connect(
    host=f"{server}",
    user=f"{user}",
    password=f"{passwd}"
)

# Barra de progreso
def progreso(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "█"*x, "."*(size-x), j, count))
        file.flush()
        file.write("\n")
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\n")
    file.flush()

for i in progreso(range(15), "Conectando: ", 40):
    time.sleep(0.1)
        
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
| [1] Crear Tabla.            |
|                             |
| [2] Borrar Tabla.           |
|                             |
| [3] Relaciones.             |
|                             |
| [4] Consultar Tablas.       |
-------------------------------
            """)
            opt2 = input(f"[{database}]~$ ")
                
        # Opcion de Crear Tablas  
            if opt2 == "1":
                os.system("clear")
                print(tit)
                table = input("Nombre de la tabla: ")
                pk = input ("[+] Clave primaria: ")
                pk_date = input("[+] Tipo de dato para la Clave primaria: ")
                mysql_cursor.execute(f"""
                    CREATE TABLE {table} (       
                    {pk} {pk_date}
                    ); 
                """)
                mysql_cursor.execute(f"ALTER TABLE {table} ADD PRIMARY KEY ({pk});")

                num = int(input("Numero de columnas (la pk no cuenta): "))
                for r in range(num):
                    name = input(f"[{r}] Nombre del registro: ")
                    date = input(f"[{r}] Tipo de dato del Registro: ")
                    allownull = input(f"[{r}] Habilitar campo vacío (allow o deny): ")
                    if allownull == "allow":
                        mysql_cursor.execute(f"ALTER TABLE {table} ADD COLUMN {name} {date};")
                    elif allownull == "deny":
                        mysql_cursor.execute(f"ALTER TABLE {table} ADD COLUMN {name} {date} NOT NULL;")
        
                mysql_cursor.execute(f"DESCRIBE {table};")
                for x in mysql_cursor:
                    print(x)
                        
            # Borrar Tablas       
            elif opt2 == "2":
                os.system("clear")
                print(tit)
                mysql_cursor.execute("SHOW TABLES;")
                for x in mysql_cursor:
                    print(x)
                table_del = input(f"[{database}] Seleccione la tabla a eliminar >> ")
                mysql_cursor.execute(f"DROP TABLE IF EXISTS {table_del};")
                mysql_cursor.execute("SHOW TABLES;")
                for x in mysql_cursor:
                    print(x)
                
                print("[-] Tabla eliminado!!!")
                a = input("[+] Presione ENTER para continuar >> ")
            
            # Crear Relaciones
            elif opt2 == "3":
                os.system("clear")
                activate4 = True
                while activate4:
                    activate = False
                    print(tit)
                    print("""
                          
Si desea cancelar escriba 'cancel'
-----------------------------------------------------------------------------------------------------------------
                                [+] ESCOJA EL TIPO DE RELACIÓN A APLICAR: 
-----------------------------------------------------------------------------------------------------------------
                                         
        1: REFLEXIVA                         2: BINARIA                                  3: TERNARIA

        _____                  _____            /\            _____                    _____         _____
       |_____| <---|          |_____|----------/__\----------|_____|                  |_____|       |_____|
          |        |                                                                        \      /
          |________|                                                                         \____/
                                                                                              \  /
                                                                                               \/
                                                                                                |
                                                                                                |
                                                                                              _____
                                                                                             |_____|

-----------------------------------------------------------------------------------------------------------------
                """)
                    relation = int(input(f" [{database}] >> "))
                    if relation == 1:
                        mysql_cursor.execute("SHOW TABLES;")
                        for x in mysql_cursor:
                            print(x)
                        table = input(f" [{database}] >> ")
                        mysql_cursor.execute(f"DESCRIBE TABLE {table};")
                        for x in mysql_cursor:
                            print(x)
                        primarykey = input(f" Clave Primaria de la Tabla >> ")
                        refkey = input("[+] Nombre de la clave para la relación Reflexiva >> ")
                        typedate = input("[+] Tipo de dato (INT, VARCHAR(num), CHAR(num), DECIMAR(num1,num2), etc. ): ")
                        nullopt = input("[+] Habilitar null o no ('allow' o 'deny') >> ")
                        if nullopt == "allow":
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table} ADD COLUMN {refkey} {typedate};
                            """)
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table} 
                                ADD FOREIGN KEY ({refkey}) REFERENCES {table}({primarykey})   
                            """)
                            print("[+] Creando Relacion: [ # . . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # # . ]")
                            time.sleep(0.2)
                            print("[+] Creando relacion: [ # # # # # ]")
                            time.sleep(0.2)
                        
                            print("[+] RELACION CREADA!!!")
                            
                        elif nullopt == "deny":
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table} ADD COLUMN {refkey} {typedate} NOT NULL;
                            """)
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table} 
                                ADD FOREIGN KEY ({refkey}) REFERENCES {table}({primarykey})           
                            """)
                            print("[+] Creando Relacion: [ # . . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # # . ]")
                            time.sleep(0.2)
                            print("[+] Creando relacion: [ # # # # # ]")
                            time.sleep(0.2)
                        
                            print("[+] RELACION CREADA!!!")
                        
                        print("[+] RELACION CREADA!!!")
                        a = input("[+] Presione ENTER para continuar . . . ")
                        sele4 = True
                        while sele4:
                            activate4 = False
                            print("""
------------------------------------
|    [a] Crear otra relación       |
|                                  |
|    [b] Volver al menu principal  |
------------------------------------                          
                            """)
                            opt = input("[+] >> ")
                            if opt == "a":
                                activate4 = True
                                sele4 = False
                            elif opt == "b":
                                sele4 = False
                                activate = True
                            else:
                                os.system("clear")
            
                    elif relation == 2:
                        mysql_cursor.execute("SHOW TABLES;")
                        for x in mysql_cursor:
                            print(x)
                        table1 = input("[+] Primera Tabla (Donde estará la Clave Ajena) >> ")
                        table2 = input("[+] Segunda Tabla >> ")
                        key2 = input("[+] Clave primaria de la segunda tabla >> ")
                        forkey = input("[+] Nombre de la Clave Ajena >> ")
                        typedate = input("[+] Tipo de dato (INT, CHAR(10), VARCHAR(10), DATE, etc.) >> ")
                        nullallow = input("[+] Permitir campo vacío (allow o deny) >> ")
                        if nullallow == "allow":
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table1} ADD COLUMN {forkey} {typedate};
                            """)
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table1} 
                                ADD  CONSTRAINT FK_{table1}_{table2} FOREIGN KEY ({forkey}) REFERENCES {table2}({key2});
                            """)
                            
                            print("[+] Creando Relacion: [ # . . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # # . ]")
                            time.sleep(0.2)
                            print("[+] Creando relacion: [ # # # # # ]")
                            time.sleep(0.2)
                            
                        elif nullallow == "deny":
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table1} ADD COLUMN {forkey} {typedate} NOT NULL;
                            """)
                            mysql_cursor.execute(f"""
                                ALTER TABLE {table1} 
                                ADD CONSTRAINT FK_{table1}_{table2} FOREIGN KEY ({forkey}) REFERENCES {table2}({key2});
                            """)
                            
                            print("[+] Creando Relacion: [ # . . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # . . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # . . ]")
                            time.sleep(0.2)
                            print("[+] Creando Relacion: [ # # # # . ]")
                            time.sleep(0.2)
                            print("[+] Creando relacion: [ # # # # # ]")
                            time.sleep(0.2)
                            
                        print("[+] Relacion creada!!!")
                        a = input("[+] Presione ENTER para continuar . . . ")
                    
                    elif relation == 3:
                        mysql_cursor.execute("SHOW TABLES;")
                        for x in mysql_cursor:
                            print(x)
                            
                        table1 = input("[1] Primera Tabla >> ")
                        pk1 = input("[1] Clave primaria de la primera tabla >> ")
                        date1 = input("[1] Tipo de dato de la clave primaria >> ")
                        
                        table2 = input("[2] Segunda Tabla >> ")
                        pk2 = input("[2] Clave primaria de la segunda tabla >> ")
                        date2 = input("[2] Tipo de dato de la clave primaria >> ")
                        
                        table3 = input("[3] Tercera Tabla >> ")
                        pk3 = input("[3] Clave primaria de la tercera tabla >> ")
                        date3 = input("[3] Tipo de dato de la clave primaria >> ")
                        
                        relationtable = input("[+] Nombre de la tabla de la relación >> ")
                        
                        mysql_cursor.execute(f"""
                            CREATE TABLE {relationtable} (
                                {pk1} {date1} NOT NULL,
                                {pk2} {date2} NOT NULL,
                                {pk3} {date3} NOT NULL
                            );               
                        """)
                        mysql_cursor.execute(f"ALTER TABLE {relationtable} ADD PRIMARY KEY ({pk1}, {pk2}, {pk3});")
                        mysql_cursor.execute(f"ALTER TABLE {relationtable} ADD CONSTRAINT FK_{relationtable}_{table1} FOREIGN KEY ({pk1}) REFERENCES {table1}({pk1});")
                        mysql_cursor.execute(f"ALTER TABLE {relationtable} ADD CONSTRAINT FK_{relationtable}_{table2} FOREIGN KEY ({pk2}) REFERENCES {table2}({pk2});")
                        mysql_cursor.execute(f"ALTER TABLE {relationtable} ADD CONSTRAINT FK_{relationtable}_{table3} FOREIGN KEY ({pk3}) REFERENCES {table3}({pk3});")
                        
                        print("[+] Creando Relacion: [ # . . . . ]")
                        time.sleep(0.2)
                        print("[+] Creando Relacion: [ # # . . . ]")
                        time.sleep(0.2)
                        print("[+] Creando Relacion: [ # # # . . ]")
                        time.sleep(0.2)
                        print("[+] Creando Relacion: [ # # # # . ]")
                        time.sleep(0.2)
                        print("[+] Creando relacion: [ # # # # # ]")
                        time.sleep(0.2)
                        print("[+] RELACION CREADA!!!")
                            
                                                                                                 

