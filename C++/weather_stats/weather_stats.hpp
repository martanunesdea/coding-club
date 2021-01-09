/* Header file */
#ifndef WEATHER_STATS_HPP
#define WEATHER_STATS_HPP

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <ctime>

#define FILE_PATH "./files/"


void weather_stats_load_data();
time_t weather_stats_convert_date_time(std::string date, std::string time);
int is_valid(std::string date, std::string time);
double compute_coeff(std::string start_date, std::string start_time, std::string end_date, std::string end_time);

#endif // WEATHER_STATS_H_