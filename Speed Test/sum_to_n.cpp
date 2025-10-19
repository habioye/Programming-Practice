// C++ code
#include <iostream>
#include <chrono>
#include <typeinfo>
#include "yaml-cpp/yaml.h"


long long sum_cpp(int n) {
    long long result = 0;
    for (int i = 1; i <= n; ++i) {
        result += i;
    }
    return result;
}

int main() {
    int n = 10000000;
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time = std::chrono::high_resolution_clock::now();
//  std::cout << typeid(start_time).name() << std::endl;
    long long sum_result = sum_cpp(n);
    std::chrono::time_point<std::chrono::high_resolution_clock> end_time = std::chrono::high_resolution_clock::now(); // Wait for the user to respond.
    std::chrono::microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    std::cout << "C++: Sum of 1 to " << n << " is " << sum_result << " calculated in " << duration.count() / 1000000.0 << " seconds" << std::endl;
    return 0;
}
