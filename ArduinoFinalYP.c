#include "OneButton.h"

#include <Wire.h>

const int MPU=0x68; //I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ; //16-bit integers
int AcXcal,AcYcal,AcZcal,GyXcal,GyYcal,GyZcal,tcal, x, y, z; //calibration variables
double t,tx,tf,pitch,roll;

OneButton button(2, true);                         //attach a button on pin 2 to the library
OneButton button2(3, true);

const int ledPin = 9;
const int ledPin2 = 7; 
int btnVal1 = 0;
int btnVal2 = 0; 
 
void setup() {

  Wire.begin(); //initiate wire library and I2C
  Wire.beginTransmission(MPU); //begin transmission to I2C slave device
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // set to zero (wakes up the MPU-6050)  
  Wire.endTransmission(true); //ends transmission to I2C slave device

  pinMode(13, OUTPUT);                              // sets the digital pin as output
  pinMode(12, OUTPUT);                              // sets the digital pin as output
  pinMode(11, OUTPUT);                              // sets the digital pin as output
  pinMode(ledPin, OUTPUT);
 
  Serial.begin(9600);    
 // Serial.println("Hello Joel");
  button.attachDoubleClick(doubleclick);            // link the function to be called on a doubleclick event.
  button.attachClick(singleclick);                  // link the function to be called on a singleclick event.
  button.attachLongPressStop(longclick);            // link the function to be called on a longpress event.
  button.setClickTicks(250);

  button2.attachDoubleClick(doubleclick2);            // link the function to be called on a doubleclick event.
  button2.attachClick(singleclick2);                  // link the function to be called on a singleclick event.
  button2.attachLongPressStop(longclick2);     
  button2.setClickTicks(250);
  
}
 
void transmit(){
  Serial.print(btnVal1);
  Serial.print(",");
  Serial.print(btnVal2); 
  Serial.print(",");
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
}

void reset(){
  btnVal1 = 0;
  btnVal2 = 0;
}

void getAngle(int Ax,int Ay,int Az) 
{
    double x = Ax;
    double y = Ay;
    double z = Az;    
    pitch = atan(x/sqrt((y*y) + (z*z))); //pitch calculation
    roll = atan(y/sqrt((x*x) + (z*z))); //roll calculation</p><p>    //converting radians into degrees
    pitch = pitch * (180.0/3.14);
    roll = roll * (180.0/3.14) ;
}

void gyro(){
  Wire.beginTransmission(MPU); //begin transmission to I2C slave device
    Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H)
    Wire.endTransmission(false); //restarts transmission to I2C slave device
    Wire.requestFrom(MPU,14,true); //request 14 registers in total  </p><p>    //Acceleration data correction
    AcXcal = -950;
    AcYcal = -300;
    AcZcal = 0;  //Temperature correction
    tcal = -1600;  //Gyro correction
    GyXcal = 480;
    GyYcal = 170;
    GyZcal = 210;    //read accelerometer data
    AcX=Wire.read()<<8|Wire.read(); // 0x3B (ACCEL_XOUT_H) 0x3C (ACCEL_XOUT_L)  
    AcY=Wire.read()<<8|Wire.read(); // 0x3D (ACCEL_YOUT_H) 0x3E (ACCEL_YOUT_L) 
    AcZ=Wire.read()<<8|Wire.read(); // 0x3F (ACCEL_ZOUT_H) 0x40 (ACCEL_ZOUT_L)

    x = AcXcal + AcX; 
    y = AcYcal + AcY;
    z = AcZcal + AcZ;
  
  
    //read gyroscope data
    GyX=Wire.read()<<8|Wire.read(); // 0x43 (GYRO_XOUT_H) 0x44 (GYRO_XOUT_L)
    GyY=Wire.read()<<8|Wire.read(); // 0x45 (GYRO_YOUT_H) 0x46 (GYRO_YOUT_L)
    GyZ=Wire.read()<<8|Wire.read(); // 0x47 (GYRO_ZOUT_H) 0x48 (GYRO_ZOUT_L) </p><p>    //temperature calculation
    
    getAngle(AcX,AcY,AcZ);
  
    //printing values to serial port
 //   Serial.print("Angle: ");
 //   Serial.print("Pitch = "); Serial.print(pitch);
 //   Serial.print(" Roll = "); Serial.println(roll);
  
   // Serial.print("Accelerometer: ");
  //  Serial.print("X = "); Serial.print(x);
  //  Serial.print(" Y = "); Serial.print(y);
   // Serial.print(" Z = "); Serial.println(z); 
}

void loop() {
  gyro();
  button.tick();                                    // check the status of the button
  button2.tick();
  transmit();
//  Serial.println("Hello");
//  digitalWrite(ledPin, HIGH);
//  delay(1000);
//  digitalWrite(ledPin, LOW);
//  delay(1000); 
  delay(50);


 // reset();
} // loop
 
 
 
void doubleclick() {                                // what happens when button is double-clicked
    if(btnVal1 == 0 || btnVal1 == 3){
    btnVal1 = 4; 
  }
  else{
  btnVal1 = 3;
  }   
  digitalWrite(12,HIGH);    

}

void doubleclick2() {                                // what happens when button is double-clicked
   if(btnVal2 == 0 || btnVal2 == 3){
    btnVal2 = 4; 
  }
  else{
  btnVal2 = 3;
  }   
  digitalWrite(12,HIGH);                             // light the green LED


} 
void singleclick(){                                 // what happens when the button is clicked
  if(btnVal1 == 0 || btnVal1 == 2){
    btnVal1 = 1; 
  }
  else{
  btnVal1 = 2;
  }   
  digitalWrite(12,HIGH);                            // light the red LED

}

void singleclick2(){                                 // what happens when the button is clicked
    if(btnVal2 == 0 || btnVal2 == 2){
    btnVal2 = 1; 
  }
  else{
  btnVal2 = 2;
  }   
  digitalWrite(12,HIGH);                                // light the red LED

} 
void longclick(){                                   // what happens when buton is long-pressed
    if(btnVal1 == 0 || btnVal1 == 5){
    btnVal1 = 6; 
  }
  else{
  btnVal1 = 5;
  }   
  digitalWrite(12,HIGH);    

}
void longclick2(){
  if(btnVal2 == 0 || btnVal2 == 5){
    btnVal2 = 6; 
  }
  else{
  btnVal2 = 5;
  }   
  digitalWrite(12,HIGH);                                // light the red LED
}
