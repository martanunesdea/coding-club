#ifndef __DISC_H__
#define __DISC_H__
#include "product.h"
// Disc class - derived from Product

class Disc : public Product {
    double size;
    int playSpeed;
    string song;

public:
    Disc( string name, double price, int quantity, double size, int speed, string songName) : 
    Product(name, price, quantity), size(size), playSpeed(speed), song(songName) {};

    int getStock();
    void sellItem();
};


#endif
