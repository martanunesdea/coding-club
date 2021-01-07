// simple-inheritance.cpp by Bill Weinman <http://bw.org/>
// 2018-10-08
#ifndef __CLASS_H__
#define __CLASS_H__

#include <iostream>
#include <string>
using namespace std;

// Product class (base)
class Product {
    string _name;
    double _price; 
    int _quantity;
    // private constructor prevents construction of base class
    Product(){};
protected:
    // protected constructor for use by derived classes
    Product ( string & n, double p, int q )
    : _name(n), _price(p), _quantity(q) {}
public:
    void print() const;
    // getters
    const string & get_name() const { return _name; }
    const double get_price() const { return _price; }
    const int get_quantity() const { return _quantity; }
    // setters 
    
};

void Product::print() const {
    printf("Name is %s, price is %f, quantity is %d\n", _name.c_str(), _price, _quantity);
}

#endif