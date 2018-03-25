void setup() {
  Serial.setTimeout(5);
  Serial.begin(9600);
DDRB =   0b00111111;
  // put your setup code here, to run once:

}

String imp;
byte by;
int lil=0;
long i =0;
void loop() {
     //digitalWrite(13,LOW);

  

  if (Serial.available()>0){
    i=Serial.parseInt();
    //i=imp.toInt();
    if (i>0 && i<64){
   // Serial.println(i);
   PORTB=i;
   
   //delay(1000);
    }
    else{
      PORTB=0;
    }

  }

}  
  // put your main code here, to run repeatedly:


