#include "queens.hpp"

using namespace std;

Queens::Queens(int Queens)
{
    Queens_ = Queens;
    count_sol_ = 0;
    board_ = new int[Queens];
    last_sol_ = new int[Queens];
}

void Queens::compute_solutions(bool print_all_solutions)
{
    solve(0, print_all_solutions);
    if ( !print_all_solutions)
    {
        board_ = last_sol_;
        print();
    }
    cout << count_sol_ << " solutions found " << endl;
}


void Queens::solve(int row, bool print_all_solutions)
{
    if ( row >= Queens_ )
    {
        count_sol_ += 1;
        memcpy(last_sol_, board_, Queens_ * sizeof(int));
        if (print_all_solutions)
        {
            print();
        }
        return;
    }
    
    for (int i = 0; i < Queens_; i++ )
    {
        if (is_safe(row, i))
        {
            board_[row] = i;
            // recursively call for next queen
            solve(row + 1, print_all_solutions);
        }
    }

}

bool Queens::is_safe(int row, int col)
{
    for(int i = 0; i < row; i++)
    {   
        if (board_[i] == col ) return false;

        if (board_[i] == col - (row - i)) return false;

        if (board_[row - 1 - i] == (col + i + 1) ) return false;
    }

    return true;
}


void Queens::print()
{
    int row, col = 0;

    cout << endl;
    
    // display array values
    for (row = 0; row < Queens_; row++)
    {
        cout << board_[row];
    }
    cout << endl;

    // display pretty board
    for (int dash = 0; dash < Queens_ * 4 + 1; dash++)
    {
        cout << "-";
    }

    cout << endl;
    for (row = 0; row < Queens_; row++)
    {
        cout << "|";
        for ( col = 0; col < Queens_; col++) 
        {
            if (board_[row] == col)
            {
                cout << " Q |";
            }
            else
            {
                cout << "   |";
            } 
        }
        cout << endl;
        for (int dash = 0; dash < Queens_ * 4 + 1; dash++)
        {
            cout << "-";
        }
        cout << endl;
    }
}

