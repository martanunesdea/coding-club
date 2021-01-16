/* Introducing exceptions */ 
#include <iostream>
#include <exception>

namespace EXC {
    class E: public std::exception {
        const char * msg;
        E();
    public:
        E(const char *s) noexcept(true) : msg(s) {}
        const char * what() const noexcept(true) { return msg; }
    };
}

const EXC::E e_no_input("No input provided");
const EXC::E e_too_many_inputs("Too many inputs provided");
const EXC::E e_undefined("Undefined");


void broken() {
    std::cout << "This is a broken function" << std::endl;
    throw e_undefined;
}

int main(){
    std::cout << "What happens when there's an exception? " << std::endl;
    try {
        broken();
    } catch( EXC::E & e) {
        std::cout << e.what() << std::endl;
    }
    return 0;
}

