void setup() {
  Serial.begin(115200); 
  pinMode(2, OUTPUT);   
}

void loop() {
  digitalWrite(2, HIGH);   
  Serial.println("LED is ON"); 
  delay(1000);             
  digitalWrite(2, LOW);   
  Serial.println("LED is OFF"); 
  delay(1000);            
}