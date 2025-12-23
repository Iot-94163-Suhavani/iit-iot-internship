void setup() {
 Serial.begin(115200);
 pinMode(34,INPUT);
 Serial.println("ADC setup is done");
}

void loop() {
 int value= analogRead(34);
 Serial.printf("Light intensity: %d\n",value);
 delay(2000);
}
