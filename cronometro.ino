#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Dirección 0x27 (o la que obtuviste con el Scanner), 16 columnas, 2 filas
LiquidCrystal_I2C lcd(0x27, 16, 2);  

int segundos = 0; // Variable para contar el tiempo

void setup() {
  lcd.init();           
  lcd.backlight();      
  
  lcd.setCursor(0, 0);  
  lcd.print("Cronometro:");
}

void loop() {
  // Nos ubicamos en la segunda fila (0, 1)
  lcd.setCursor(0, 1);  
  
  // Imprimimos el valor de la variable
  lcd.print(segundos);
  lcd.print(" segundos");

  // Esperamos 1 segundo
  delay(1000);

  // Aumentamos el contador en 1
  segundos = segundos + 1;

  // Limpieza rápida si el número crece mucho (opcional)
  if(segundos > 99) {
    lcd.setCursor(0,1);
    lcd.print("       "); // Borra la línea para que no queden restos
  }
}