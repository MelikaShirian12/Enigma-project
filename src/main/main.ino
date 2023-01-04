#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(7,6, 8, 9, 10, 11);
SoftwareSerial esp8266(2,3);// 2 ->RX   3->TX

void show_welcome(LiquidCrystal &lcd)
{
  lcd.setCursor(5,0);
  lcd.print("Hello!");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("*ENIGMA MACHINE*");
  lcd.setCursor(6,1);
  lcd.print("****");
  delay(2000);
  for(int i = 0 ; i < 16; i++)
    {
      lcd.scrollDisplayRight();
      delay(500);
    }
  delay(500);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(" I was made by :");
  delay(2000);
  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Melika And");
  lcd.setCursor(4,1);
  lcd.print("Kianoosh");
  delay(4000);
  lcd.setCursor(1,0);
  lcd.print("Enter Date and");
  lcd.setCursor(4,1);
  lcd.print("input...");
}

void setup() {
  lcd.begin(16, 2);
  lcd.clear();
  ////////////////////////////////////////////////
  esp8266.begin(115200);
  Serial.begin(9600);
  ////////////////////////////////////////////////
  esp8266.println("AT+CIPMUX=1");
  delay(2000);
  esp8266.println("AT+CIPSERVER=1,8888");
  //////////////////////////////////////////////// setting up esp8266
  pinMode(13, OUTPUT);
  digitalWrite(13,HIGH);
  ////////////////////////////////////////////////

  show_welcome(lcd);
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

    if(command[0] == 'R')
    {
      lcd.clear();

      for(int i = 0 ; i < 12;i++)
      {
        lcd.print(command[i]);
      }
      if(command.length() - 11 < 16)
        lcd.setCursor(0,1);
      else 
      lcd.setCursor(0,0);
      for(int i = 12 ; i < command.length();i++)
      {
        lcd.print(command[i]);
      }
    }
  }
}
