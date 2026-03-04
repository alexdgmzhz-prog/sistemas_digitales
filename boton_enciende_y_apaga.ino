int ledPin = 8;
int botonPin = 2;

int estadoLed = 0;
int estadoBoton;
int ultimoEstadoBoton = 1;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(botonPin, INPUT_PULLUP);
}

void loop() {
  estadoBoton = digitalRead(botonPin);

  if (estadoBoton == 0 && ultimoEstadoBoton == 1) {
    if (estadoLed == 0) {
      estadoLed = 1;
    } else {
      estadoLed = 0;
    }
    digitalWrite(ledPin, estadoLed);
    delay(200); // antirrebote
  }

  ultimoEstadoBoton = estadoBoton;
}