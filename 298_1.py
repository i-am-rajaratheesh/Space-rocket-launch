# Add line no. 2, 4 & 6
from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)

broker = 'broker.emqx.io'
port = 1883
topic = "topicName/iot"

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def main():
    return render_template('main.html')

@app.route('/1', methods=['POST'])
def french(): 
    french_test()
    return render_template('main.html')

def french_test():
    client = connect_mqtt()
    client.loop_start()
    send_french_data(client) 

@app.route('/2', methods=['POST'])
def german():
    german_test()
    return render_template('main.html')

def german_test():
    client = connect_mqtt()
    client.loop_start()
    send_german_data(client) 

@app.route('/3', methods=['POST'])
def golden():
    golden_test()
    return render_template('main.html')

def golden_test():
    client = connect_mqtt()
    client.loop_start()
    send_golden_data(client) 

def send_french_data(client):
    msg = "French Bulldog"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send `{msg}` to topic `{topic}`")

def send_german_data(client):
    msg = "German Shepherd"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send `{msg}` to topic `{topic}`")

def send_golden_data(client):
    msg = "Golden Retriever"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send `{msg}` to topic `{topic}`")

if __name__ == "__main__":
    app.run(port=5001)





