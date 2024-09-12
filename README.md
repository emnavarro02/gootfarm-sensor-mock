# Sensor Node Emulator

## Description

Contains an emulator of a sensor node that sends random data to a MQTT broker node.

This sensor node emulator will generate values for two types of sensors: moisture and temperature.
For mositure, the sensor node emulator will generate a random number between 0 - 100.
For temperurature, the sensor node emulator generates a random number between 12 - 42.

## How to use

To launch the sensor node emulator with default parameters run the following command:

```{powershell}
python main.py
```

If the sensor node emulator is launched with no parameters, the script will execute forever and randomly generate values with the default frequency (10 seconds).

Alternativelly it is possible to specify the type and value of a measurment by using the swtiches `--type` and `--value`. In this mode, the script will execute only once.

Moreover, it is possible to customize other parameters by using command switches. The following switches are accepted:

| Parameter       | Description                                                      | Default    | Type   |
|-----------------|------------------------------------------------------------------|------------|--------|
| -f, --frequency | How often a message is published in seconds. Default value is 10 | 10         | int    |
| -i, --id        | The id of the sensor node. If not set a random ID is created     | None       | String |
| -t, --topic     | The MQTT topic to publish messages                               | '/metrics' | String |
| -b, --topic     | The MQTT broker IP address                                       | '127.0.0.1'| String |
| -p, --topic     | The MQTT broker port                                             | 1883       | int    | 
| -T, --type      | Type of measurement to be sent to the server                     | None       | String | 
| -p, --value     | Value of measurment to be sent to the server                     | None       | int    | 

###  Examples:

* Show the help:
```{powershell}
python main.py -h
```

* Launches the sensor node emulator and connect to MQTT broker 192.168.0.100 on port 443:
```{powershell}
python main.py -b 192.168.0.100 -p 443
```

* Launches the sensor node emulator and connect to MQTT broker 192.168.0.100 on port 443:
```{powershell}
python main.py -b 192.168.0.100 -p 443
```

* Launches the sensor node emulator and sets messages frequency to every 60 seconds:
```{powershell}
python main.py -f 60
```

* Launches the sensor node emulator in the run-once mode, and send a measurement to the listerner:
```{powershell}
python main.py -T temperature -v 26
```

