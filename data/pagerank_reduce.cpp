#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <vector>
#include <unordered_map>

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
    std::unordered_map< std::string, std::vector<std::string> > lineMap;

    while ( std::getline(std::cin, line) ) {
        std::istringstream lineStream(line);
        std::string key, value;

        std::getline(lineStream, key, '\t');
        std::getline(lineStream, value);

        if (key == "iter_num") {
            std::cout << line << std::endl;
        } else if (lineMap.count(key) == 0) {
            std::vector<std::string> vals;
            vals.push_back(value);
            lineMap[key] = vals;
        } else {
            lineMap[key].push_back(value);
        }
    }

    for( const auto& pair : lineMap ) {
        float sum = 1.0 - ALPHA;
        std::vector<std::string> ranksOutlinks;

        for (std::string s : pair.second) {
            if (s.find(",") == std::string::npos) {
                sum += std::stof(s);
            } else {
                ranksOutlinks = split(s, ',');
            }
        }

        ranksOutlinks[1] = ranksOutlinks[0];
        ranksOutlinks[0] = std::to_string(sum);

        std::cout << pair.first << "\t";
        for (int i = 0; i < ranksOutlinks.size() - 1; i++) {
            std::cout << ranksOutlinks[i] << ",";
        }
        std::cout << ranksOutlinks[ ranksOutlinks.size() - 1 ] << std::endl;
    }
}
