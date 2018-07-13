#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef unsigned long long ull;

struct Data {
    string pattern, text;
};

Data read_input() {
    Data data;
    std::cin >> data.pattern >> data.text;
    return data;
}

void print_occurrences(const std::vector<int>& output) {
    for (size_t i = 0; i < output.size(); ++i)
        std::cout << output[i] << " ";
    std::cout << "\n";
}

long long hash_func(const string& s) {
    static const size_t multiplier = 263;
    static const size_t prime = 1000000007;
    long long hash = 0;
    for (int i = static_cast<int> (s.size()) - 1; i >= 0; --i)
        hash = (hash * multiplier + s[i]) % prime;
    return hash;
}

bool isEqual(string s1, string s2) {
    if (s1.length() != s2.length()) {
        return false;
    }
    return s1 == s2;
}

std::vector<int> get_occurrences(const Data& input) {
    const string& s = input.pattern, t = input.text;
    std::vector<int> ans;
    string sub_t = "";
    long long hash_s = hash_func(s);
    for (size_t i = 0; i + s.size() <= t.size(); ++i) {
        sub_t = t.substr(i, s.size());
        long long hash_t = hash_func(sub_t);
        if (hash_t == hash_s) {
            if (isEqual(sub_t, s)) {
                ans.push_back((int)i);
            }
        }
    }
    return ans;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    print_occurrences(get_occurrences(read_input()));
    return 0;
}
