import pulsar


client = pulsar.Client('pulsar://localhost:6650') #ip de
producer = client.create_producer('criminis')#Topico criminis


with open("nueva imagen.bmp", 'rb') as f:
            content = f.read()
            producer.send(content)

client.close()