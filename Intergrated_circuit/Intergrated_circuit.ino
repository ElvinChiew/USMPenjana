#include "DHT.h"
#define DHTPIN 10
#define DHTTYPE DHT11
#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define FlamePin A0
#define buzzer_led 7 
#define buzzer 4
int ledPin = 9;                
int inputPin = 11;               
int pirState = LOW;             
int val = 0; 
int sprinkler = 3;
DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial mySerial(9, 10);
byte tx = 1; 
LiquidCrystal_I2C lcd(0x27,20,4); 
String textForSMS;

void setup() {
  lcd.init();                      // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
  pinMode(FlamePin, INPUT_PULLUP);
  pinMode(buzzer_led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode (13, OUTPUT);
  pinMode(ledPin, OUTPUT);      
  pinMode(inputPin, INPUT);
  pinMode(sprinkler, OUTPUT);     
  pinMode(tx, OUTPUT);
  dht.begin();
  mySerial.begin(9600);
  Serial.begin(9600);
}

void loop(){
  int chk;
  float h=dht.readHumidity();
  float t=dht.readTemperature();

  lcd.setCursor(0,0);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print(" C");
  lcd.setCursor(0,1);
  lcd.print("Hum: ");
  lcd.print(h);
  lcd.print(" %");
  delay(1000);

  if(t>24){
    digitalWrite(13, HIGH);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("  Temperature to HOT ");
    delay(100);
    lcd.clear();
    lcd.print("Sending SMS...");
    delay(100);
    Serial.print("AT+CMGF=1\r");
    delay(100);
    Serial.print("AT+CMGS=\"+233266302607\"\r");
    Serial.print("Please Be Informed that the temperature in the Server Room is Abnormal!\r");
    delay(200);
    Serial.println((char)26); // End AT command with a ^Z, ASCII code 26
    delay(200);
    Serial.println();
    }
    else{
    digitalWrite(13, LOW);
    lcd.setCursor(0, 0);
    lcd.print("   Temperature is okay    ");

      }
   if(h>50){
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("  The humidity HIGH ");
    delay(100);
    lcd.clear();
    lcd.print("Sending SMS...");
    delay(100);
    Serial.print("AT+CMGF=1\r");
    delay(100);
    Serial.print("AT+CMGS=\"+233266302607\"\r");
    Serial.print("Please Be Informed that the HUMIDITY in the Server Room is Abnormal!\r");
    delay(200);
    Serial.println((char)26); // End AT command with a ^Z, ASCII code 26
    delay(200);
    Serial.println();      
    }
    else{
    digitalWrite(13, LOW);
    lcd.setCursor(0, 0);
    lcd.print("   Temperature is okay    ");
      } 
  int Flame = digitalRead(FlamePin);

   if(Flame==HIGH){
    digitalWrite(buzzer_led, HIGH);
    digitalWrite(buzzer, HIGH);
    digitalWrite(sprinkler, HIGH);
    delay(200);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("  There is fire ");
    lcd.setCursor(0, 1);
    lcd.print("Sprinkler ON");
    delay(100);
    lcd.clear();
    lcd.print("Sending SMS...");
    delay(100);
    Serial.print("AT+CMGF=1\r");
    delay(100);
    Serial.print("AT+CMGS=\"+233266302607\"\r");
    Serial.print("Fire in Server Room\r");
    delay(200);
    Serial.println((char)26); // End AT command with a ^Z, ASCII code 26
    delay(200);
    Serial.println(); 
    
    } 
    else{
    digitalWrite(buzzer_led,LOW);
    digitalWrite(buzzer,LOW);
    digitalWrite(sprinkler, LOW);    
    lcd.setCursor(0, 0);
    lcd.print("   No fire   ");
      }
  val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);  // turn LED ON
    if (pirState == LOW) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("There is Someone in server room");
    delay(100);
    lcd.clear();
    lcd.print("Sending SMS...");
    delay(100);
    Serial.print("AT+CMGF=1\r");
    delay(100);
    Serial.print("AT+CMGS=\"+233266302607\"\r");
    Serial.print("People in Server Room\r");
    delay(200);
    Serial.println((char)26); // End AT command with a ^Z, ASCII code 26
    delay(200);
    pirState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); // turn LED OFF
    if (pirState == HIGH){
    lcd.setCursor(0, 0);
    lcd.print("No one in the server room");
      pirState = LOW;
    }
  }
  delay(1000);
    
     

}
