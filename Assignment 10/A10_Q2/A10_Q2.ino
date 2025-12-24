#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";

const char* serverURL = "http://10.250.240.60:5000/sensor";

float temperature = 28.5;
float humidity = 65.2;

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(serverURL);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    String postData = "temperature=" + String(temperature) +
                      "&humidity=" + String(humidity);

    int httpResponseCode = http.POST(postData);

    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Server response:");
      Serial.println(response);
    }

    http.end(); 
  }
  else {
    Serial.println("WiFi not connected");
  }
  
  delay(5000);
}
