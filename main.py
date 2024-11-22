# Generador de ID Único
from random import randint

print('*** Sistema de Generador de ID Único ***')

# Solicitar datos al usuario
name = input('¿Cuál es tu nombre?: ').strip()
lastname = input('¿Cuál es tu apellido?: ').strip()
birthyear = input('¿Cuál es tu año de nacimiento?: ').strip()

# Validar el año de nacimiento
if not birthyear.isdigit() or len(birthyear) != 4:
    print("\n❌ Error: Debes ingresar un año de nacimiento válido (4 dígitos).")
else:
    # Generar un número aleatorio de 4 dígitos
    random_number = randint(1000, 9999)

    # Crear el ID utilizando los datos ingresados
    unique_id = f"{name[:2].upper()}{lastname[:2].upper()}{birthyear[-2:]}{random_number}"
    
    # Mensaje final
    message = f'''
Hola {name}, habitante de Ciudad Gótica:

    Tu nuevo número de identificación (ID) generado por el sistema es:

    👉 {unique_id}

¡Felicidades y que tengas un excelente día!
'''
    print(message)
