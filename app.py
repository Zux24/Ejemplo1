import requests

def consumir_endpoint(url):
    try:
        # Realiza la solicitud al endpoint
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Imprime la respuesta del servidor
            print("Respuesta del servidor:")
            print(response.text)
        else:
            # Imprime un mensaje de error si la solicitud no fue exitosa
            print(f"Error en la solicitud. Código de estado: {response.status_code}")

    except Exception as e:
        print(f"Error al realizar la solicitud: {e}")

# Reemplaza la URL con el endpoint que deseas consumir
url_del_endpoint = "https://ejemplo.com/api/datos"
consumir_endpoint(url_del_endpoint)
