#ifndef __PIG_H__
#define __PIG_H__
#include "animal.h"

// Pig class - derived from Animal
class Pig : public Animal {
    int _fed;
public:
    Pig( string n) : Animal(n, "pig", "oink"), _fed(0) {};
    int feed() { return ++_fed; }
};

#endif
