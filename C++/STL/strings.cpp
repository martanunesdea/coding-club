/* Introducing strings */
#include <iostream>
#include <string>

int main() {
    std::string s1 = "This is a string";
    std::string::iterator it;

    // size and length
    std::cout << "size is same as length: " << s1.size() << std::endl;
    std::cout << "size is same as length: " << s1.length() << std::endl;

    // + for concatenation
    std::cout << "concatenated string: ";
    std::string s2 = "this is also a string";
    std::cout << s1 + ":" + s2 << std::endl;

    // compare
    std::cout << "is s1 == s2? " << (s1 == s2 ? "yes" : "no") << std::endl;
    std::cout << "copy assign s2 = s1 " << std::endl;

    // iteration
    std::cout << "each character: ";
    for ( char c : s1 ){
        std::cout << c << " ";
    }
    std::cout << std::endl;

    // insert & erase with an iterator
    it = s1.begin() + 4;
    s1.insert(it, 'X');
    std::cout << "s1 after insert: " << s1 << std::endl;

    it = s1.begin() + 4;
    s1.erase(it);
    std::cout << "s1 after insert: " << s1 << std::endl;

    // replace
    s1.replace(5, 2, "ain't");
    std::cout << "s1 after replace: " << s1 << std::endl;

    // substr
    std::cout << "substr: " << s1.substr(5, 5) << std::endl;

    // find
    size_t pos = s1.find("s");
    std::cout << "find first \"s\" in s1 (pos): " << pos << std::endl;

    // rfind
    pos = s1.rfind("s");
    std::cout << "find last \"s\" in s1 (pos): " << pos << std::endl;

    return 0;
}