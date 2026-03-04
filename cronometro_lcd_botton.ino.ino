#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  

const int pinBoton = 2; 
int segundos = 0;

void setup() {
  lcd.init();           
  lcd.backlight();      
  
  pinMode(pinBoton, INPUT_PULLUP); 
  lcd.setCursor(0, 0);  
  lcd.print("Manten presionado");
}

void loop() {
 
  if (digitalRead(pinBoton) == LOW) {
    
    lcd.clear(); 
    
    lcd.setCursor(0, 0);
    lcd.print("Tiempo: ");
    lcd.print(segundos);
    
    lcd.setCursor(0, 1);
    lcd.print("... CORRIENDO ...");
    
    lcd.scrollDisplayLeft(); 
    
    segundos++; 
    delay(300); 
  } else {
   
    lcd.setCursor(0, 1);
    lcd.print("PAUSADO       "); 
  }
}