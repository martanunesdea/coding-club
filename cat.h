#ifndef __CAT_H__
#define __CAT_H__
#include "animal.h"
// Cat class - derived from Animal
class Cat : public Animal {
    int _petted;
public:
    Cat( string n ) : Animal(n, "cat", "meow"), _petted(0) {};
    int pet() { return ++_petted; }
};

#endif
