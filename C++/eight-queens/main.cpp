/* Entry point the Eight Queens program 
 * Author: Marta 
 * Date: 10/01/201
 * Compiler: clang v11
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include "queens.hpp"
using namespace std;


int main(int argc, char* argv[]) 
{
	if (argc <= 1)
	{
		cerr << "ERROR: Missing argument for board dimensions" << endl;
		return 1;
	}
    
	if (atoi(argv[1]) < 4)
	{
		cerr << "ERROR: Invalid board dimensions; first argument must be integer >= 4" << endl;
		return 2;
	}
    
	Queens nq = Queens(atoi(argv[1]));
	nq.compute_solutions(argv[2]);

	return 0;
}