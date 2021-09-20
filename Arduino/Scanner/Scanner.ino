#include <Stepper.h>
#include <SharpIR.h>
#include <math.h>
#define IRPin A0
#define model 1080

const int stepsPerRevolution = 2048;
Stepper myStepper = Stepper(stepsPerRevolution, 2, 4, 3, 5);
Stepper myStepper_z = Stepper(stepsPerRevolution, 6, 8, 7, 9);
int distance_cm;

SharpIR mySensor = SharpIR(IRPin, model);

int analog_mesafe =0;


void setup() {
  myStepper.setSpeed(5);
  myStepper_z.setSpeed(5);
  Serial.begin(9600);
  while (!Serial) {
  ;
}
 
}
float value;
float ortalama;
float sonuc;
float son;
int turn=52;
int sil = 0;
int stabil = 50;
int stepCount = 2048;
int step_s = 0;
int say=0;
void loop() {
 
  step_s = 2048/stepCount;
  
  if(sil == 0){

    delay(500);
    for(int c = 0; c<turn;c++){
      for(int a = 0;a<stepCount;a++){
        sonuc = 0;
        ortalama = 0;
        son = 0;
          for(int i=0;i<stabil;i++){
          distance_cm = analogRead(A0);
          value = mapFloat(distance_cm,665.0,350.0,7.0,16.5);
          ortalama = ortalama +value;
          delay(2);
          }
      sonuc = ortalama/30;
      son = 17.0 -sonuc;
      Serial.println(son);
      myStepper.step(step_s);
      }
    myStepper_z.step(-2048);
    delay(2000);
    }

  Serial.println("bitti");
  delay(100);
  sil = 1;
  }
 
 //myStepper.step(2048);
//myStepper_z.step(2048);
//say = say+1;
//Serial.println(say);
//tek();
//+ aşağıya iniyor
//- yukarı
}
void tek(){
  for(int i = 0;i <60;i++){
  
  sonuc = 0;
  ortalama = 0;
  son = 0;
  for(int i=0;i<40;i++){
          distance_cm = analogRead(A0);
          //value = mapFloat(distance_cm,665.0,350.0,7.0,16.5);
          ortalama = ortalama +distance_cm;
          delay(2);
          }
  sonuc = ortalama/40;
  //son = 17.0 -sonuc;
  Serial.print("value : ");
  Serial.println(sonuc);
  delay(500);
  }
}
float mapFloat(float fval, float val_in_min, float val_in_max, float val_out_min, float val_out_max)
{
  return (fval - val_in_min) * (val_out_max - val_out_min) / (val_in_max - val_in_min) + val_out_min;
}
