#include "SevSeg.h"
SevSeg sevseg;
const unsigned long eventInterval = 2000;
unsigned long previousTime = 0;
int i = 1;

void setup()
{
  //Set to 1 for single digit display
  byte numDigits = 1;

  //defines common pins while using multi-digit display. Left empty as we have a single digit display
  byte digitPins[] = {};

  //Defines arduino pin connections in order: A, B, C, D, E, F, G, DP
  byte segmentPins[] = {3, 2, 8, 7, 6, 4, 5, 9};
  bool resistorsOnSegments = true;

  //Initialize sevseg object. Uncomment second line if you use common cathode 7 segment
  // sevseg.begin(COMMON_ANODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);

  sevseg.setBrightness(90);
}

void loop()
{ 
   unsigned long currentTime = millis();

   if (currentTime - previousTime >= eventInterval && i < 10) {
     sevseg.setNumber(i);
     sevseg.refreshDisplay();
     i++;
   }
 
}
