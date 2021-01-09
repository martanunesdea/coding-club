#ifndef _QUEENS_H_
#define _QUEENS_H_

#include <iostream>
#include <cstring>

class Queens
{
public:
	Queens(int Queens);
	void compute_solutions(bool print_all_solutions);

private:
	int* board_ = NULL;
	int* last_sol_ = NULL;
	int Queens_, count_sol_ = 0;

	void solve(int row, bool printAllSolns);
	bool is_safe(int row, int col);
	void print();
};

#endif // _QUEENS_H_