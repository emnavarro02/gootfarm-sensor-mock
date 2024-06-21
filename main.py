import argparse
import time
import json
import uuid
import random # import randrange, choice
from datetime import datetime
import paho.mqtt.client as paho

sensors = ['moisture','temperature']

def on_publish(client, userdata, result):         # create function for callback
    pass

def generate_value(sensor):
    if 'temperature' in sensor:
        return random.randrange(12, 42)
    elif 'moisture' in sensor:
        return random.randrange(0, 100)
    else:
        print('sensor not found.')

def loop(id,broker_address,broker_port,sleep):
    try:
        print(f'''
        ======================================================
        [DEBUG] Listener parameters
        ======================================================
        Listner ID:       {id}
        Update frequency: {sleep}
        Broker Address:   {broker_address}
        Broker Port:      {broker_port}
        Topic:            {topic}
        ======================================================
        ''')
        
        client = paho.Client(paho.CallbackAPIVersion.VERSION1)                      # create client object
        client.connect(broker_address, broker_port)
        client.on_publish = on_publish             # assign function to callback

        while True:
            sensor = random.choice(sensors)
            value  = generate_value(sensor)

            dict = {"timestamp": datetime.today().isoformat(), "name": id,"value": value,"type": sensor}
            message = json.dumps(dict)
            print(f"\n[INFO] New message: {message}")
            ret = client.publish(topic, message)               # publish
            time.sleep(sleep)
    except KeyboardInterrupt:
        print(f"[INFO] Listener {id} has stopped.")
        client.disconnect()
        raise SystemExit
    except Exception as e:
        print(f"[ERROR] It was not possible to connect to the broker server {broker_address}. Check if it's started and accepting messages.")
        print(e)

def send_once(id, broker_address, broker_port, type, value):
    client= paho.Client()                      # create client object
    client.connect(broker_address, broker_port)
    client.on_publish = on_publish             # assign function to callback

    dict = {"timestamp": datetime.today().isoformat(), "name": id,"value": value,"type": type}
    message = json.dumps(dict)
    print(f"\n[INFO] New message: {message}")
    ret = client.publish(topic, message)               # publish
    print("[INFO] {ret}.".format(ret=ret) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Insert required parameters...')
    parser.add_argument('-f','--frequency', default=10 ,type=int, help='How often a message is published in seconds. Default is 10.')
    parser.add_argument('-i','--id', default=None, help='The id of the subscriber. If not set a random ID will be created.')
    parser.add_argument('-t','--topic', default='/metrics', help='\nThe MQTT topic to publish messages. Default="/metrics"')
    parser.add_argument('-b','--broker_address', default='127.0.0.1', help='The MQTT broker IP address. Default = 127.0.0.1')
    parser.add_argument('-p','--broker_port', default=1883, type=int, help='The MQTT broker port. Default=1883')
    parser.add_argument('-v','--value', default=None, type=int, help='Value of measurment to be sent to the server.')
    parser.add_argument('-T','--type', default=None, help='Type of measurement to be sent to the server.')
    args = parser.parse_args()

    broker_address = args.broker_address
    broker_port    = args.broker_port
    topic          = args.topic
    frequency      = args.frequency
    type = args.type 
    value = args.value
    id             = args.id
    if not id:
        id = str(uuid.uuid4())

    if type and value:
        send_once(id=id, broker_address=broker_address, broker_port=broker_port,type=type, value=value)
    elif type or value:
        raise Exception("Both type and value are required.")
    else:
        loop(id=id, broker_address=broker_address, broker_port=broker_port, sleep=frequency)