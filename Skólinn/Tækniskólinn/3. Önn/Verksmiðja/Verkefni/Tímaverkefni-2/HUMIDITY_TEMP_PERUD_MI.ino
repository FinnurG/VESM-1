#include <dht.h>  // Include library
#define outPin 8  // Defines pin number to which the sensor is connected

dht DHT;      // Creates a DHT object

void setup() {
  Serial.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  digitalWrite(6, LOW); 
  digitalWrite(7, LOW);
  
  int readData = DHT.read11(outPin);

  float t = DHT.temperature;  // Read temperature
  float h = DHT.humidity;   // Read humidity
  
  Serial.print("Temperature = ");
  Serial.print(t);
  Serial.print("°C | ");
  Serial.print("Humidity = ");
  Serial.print(h);
  Serial.println("% ");
  Serial.println("");

  if (t > 24) {
  digitalWrite(7, HIGH);
}
  if (h > 37) { // <
  digitalWrite(6, HIGH);
}
 
  delay(2000); // wait two seconds
  
}
