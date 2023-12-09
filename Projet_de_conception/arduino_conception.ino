int motor_pin = 10;
int photores_pin = A0;
int light_value;
int v_motor;

void setup() {
  // put your setup code here, to run once:
  pinMode(motor_pin, OUTPUT);
  pinMode(photores_pin, INPUT);
  Serial.begin(9600);
  analogWrite(motor_pin, 255);
  delay(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  light_value = analogRead(photores_pin);
  v_motor = map(light_value, 0, 1023, 0, 33);
  if (v_motor > 23){
    v_motor = 23;
  } else if (v_motor < 5){
    v_motor = 5;
  }
  Serial.println(v_motor);
  analogWrite(motor_pin, v_motor);
}
