int entradaBoton = 2;

int salidaLED = 13;

void setup() {

}


pinMode(salidaLED, OUTPUT);
pinMode(entradaBoton, INPUT);

void loop() {

int bitRecibido = digitalRead(entradaBoton);

if (bitRecibido == HIGH) {
digitalWrite(salidaLED, HIGH); 

} else {
digitalWrite(salidaLED, LOW); 

}

i

}