#include <stdio.h>
#include <stdlib.h>

/* Variables */
double D = 18.69;
double A = 4.01814;
double B = 1203.835;
double C = -53.226;
double H = 33.9; // ?
double R = 0.0083174621; // ?

double convertP(double mmHg) {
  double bar = mmHg/750.061683;
  printf("Pressure converted to: %fK\n", bar); // DEBUG  
  return bar;
}

double cc_equation() {
  

}

double toK(double c) {
  double ret = c+273.15;
  printf("Temperature converted to: %fK\n", ret); // DEBUG
  return c+273.15;
}

int main()
{

  /* Get Input */
  char input[10] = "";
  printf("Enter temperature in degrees C: ");
  scanf("%s", input);
  printf("You entered: %s\n", input); // DEBUG
  double temperatureC = atof(input);

  /* Convert to K */
  double temperatureK = toK(temperatureC);

  /* Computer Vapor Pressure with CC equation */
  double cc = cc_equation(temperatureK);

  /*Compute Vapor Pressure with Antoine equation */
  
  

  
  return 0;
}
