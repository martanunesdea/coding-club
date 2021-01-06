/* Entry point for weather stats application */
#include <iostream>
#include <string>
#include "weather_stats.hpp"

using namespace std;


int main()
{
    cout << "Welcome to the weather calculator" << endl;
    weather_stats_load_data();

    string start_date, start_time;
    do 
    {
        cout << endl << "Enter START DATE as yyyy_mm_dd: ";
        cin >> start_date;
        cout << "Enter START TIME as hh:mm:ss (24-hour): ";
        cin >> start_time;
    } while ( !is_valid(start_date, start_time) );


    string end_date, end_time;
    do {
        cout << endl << "Enter END DATE as yyyy_mm_dd: ";
        cin >> end_date;
        cout << "Enter END TIME as hh:mm:ss (24-hour): ";
        cin >> end_time;
    } while ( !is_valid(end_date, end_time) );


    // compute coefficient
    double coeff = compute_coeff(start_date, start_time, end_date, end_time);

    cout << "Coefficient is " <<  coeff * 24 * 60 * 60 << " inHg/day" << "\n";

}