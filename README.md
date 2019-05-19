## Espy
Communicate with an esp8266 in the context of home automation.

## About
This skill has been created for the makers and hackers who want to build their own home automation system based on esp8266. the purpose of this skill is to be able to use mycroft to send commands to all esp8266s on the local network. the communication protocol can be selected (websocket, mqtt, http get).

## Examples 
* "_Hey Mycroft, can you switch on the mood lamp ?_"

* "_Hey Mycroft, can you turn off the TV ?_"

## Configuration


```
    "Esp8266Skill": {
        "units": "esp8266.local",   // Can be an IP Address
        "protocol": "http_get",     // Options : ws, mqtt, http_get
        "ws-port": 81,
        "mqtt-host" : "test.mosquitto.org",
        "mqtt-port" : 1883,
        "mqtt-auth" : "no",         // yes or no
        "mqtt-user" : "youruser",
        "mqtt-pass" : "yourpass"
    },
```

## Requirements

This skill requires the installation of paho-mqtt : `pip install paho-mqtt`.

The arduino code for the ESP8266 can be found [here](https://github.com/Dark5ide/ESP8266_Controller). 

## TODO

* Improve the keyword part.
* Auto-recognition of a new ESP8266 on the local network.
* Clean the code
* MQTT protocol implementation. **(done)**
* Put the Arduino code of the ESP8266 on github **(done)** : https://github.com/Dark5ide/ESP8266_Controler3
* Use JSON format for the information transmitted. **(done)**

## Credits
Dark5ide

## Category

## Tags


