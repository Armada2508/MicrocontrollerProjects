#include <Joystick.h>

const int pin_count = 12;

Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_JOYSTICK, pin_count, 0, false, false, false, false, false, false, false, false, false, false, false);

const int input_pin_map[pin_count] = {1, 0, 3, 2, 4, 5, 6, 7, 10, 11, 12, 13};
int button_state[pin_count] = {1};

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  for (int i = 0; i < pin_count; i++) {
    pinMode(input_pin_map[i], INPUT_PULLUP);
  }
  Joystick.begin();
}

void loop() {
  for (int i = 0; i < pin_count; i++) {
    int currentButtonState = !digitalRead(input_pin_map[i]);
    if (currentButtonState != button_state[i]) {
      Joystick.setButton(i, currentButtonState);
      button_state[i] = currentButtonState;
    }
  }
}
