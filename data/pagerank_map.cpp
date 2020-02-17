#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define ALPHA 0.85

std::vector<std::string> split(std::string s, char delimiter) {
    std::vector<std::string> ret;

    std::istringstream strStream(s);
    std::string current;

    while ( std::getline(strStream, current, delimiter) ) {
        ret.push_back(current);
    }

    return ret;
}

int main (void) {
    std::string line;

    while ( std::getline(std::cin, line) ) {
        std::istringstream lineStream(line);
        std::string key, value;

        std::getline(lineStream, key, '\t');
        std::getline(lineStream, value);

        // std::vector<std::string> keyVal = split(line, '\t');
        // std::string key = keyVal[0], value = "\t".join ... keyVal[1];

        if (key == "iter_num") {
            std::cout << line << std::endl;
        } else {
            std::vector<std::string> vals = split(value, ',');

            float cur_rank = std::stof( vals[0] );
            std::string prev_rank = vals[1];
            // essentially maingin 'outlinks' as vals[2:] (ignoring first 2)

            int num_outlinks = vals.size() - 2;
            if ( num_outlinks == 0 ) {
                num_outlinks++;
                vals.push_back( split(key, ':')[1] );
            }

            float added_value = cur_rank * ALPHA / num_outlinks;

            for (int i = 2; i < vals.size(); i++) {
                std::cout << "NodeId:" << vals[i] << "\t"
                    << added_value << std::endl;
            }

            std::cout << key << "\t" << cur_rank << "," << prev_rank << ",";
            for (int i = 2; i < vals.size() - 1; i++) {
                std::cout << vals[i] << ",";
            }
            std::cout << vals[vals.size() - 1] << std::endl;
        }
    }
}
