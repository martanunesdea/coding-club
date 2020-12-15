#ifndef __CHILD_CLASS_H__
#define __CHILD_CLASS_H__

#include <iostream>
#include <string>
#include "animal.h"
using namespace std;

// Dog class - derived from Animal
class Dog : public Animal {
    int _walked;
public:
    Dog( string n ) : Animal(n, "dog", "woof"), _walked(0) {};
    int walk() { return ++_walked; }
};

#endif