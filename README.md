# pypulsar

correr servidor de pulsar con 

<code>docker-compose up --build</code>


levantar consumidores con 
<code>py *_consumer.py</code>



publicar mensaje con
<code>py pub.py</code>


para levantar un GUI para pulsar


<code>docker run -it   -p 9527:9527 -p 7750:7750   -e SPRING_CONFIGURATION_FILE=/pulsar-manager/pulsar-manager/application.properties   apachepulsar/pulsar-manager:v0.3.0 --network pulsar</code>



