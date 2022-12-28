#include <SoftwareSerial.h>
SoftwareSerial esp8266(2,3);// 2 ->RX   3->TX


void setup() {
  // put your setup code here, to run once:
  esp8266.begin(115200);
  Serial.begin(9600);
  
  esp8266.println("AT+CIPMUX=1");
  delay(2000);
  esp8266.println("AT+CIPSERVER=1,8888");

}

void loop() {
  // put your main code here, to run repeatedly:
  if (esp8266.available() > 0)
  {
    //String st = esp8266.readString() ; 
    //if(st == "abc")
    //  Serial.write("L");
      
    char c = esp8266.read();
    Serial.write(c);
  }
  if (Serial.available() > 0)
  {
    
    delay(1000);
    String command = "";
    while (Serial.available())
    {
      command += (char)Serial.read();
      //Serial.write(command[0]);
    }
    esp8266.println(command);
  }
}
