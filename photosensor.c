const int pResistor = A0; // Photoresistor at Arduino analog pin A0
const int ledPin = 9;     // Led pin at Arduino pin 9

//Variables
int value;          // Store value from photoresistor (0-1023)

void setup() {
  //Initiate Serial communication.
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  // Set lepPin - 9 pin as an output
  pinMode(pResistor, INPUT);// Set pResistor - A0 pin as an input (optional)
}

void loop() {

  value = analogRead(pResistor);
  Serial.println(value);
  
  if (value > 500) {
    digitalWrite(ledPin, LOW);  //Turn led off
  }
  else {
    digitalWrite(ledPin, HIGH); //Turn led on
  }

  delay(1000); //Small delay
}