void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available() > 0) {  
  char stafur = Serial.read();
    if(stafur != '\n') {
    	if (stafur == 'h')
			Serial.println("hallo");
    	else if (stafur == 'b')
      		Serial.println("bless");
      	else
      		Serial.println("skil ekki!");
      	
    }
  }
}