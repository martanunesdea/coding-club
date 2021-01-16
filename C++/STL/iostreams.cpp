/* handling files with STL library */
#include <iostream>
#include <fstream>

int main() {
    static int lineno = 0;
    static const char * filename = "test.txt";
    static const char * textstring = "This is the test file";

    // writing to a file
    std::cout << "write the file: " << std::endl;
    std::ofstream output_file(filename);
    output_file << ++lineno << " " << textstring << std::endl;
    output_file << ++lineno << " " << textstring << std::endl;
    output_file << ++lineno << " " << textstring << std::endl;
    output_file.close();

    // reading a file
    static char buf[128];
    std::cout << "read the file: " << std::endl;
    std::ifstream input_file(filename);
    
    while (input_file.good()){
        input_file.getline(buf, sizeof(buf));
        std::cout << buf << std::endl;
    }
    input_file.close();

    // delete file
    std::cout << "delete file." << std::endl;
    remove(filename);
    return 0;
}