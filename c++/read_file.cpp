#include <iostream>
#include <fstream>

int main()
{
    std::ifstream in_stream;
    in_stream.open("myfile.txt");
    int user_answer = 0;
    std::string password;

    if ( !in_stream.fail() )
    {
        while(in_stream >> password)
        {
            std::cout << "The password is: " << password << std::endl;
            std::cout << "What's the answer? ";
            std::cin >> user_answer;
            if ( user_answer == password.length() ) std::cout << "Correct\n";
            else std::cout << "Try again\n";
        
        }
    }
    in_stream.close();
}