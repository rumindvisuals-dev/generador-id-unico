# Generador de ID Único

print('*** Sistema de Generador de ID Único ***')

# Solicitar datos al usuario
name = input('¿Cuál es tu nombre?: ')
lastname = input('¿Cuál es tu apellido?: ')
birthyear = input('¿Cuál es tu año de nacimiento?: ')

# Crear el ID utilizando los datos ingresados
# Se utiliza una f-string para formatear correctamente el ID
unique_id = f"{name[:2].upper()}{lastname[:2].upper()}{birthyear[-2:]}"

# Mostrar el ID generado
print(f"\nTu ID único es: {unique_id}")
