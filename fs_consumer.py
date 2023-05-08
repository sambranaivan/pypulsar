import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('criminis', subscription_name='cat-FileSystemConsummer')
def process_message(msg):
    # Aquí puedes procesar el mensaje como desees, por ejemplo, guardar el archivo
    file_content = msg.data()

    # Guardar el archivo en disco (puedes cambiar el nombre y la ubicación según sea necesario)
    with open('nueva imagen2.bmp', 'wb') as f:
        f.write(file_content)

    print("Archivo recibido y guardado.")
# while True:
#     msg = consumer.receive()
#     print("Received message: '%s'" % msg.data())
#     consumer.acknowledge(msg)
while True:
    try:
        # Esperar y recibir un mensaje
        msg = consumer.receive()

        # Procesar el mensaje (en este caso, guardar el archivo)
        process_message(msg)

        # Confirmar el procesamiento exitoso del mensaje
        consumer.acknowledge(msg)
    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")

# Cerrar el consumidor y el cliente
consumer.close()
client.close()


