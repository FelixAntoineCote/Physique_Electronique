// Pin utilisé pour controler le transistor du moteur
int motor_pin = 10;
// Pin utilisé pour mesurer la résistance de la photoresistance
int photores_pin = A0;
// Variable utilisée pour enregistré la résistance de la photoresistance
int light_value;
// Variable utilisé pour enregistrer la vitesse du moteur
int v_motor;

// Partie du code qui se lance une fois lorsque l'arduino boot
void setup() {
  // On met la pin control moteur en sortie et la pin photoresistance en mode entrée
  pinMode(motor_pin, OUTPUT);
  pinMode(photores_pin, INPUT);
  // On initie la console sur la fréquence 9600
  Serial.begin(9600);
  // On lance le moteur à 100% pour lancer son inertie
  analogWrite(motor_pin, 255);
  delay(1000);
}

// Partie du code qui se répète à l'infini
void loop() {
  // Lis la résistance de la photorésistance
  light_value = analogRead(photores_pin);
  // Assigne la variable de la vitesse du moteur selon l'échelle qui nous intéresse en fonction de la
  // valeur de la résistance de la photorésistance
  v_motor = map(light_value, 0, 1023, 0, 33);
  // v_motor a 23 = 495 rpm et v_motor a 5 = 200 rpm. L'échelle se rend plus que ces valeurs pour augmenter
  // la variation (photorésistance se rend rarement aux extrêmes). Cependant, on ne veut pas que le moteur
  // dépasse ces vitesses, donc on les limites.
  if (v_motor > 23){
    v_motor = 23;
  } else if (v_motor < 5){
    v_motor = 5;
  }
  // On imprime la vitesse du moteur à la console
  Serial.println(v_motor);
  // On envoie la vitesse demandée au moteur
  analogWrite(motor_pin, v_motor);
}
