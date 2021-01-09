/* Entry point for application */
#include <iostream>
#include <string>
#include "product.h"
#include "disc.h"

using namespace std; 

int main() {
    
    Disc d("Rover", 20, 100, 12);
   
    d.print();
}
