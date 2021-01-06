/* Source file for application code */
#include "weather_stats.hpp"

using namespace std;
std::map<time_t, double> time_to_pressure; 


void weather_stats_load_data(void)
{
    for ( int year = 2012; year < 2016; year++)
    {
        ostringstream filename_stream;
        filename_stream << FILE_PATH << "Environmental_Data_Deep_Moor_" << year << ".txt";
        string filename = filename_stream.str();
        cout << "Loading " << filename << "... " << endl;

        fstream file_stream;
        file_stream.open(filename);

        string line;
        getline(file_stream, line); // ignore first line (headers)
        while (getline(file_stream, line))
        {
            string date, time;
            double Air_Temp, Barometric_Press, Dew_Point, Relative_Humidity,Wind_Dir, Wind_Gust, Wind_Speed;
            istringstream buffer(line);

            buffer >> date >> time >> Air_Temp >> Barometric_Press >> Dew_Point >> Relative_Humidity >> Wind_Dir >> Wind_Gust >> Wind_Speed;
            time_t dateTime = weather_stats_convert_date_time(date, time);
            time_to_pressure[dateTime] = Barometric_Press;
        }

        file_stream.close();
    }
}

time_t weather_stats_convert_date_time(string date, string time)
{
    int yyyy, mon, dd = 0;
    int hh, mm, ss = 0;

    if (sscanf(date.c_str(), "%d_%d_%d", &yyyy, &mon, &dd) != 3)
    {
        cerr << "ERROR: Failed to parse date string " << date << endl;
        return -1;
    }

    if (sscanf(time.c_str(), "%d:%d:%d", &hh, &mm, &ss) != 3)
    {
        cerr << "ERROR: Failed to parse time string " << date << endl;
        return -2;
    }
    
    struct tm dateTime = {};
    dateTime.tm_year = yyyy - 1900; // years since 1900
    dateTime.tm_mon = mon - 1;      // months since January
    dateTime.tm_mday = dd;          // day of the month
    dateTime.tm_hour = hh;          // hours since midnight
    dateTime.tm_min = mm;           // minutes after the hour
    dateTime.tm_sec = ss;           // seconds after the minute

    // return a time_t value representing seconds since 1970
    return mktime(&dateTime);
}

int is_valid(string date, string time)
{
    return 1;
}

double compute_coeff(string start_date, string start_time, string end_date, string end_time)
{
    time_t start_datetime = weather_stats_convert_date_time(start_date, start_time);
    time_t end_datetime = weather_stats_convert_date_time(end_date, end_time);

    if (end_datetime < start_datetime)
    {
        cerr << "ERROR: The start date/time must occur before the end date/time" << endl;
        exit(1);
    }

    // find iterators based on input range
    map<time_t, double>::iterator start_time_pressure;
    map<time_t, double>::iterator end_time_pressure;
    start_time_pressure = time_to_pressure.lower_bound(start_datetime);
    end_time_pressure = time_to_pressure.lower_bound(end_datetime);

    // Extract time and timeToPressure values
    double time_difference = end_time_pressure->first - start_time_pressure->first;
    double pressure_difference = end_time_pressure->second - start_time_pressure->second;

    // calculate and return slope
    return (pressure_difference) / (time_difference);
}