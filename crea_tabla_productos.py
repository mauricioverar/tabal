import sqlite3#importa libreria para trabajar con base de datos
conexion=sqlite3.connect('productos.db')#enlace a base de datos
consulta=conexion.cursor()#guarda resultado en consulta y habilita la conexion
tabla='CREATE TABLE tabla(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
    'nombre VARCHAR(30)NOT NULL,'\
    'calorias INTEGER(9)NOT NULL,'\
    'sodio INTEGER(9)NOT NULL);' #crea la tabla con los sig campos este será el numero para indicar los registros
#uso de condicionales con dos mensajes posibles
print (tabla)
if(consulta.execute(tabla)):
    print('la tabla fue creada')
else:
    print('la tabla no fue creada')
    
consulta.close()#des-habilita conexion
conexion.commit()#guarda los cambios con el metodo commit
conexion.close()#cierra la conexion
#esto se hace una vez solo para crear la tabla
