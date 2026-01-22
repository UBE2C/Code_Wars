#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

/* Return a freeable pointer */
char* zombie_shootout(unsigned zombies, unsigned distance, unsigned ammo) {
  unsigned z = zombies;
  float d = distance;
  unsigned a = ammo;

  int msg_1_len = snprintf(NULL, 0, "You shot all %u zombies.", zombies);
  int msg_2_len = snprintf(NULL, 0, "You shot %u zombies before being eaten: overwhelmed.", zombies);
  int msg_3_len = snprintf(NULL, 0, "You shot %u zombies before being eaten: ran out of ammo.", zombies);

  while(z > 0 && d > 0 && a > 0) {
    z -= 1;
    d -= 0.5;
    a -=1;

  }

  if(z == 0) {
    char* msg_1 = calloc(msg_1_len + 1, sizeof(char));
    snprintf(msg_1, msg_1_len + 1, "You shot all %u zombies.", zombies);
    return msg_1;
  }

  if(z != 0 && d == 0 && a != 0) {
    char* msg_2 = calloc(msg_2_len + 1, sizeof(char));
    snprintf(msg_2, msg_2_len + 1, "You shot %u zombies before being eaten: overwhelmed.", zombies - z);
    return msg_2;

  } else if (z != 0 && d != 0 && a == 0) {
    char* msg_3 = calloc(msg_3_len + 1, sizeof(char));
    snprintf(msg_3, msg_3_len + 1, "You shot %u zombies before being eaten: ran out of ammo.", zombies - z);
    return msg_3;

  } else if (z != 0 && d == 0 && a == 0) {
    char* msg_2 = calloc(msg_2_len + 1, sizeof(char));
    snprintf(msg_2, msg_2_len + 1, "You shot %u zombies before being eaten: overwhelmed.", zombies - z);
    return msg_2;

  }

  return NULL;

}

int main(void) {

    char* output = zombie_shootout(5, 20, 20);
    puts(output);
    free(output);

    return 0;

}
