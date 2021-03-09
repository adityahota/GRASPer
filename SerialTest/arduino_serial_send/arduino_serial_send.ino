#define BUFF_SIZE 20

int current = 0;
char buff[BUFF_SIZE];

void setup() {
  Serial.begin(9600);
  memset(buff, 0, BUFF_SIZE);
}

void loop() {
  sprintf(buff, "Current: %d", current++);
  Serial.println(buff);
  memset(buff, 0, BUFF_SIZE);
  delay(1000);
}
