/* Entry point for application */
#include <iostream>
#include <string>
#include "animal.h"
#include "dog.h"
#include "cat.h"
#include "pig.h"
using namespace std; 

int main() {
    Dog d("Rover");
    Cat c("Fluffy");
    Pig p("Arnold");
    
    d.speak();
    c.speak();
    p.speak();
    cout << "the " << d.type() << " has been walked " << d.walk() << " times" << endl;
    cout << "the " << c.type() << " has been petted " << c.pet() << " times" << endl;
    cout << "the " << p.type() << " has been fed " << p.feed() << " times" << endl;
}
