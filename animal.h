// simple-inheritance.cpp by Bill Weinman <http://bw.org/>
// 2018-10-08
#ifndef __CLASS_H__
#define __CLASS_H__

#include <iostream>
#include <string>
using namespace std;

// Animal class (base)
class Animal {
    string _name;
    string _type;
    string _sound;
    // private constructor prevents construction of base class
    Animal(){}
protected:
    // protected constructor for use by derived classes
    Animal ( const string & n, const string & t, const string & s )
    : _name(n), _type(t), _sound(s) {}
public:
    void speak() const;
    const string & name() const { return _name; }
    const string & type() const { return _type; }
    const string & sound() const { return _sound; }
};

void Animal::speak() const {
    printf("%s the %s says %s\n", _name.c_str(), _type.c_str(), _sound.c_str());
}

#endif