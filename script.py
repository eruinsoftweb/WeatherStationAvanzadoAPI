import requests
import time
import random

# URL de tu aplicación Flask
flask_url = "http://127.0.0.1:5000/postWeatherData"

while True:
    # Simulación de datos aleatorios
    temperature = round(random.uniform(-14, 46), 2)
    altitude = round(random.uniform(4, 71), 2)
    pressure = round(random.uniform(900, 1100), 2)

    # Fecha y hora actuales
    current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

    # Datos para enviar a la aplicación Flask como datos de formulario
    data = {
        'Temp': str(temperature),
        'Alt': str(altitude),
        'Pres': str(pressure),
        'Date': current_datetime.split()[0],
        'Time': current_datetime.split()[1]
    }

    # Enviar solicitud POST a la aplicación Flask con datos de formulario
    try:
        response = requests.post(flask_url, data=data)
        print("Data sent successfully.")
    except Exception as e:
        print(f"Error sending data: {e}")

    # Esperar un tiempo antes de enviar el siguiente conjunto de datos
    time.sleep(60)  # Puedes ajustar este valor según tus necesidades
