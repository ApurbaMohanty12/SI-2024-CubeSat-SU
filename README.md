# SI-2024-CubeSat-SU
Repository for Summer Internship 2024 "Intro to CubeSat and Satellite Communication
# Lab Exercises
## Lab-1 Introduction to ESP32
-[Datasheet ESP32]
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
  delay(1000);                      // wait for a second
  digitalWrite(LED1, LOW);   // turn the LED off by making the voltage LOW
  delay(1000); 
   digitalWrite(LED2, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED2, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```
# Lab-2 Blinking LED
Des
'''C
## Lab-3 Dimming LED
Parameters from the LED Datasheet
|Parameters|Value|
|----------|-----|
|Max Forward Current| 30mA|
|Forward Voltage| 1.85 V|
|Dominant Wavelength| 640 nm|
|Colour|Red|
|Typical Capacitance|45pF|
|Operating Range|25 C|

'''
