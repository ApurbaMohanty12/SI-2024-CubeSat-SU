# SI-2024-CubeSat-SU
Repository for Summer Internship 2024- **"Introduction to CubeSat and Satellite Communication."**
# 📚THEORY
## Introductory Talks
<ul>
  <li>Brief discussion about the course by Dr Saroj Rout Sir.</li>
  <li>Introductory Talk by Dr Chinmoy Saha Sir.</li>
  <li>Introduction to ToSpace by Adnaan M Sir.</li>
</ul>

# 💻LAB 
## Introduction to ESPN32 Board
<ul>
  <li>Introduction to ESPN32 Board by Prof Prasanta Swain Sir.
  <li>ESPN32 is technically a chip,that provide Internet and Bluetooth to IoT Devices.</li>
  <li>Figure of ESPN32 Board ![download](https://github.com/ApurbaMohanty12/SI-2024-CubeSat-SU/assets/173773194/db748177-8706-4053-a0ef-919d5096f7f3)</li>
  <li>Requisites-</li>
  <ul>
    <li>Download Arduino IDE</li>
    <li>Open Arduino IDE->Files->Preferences->Add the necessary URLs from <ul><li>https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html </li>
    <li>https://randomnerdtutorials.com/</li>
  </ul>
</ul>

## Basic Bliinking off LED
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
<li>Circuit Diagram</li>
<li>Figure</li>
</ul>
