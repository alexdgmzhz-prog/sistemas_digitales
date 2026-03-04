int tempPin = 0; // 

LiquidCrystal_I2C lcd(0x27,16,2);  

void setup() {
  lcd.init();      
  lcd.backlight(); 
  
  lcd.setCursor(0, 0);
  lcd.print("Termometro");
  delay(1000);
  lcd.clear();
}

void loop() {
  int tempReading = analogRead(tempPin); 
  
  double tempK = log(10000.0 * ((1024.0 / tempReading - 1)));
  tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK )) * tempK );
  
  float tempC = tempK - 273.15;            
  float tempF = (tempC * 9.0)/ 5.0 + 32.0; 

  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(tempC);
  lcd.print(" C");

  lcd.setCursor(0, 1);
  lcd.print("Fahr: ");
  lcd.print(tempF);
  lcd.print(" F");

  delay(500); 
}