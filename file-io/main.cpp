/* Loading and saving to a file */
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream inStream;
    inStream.open("file.txt");
    int userGuess = 0;
    string password;

    if ( !inStream.fail() )
    {
        while( inStream >> password )
        {
            cout << "The password is: " << password << endl;
            cout << "What is your answer? \n";
            cin >> userGuess;
            if ( userGuess == password.length() )
            {
                cout << "Congrats\n";
            }
            else
            {
                cout << "Sorry try again later\n";
            }
            
        }
    }
    inStream.close();

    ofstream outputFile;
    outputFile.open("file.txt", ios::app); // add app to prevent overwriting
    outputFile << "\nhello it's me\n" << endl;

    outputFile.close();

}