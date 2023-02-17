import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("lijianso/pong")
    client.message_callback_add("lijianso/pong", on_message)
    
    

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
    message = int(msg.payload.decode())
    message += 1
    client.publish("lijianso/ping", message)
    print(f"{message} published")
    time.sleep(1)

if __name__ == '__main__':
   
    #create a client object
    client = mqtt.Client()
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    time.sleep(1)
    
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="192.168.43.198", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    msg = 0
    client.publish("lijianso/ping", msg)
    print(f"{msg} published")
    
    client.loop_forever()

