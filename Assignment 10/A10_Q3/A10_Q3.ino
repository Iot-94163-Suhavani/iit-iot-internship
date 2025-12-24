#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";

const char* mqtt_server = "test.mosquitto.org";

const char* temp_topic = "sensor/temperature";
const char* hum_topic  = "sensor/humidity";

WiFiClient espClient;
PubSubClient client(espClient);

float temperature = 27.8;
float humidity = 62.4;

void setup_wifi() {
  delay(10);
  Serial.print("Connecting to WiFi");

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");

    if (client.connect("ESP32_Publisher")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" retrying...");
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  char tempStr[10];
  char humStr[10];

  dtostrf(temperature, 4, 2, tempStr);
  dtostrf(humidity, 4, 2, humStr);

  client.publish(temp_topic, tempStr);
  client.publish(hum_topic, humStr);

  Serial.print("Published Temperature: ");
  Serial.println(tempStr);

  Serial.print("Published Humidity: ");
  Serial.println(humStr);

  delay(5000);  
}
