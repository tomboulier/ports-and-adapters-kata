# Hexagonal Architecture / Ports and Adapter Kata

This is a kata on ports and adapters architecture. The task is to retrieve a list of weather observations from the following API:

https://open-meteo.com/

and output the result into a CSV file of the following format:

id,name,date,time,temperature,pressure,wind_direction (optional)

The API documentation can be found here: https://open-meteo.com/en/docs

The goal is not to get this done as quickly as possible, but to follow the rules of
[ports and adapters architecture](http://alistair.cockburn.us/Hexagonal+architecture):
  * The application itself does not depend directly on any external systems, but only on ports
  * The protocol for a port is given by the purpose of the conversation it describes
  * For each external system there is an ‘’adapter’’ that converts the API definition to the format needed by that system and vice versa

Now have some fun!



