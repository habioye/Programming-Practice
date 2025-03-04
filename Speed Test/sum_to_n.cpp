// C++ code
#include <iostream>
#include <chrono>

long long sum_cpp(int n) {
    long long result = 0;
    for (int i = 1; i <= n; ++i) {
        result += i;
    }
    return result;
}

int main() {
    int n = 10000000;
    auto start_time = std::chrono::high_resolution_clock::now();
    long long sum_result = sum_cpp(n);
    auto end_time = std::chrono::high_resolution_clock::now(); // Wait for the user to respond.
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    std::cout << "C++: Sum of 1 to " << n << " is " << sum_result << " calculated in " << duration.count() / 1000000.0 << " seconds" << std::endl;
    return 0;
}
