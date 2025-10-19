
// #include <bits/stdc++.h> // This is mainly for competitive programming and
// not guarranteed to be part of a cpp compiler

// using namespace std;
#include <chrono>
#include <string>
class Timer {
public:
  Timer(std::string scope_name = "Default") : m_scope_name(scope_name) {
    start();
  }

  ~Timer() {
    if (!m_printed) {
      stop();
      print();
    }
  }

  void start() {
    m_start_time = clock::now();
    m_printed = false;
    m_started = true;
  }
  void start(std::string scope_name) {
    m_scope_name = scope_name;
    m_start_time = clock::now();
    m_printed = false;
    m_started = true;
  }

  void stop() {
    m_end_time = clock::now();
    m_started = false;
  }

  void print() {
    if (m_started)
      stop();

    const double ms =
        std::chrono::duration<double>(m_end_time - m_start_time).count() *
        1000.0;
    std::fprintf(stderr, "%s took %.4f msec\n", m_scope_name.c_str(), ms);
    m_printed = true;
  }
  double duration() {
    if (m_started)
      stop();

    return std::chrono::duration<double>(m_end_time - m_start_time).count() *
           1000.0;
  }

private:
  using clock = std::chrono::steady_clock;

  clock::time_point m_start_time;
  clock::time_point m_end_time;
  std::string m_scope_name;
  bool m_started = false;
  bool m_printed = false;
};

int main() {
  Timer t("first");
  t.print();
  t.start("second");
  t.print();
  t.start();
  t.print();
  return 0;
}
