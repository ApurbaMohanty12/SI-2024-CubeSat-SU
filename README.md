# SI-2024-CubeSat-SU
Repository for Summer Internship 2024- **"Introduction to CubeSat and Satellite Communication."**
# Lab Exercises
## _Lab-1 Introduction to ESP32_
<ul>
<li>Blinking Off LED</li>

```python
#define LED 2
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED, LOW);   // turn the LED off by making the voltage LOW
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
