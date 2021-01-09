// source file for disc
// include things
#include "disc.h"

void Disc::sellItem()
{
    int current_stock = this.get_quantity();
    current_stock = current_stock - 1;
    this.set_quantity(current_stock);
}

int Disc::getStock()
{
    
}