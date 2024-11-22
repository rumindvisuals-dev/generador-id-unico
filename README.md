# Generador de ID Único

Este proyecto es un generador de identificación único que crea un ID exclusivo para cada usuario utilizando su nombre, apellido, año de nacimiento y un número aleatorio. El objetivo es demostrar cómo generar un ID único de manera sencilla y amigable para el usuario.

## Descripción

El sistema solicita al usuario su nombre, apellido y año de nacimiento. Luego, valida que el año de nacimiento sea correcto (4 dígitos) y genera un número aleatorio de 4 cifras. Después, combina estos datos en un formato único y genera un mensaje personalizado para el usuario, el cual muestra su ID único.

### El formato del ID generado es el siguiente:
```
[primeras dos letras del nombre][primeras dos letras del apellido][últimos dos dígitos del año de nacimiento][número aleatorio de 4 dígitos]
```

Ejemplo de un ID generado:
```
JUPE96AB3401
```

### Ejemplo de mensaje mostrado al usuario:
```
Hola Juan, habitante de Ciudad Gótica:

    Tu nuevo número de identificación (ID) generado por el sistema es:

    👉 JUPE96AB3401

¡Felicidades y que tengas un excelente día!
```

## Requisitos

Para ejecutar el programa, necesitas tener instalado Python 3.x en tu máquina.

## Instrucciones de uso

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/rumindvisuals-dev/generador-id-unico.git
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd generador-id-unico
   ```

3. Ejecuta el archivo `main.py`:
   ```bash
   python main.py
   ```

4. Ingresa los datos solicitados (nombre, apellido y año de nacimiento).

5. Recibe tu ID único y mensaje personalizado.

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en hacer un *fork* del repositorio y enviar tus *pull requests*. Asegúrate de seguir las buenas prácticas de codificación y agregar pruebas si es necesario.
