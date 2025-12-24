#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";

const char* mqtt_server = "test.mosquitto.org";

const char* led_topic = "home/led";

WiFiClient espClient;
PubSubClient client(espClient);

const int ledPin = 2;   

void setup_wifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived: ");

  String msg = "";
  for (int i = 0; i < length; i++) {
    msg += (char)message[i];
  }

  Serial.println(msg);

  if (msg == "ON") {
    digitalWrite(ledPin, HIGH);
    Serial.println("LED ON");
  }
  else if (msg == "OFF") {
    digitalWrite(ledPin, LOW);
    Serial.println("LED OFF");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_LED_Subscriber")) {
      Serial.println("connected");
      client.subscribe(led_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

