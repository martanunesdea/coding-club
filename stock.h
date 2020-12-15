/* stock.h
 * Description: Class for Stock object
 * Date: 15/12/2020
 * Author: Marta Nunes de Abreu
 * Compiler: Clang++ v11
 */

#include <iostream>
#include <string>
using namespace std;

class Stock {
    private: 
    string name_;
    int num_available_;
    int num_sold_;
    int price_;

    public:
    // Constructor
    Stock(); 
    // Deconstructor
    ~Stock();

    // Accessors and Mutators
    void set_num_available(int num_available);
    int get_num_available();
    void set_num_sold(int num_sold);
    int get_num_sold();
    void set_price(int price);
    int get_price();
    
}