# SI-2024-CubeSat-SU
Repository for Summer Internship 2024- **"Introduction to CubeSat and Satellite Communication."**
# 📚THEORY
## Introductory Talks
<ul>
  <li>Brief discussion about the course by Dr Saroj Rout Sir.</li>
  <li>Introductory Talk by Dr Chinmoy Saha Sir.</li>
  <li>Introduction to ToSpace by Adnaan M Sir.</li>
</ul>

## Introduction to small satellites and formal CubeSats 🧊
<ul>
  <li>CubeSat is an actual spacecraft i.e launched into orbits,which is basically developed in educational institutes.</li>
  <li>It began as a collaborative effort in 1999 between Jordi Puig-Suari(a professor at Cal Poly) and Bob Twiggs(a professor at SSDL).</li>
  <li>The original intent of the project was to provide access to space for Space Uni Science Community.Many major schools and universities have also been able to start CCubeSats program of their own.</li>
  <li>Govt. agencies and commercial groups around the world have developed CubeSats.</li>
  <li>It can help reduce the costs of techical development and scientific investigations,and increase accrss to space,an exponential growth in the popularity of CubeSats.</li>
</ul>

### CLSI
<ul>
  <li>It stands for CubeSat Launch Initiative.</li>
  <li>It is a NASA initiative that provides oppurtunities for qualified CubeSats to fly as auxiliary payloads on future launches that have excess capacity.</li>
  <li>It enables NASA to develop public private partnerships that provide a low cost platform for NASA Science missions,including planetary explorations,Earth observations and fund Earth Science.</li>
  <li></li>
</ul>

# 💻LAB 
## Introduction to ESPN32 Board
<ul>
  <li>Introduction to ESPN32 Board by Prof Prasanta Swain Sir.
  <li>ESPN32 is technically a chip,that provide Internet and Bluetooth to IoT Devices.</li>
  <li>Requisites-</li>
  <ul>
    <li>Download Arduino IDE</li>
    <li>Open Arduino IDE->Files->Preferences->Add the necessary URLs from <ul><li>https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html </li>
    <li>https://randomnerdtutorials.com/</li>
  </ul>
    </ul>

## Basic Blinking off LED💡
<ul>
  
<li>Python Code</li>

  ```python
  #define LED 2
  void setup()
  {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() 
{
  digitalWrite(LED, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```
## Multiple Blinking of LED 💡
<ul>
  <li>Python Code</li>

  
  ```python
  #define LED1 2
  #define LED2 5

// the setup function runs once when you press reset or power the board

   void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED1, OUTPUT);

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED2, OUTPUT);
}


// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED1, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(150);                      // wait for a second
  digitalWrite(LED1, LOW);   // turn the LED off by making the voltage LOW
  delay(1000); 
   digitalWrite(LED2, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED2, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```
</ul>


## Serial Monitor Blinking of LED 💡

  
```python
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  if(Serial.available()){
    String command =Serial.readStringUntil('/n');
    if(command=="ON")
 {
    digitalWrite(LED_BUILTIN,HIGH);
    Serial.println("Turn LED ON");
 }
  else if(command=="OFF")
  {
    digitalWrite(LED_BUILTIN,LOW);
    Serial.println("Turn LED OFF");
  }
  // put your main code here, to run repeatedly:
  }
}
```

## Fading Off LED💡
```python
//#define ledcAttach

const int ledPin=5;

const int freq=5000;
const int resolution=8;


void setup() {
  // put your setup code here, to run once:

ledcAttach(ledPin,freq,resolution);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int dutyCycle=255; dutyCycle <=0;dutyCycle++)
  {
    ledcWrite(ledPin,dutyCycle);
    delay(15);
  }
  for(int dutyCycle=255;dutyCycle>=0;dutyCycle--)
  {
    ledcWrite(ledPin,dutyCycle);
    delay(15);
  }

}
```
## OLED 📱
```python
#include<SPI.h>
#include<Wire.h>
#include<Adafruit_GFX.h>
#include<Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET 4
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH,SCREEN_HEIGHT,&Wire,OLED_RESET);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS)){
  Serial.printf(F("SSD1306 allocation failed"));
  for(;;);

}

delay(2000);
display.clearDisplay();
display.setTextSize(3);
display.setTextColor(SSD1306_WHITE);
display.setCursor(0,0);
display.println(F("HELL0"));
display.display();
delay(2000);
}
void loop() {
  
  // put your main code here, to run repeatedly:

}
```

## OLED with scrolling 📱
```python
#include<Wire.h>
#include<Adafruit_GFX.h>
#include<Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET 4
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH,SCREEN_HEIGHT,&Wire,OLED_RESET);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC,SCREEN_ADDRESS)){
  Serial.printf(F("SSD1306 allocation failed"));
  for(;;);

}

delay(2000);

display.setCursor(0,0);
display.setTextSize(1);

display.println(F("Full"));
display.println(F("Screen"));
display.println(F("Recording"));
display.display();
delay(2000);
}
void loop() {
  display.startscrollright(0x00,0x07);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrollleft(0x00,0x07);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrolldiagright(0x00,0x07);
  delay(2000);
  display.startscrolldiagleft(0x00,0x07);
  delay(2000);
  display.stopscroll();
  display.clearDisplay();
  
  // put your main code here, to run repeatedly:

}

```

## Temperature & Humidity Sensor 🌬️
```python
#include "DHT.h"
#define DHT22PIN 4
DHT dht(DHT22PIN , DHT11);
void setup()
 {
  Serial.begin(9600);
  dht.begin();
  // put your setup code here, to run once:

}

void loop() 
{
  float humi=dht.readHumidity();
  float temp=dht.readTemperature();
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("ōC");
  Serial.print("Humidity: ");
  Serial.println(humi);
  delay(1000);
  // put your main code here, to run repeatedly:

}
```
## Temperature & Humidity Sensor on OLED 🌬️
```python
#include<Wire.h>
#include<Adafruit_GFX.h>
#include<Adafruit_SSD1306.h>
#include<Adafruit_Sensor.h>
#include <DHT.h>

#define SCREEN_WIDTH 128 //128OLED DISPLAY WIDTH
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH,SCREEN_HEIGHT,&Wire,-1);

#define DHT22PIN 4

#define DHTTYPE DHT22
DHT dht(DHT22PIN, DHTTYPE);

void setup(){
  Serial.begin(9600);
  dht.begin();

  if(!display.begin(SSD1306_SWITCHCAPVCC,0X3C)){
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  delay(2000);
  display.clearDisplay();
  display.setTextColor(WHITE);
}

void loop(){
  delay(5000);

  float humi = dht.readHumidity();
  float temp = dht.readTemperature();
  if(isnan(humi)||isnan(temp)){
    Serial.println("Failed to read from DHT sensor!");
  }

  display.clearDisplay();

display.setTextSize(1);
display.setTextColor(SSD1306_BLACK,SSD1306_WHITE);
display.setCursor(0,0);
display.print("temperature");
display.setTextSize(2);
display.setTextColor(SSD1306_BLACK,SSD1306_WHITE);
display.setCursor(0,10);
display.print(temp);
display.print(" ");
display.setTextSize(2);
display.print("C");


display.setTextSize(1);
display.setTextColor(SSD1306_BLACK,SSD1306_WHITE);
display.setCursor(0,35);
display.print("HUMIDITY");
display.setTextSize(2);
display.setTextColor(SSD1306_BLACK,SSD1306_WHITE);
display.setCursor(0,45);
display.print(humi);
display.print(" %");

display.display();
}
```
## LoRa Sender Protocol📡
```python
#include<SPI.h>
#include<LoRa.h>
#define DIO0 26
#define RST 14
#define NSS 18
#define MOSI 27
#define MISO 19
#define SCLK 5
int counter = 0;
void setup() {
  Serial.begin(115200);
  while(!Serial);
  Serial.println("LoRa Sender");
  // put your setup code here, to run once:
  SPI.begin(SCLK,MISO,MOSI,NSS);
  LoRa.setPins(NSS,RST,DIO0);
  while(!LoRa.begin(433E6)){
    Serial.println(".");
    delay(500);
  }
LoRa.setSyncWord(0xF3);
Serial.println("LoRa Initializing OK!");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Sending packet:");
  Serial.println(counter);
  LoRa.beginPacket();
  LoRa.print("Good afternoon");
  LoRa.print(counter);
  LoRa.endPacket();
  counter++;
  delay(1000);

}
```
## LoRa Receiver Protocol 📡
```python
#include<SPI.h>
#include<LoRa.h>
#define DIO0 26
#define RST 14
#define NSS 18
#define MOSI 27
#define MISO 19
#define CLK 5
//int counter = 0;
void setup() {
  Serial.begin(115200);
  while(!Serial);
  Serial.println("LoRa Receiver");
  // put your setup code here, to run once:
  SPI.begin(CLK,MISO,MOSI,NSS);
  LoRa.setPins(NSS,RST,DIO0);
  while(!LoRa.begin(433E6)){
    Serial.println(".");
    delay(500);
  }
LoRa.setSyncWord(0xF3);
Serial.println("LoRa Initializing OK!");
}

void loop() {
  int packetSize=LoRa.parsePacket();
  if(packetSize){
    Serial.print("Received packet'");
    while(LoRa.available()){
      String LoRaData=LoRa.readString();
      Serial.print(LoRaData);
    }
    float snr=LoRa.packetSnr();
    Serial.print("'with RSSI'");
    Serial.println(LoRa.packetRssi());
    Serial.print("with snr");
    Serial.println(snr);
  }
  // put your main code here, to run repeatedly:
 // Serial.print("Sending packet:");
  //Serial.println(counter);
  //LoRa.beginPacket();
  //LoRa.print("hello");
  //LoRa.print(counter);
  //LoRa.endPacket();
  //counter++;
  //delay(1000);

}

```






