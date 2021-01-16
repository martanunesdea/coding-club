/* Intro to vectors */
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::cout << "Vector from pre-determined list: " << std::endl;
    std::vector<int> v1 = {1,2,3,4,5,6,7,8,9,10};

    std::cout << "size: " << v1.size() << std::endl;
    std::cout << "front: " << v1.front() << std::endl;
    std::cout << "back: " << v1.back() << std::endl;
    std::cout << std::endl;

    // iterator
    std::vector<int>::iterator it_begin = v1.begin();
    std::vector<int>::iterator it_end = v1.end();
    // this would also work: auto it_begin = v1.begin()
    
    for ( auto it = it_begin; it < it_end; ++it)
    {
        std::cout << *it << ' ';
    }
    // this would also work: for (auto it = v1.begin(); it < v1.end(); ++it)
    std::cout << std::endl;

    // looking up by position
    std::cout << "element 8: " << v1.at(8) << std::endl;
    std::cout << "element 6: " << v1[6] << std::endl;

    // range-based for loop
    std::cout << "range-based for loop: " << std::endl;
    for ( int i : v1 ){
        std::cout << i << ' ';
    }
    std::cout << std::endl << std::endl;

    std::cout << "Insert 13 at begin+3: " << std::endl;
    v1.insert(v1.begin()+3, 13);
    std::cout << "size: " << v1.size() << std::endl;
    std::cout << "v1[3]: " << v1[3] << std::endl;

    std::cout << "Erase at begin+3: " << std::endl;
    v1.erase(v1.begin()+3);
    std::cout << "size: " << v1.size() << std::endl;
    std::cout << "v1[3]: " << v1[3] << std::endl;

    // add at the end
    std::cout << "Push back 11: " << std::endl;
    v1.push_back(11);
    std::cout << "size: " << v1.size() << std::endl;
    std::cout << "v1.back(): " << v1.back() << std::endl;
    std::cout << std::endl;

    // std::vector of strings
    std::cout << "vector of strings" << std::endl;
    std::vector<std::string> vs = {"one", "two", "three", "four", "five"};
    for(const std::string & v : vs){
        std::cout << v << std::endl;
    }

    return 0;

}