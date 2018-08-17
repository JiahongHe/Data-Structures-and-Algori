#include <string>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef map<char, int> edges;
typedef vector<edges> trie;

bool find_val(map<char, int> edges, char key) {
    map<char, int>::iterator it;
    it = edges.find(key);
    if (it != edges.end()) {
        return true;
    }
    return false;
}

trie build_trie(vector<string> & patterns) {
    trie t;
    t.push_back(map<char, int>());
    int node_count = 1;
    for (string pattern: patterns) {
        int curr_node = 0;
        for (char c: pattern) {
            if (!find_val(t[curr_node], c)) {
                t[curr_node].insert(make_pair(c, node_count));
                t.push_back(map<char, int>());
                node_count++;
            }
            curr_node = t[curr_node][c];
        }
    }
    return t;
}

int main() {
    size_t n;
    std::cin >> n;
    vector<string> patterns;
    for (size_t i = 0; i < n; i++) {
        string s;
        std::cin >> s;
        patterns.push_back(s);
    }
    
    trie t = build_trie(patterns);
    for (size_t i = 0; i < t.size(); ++i) {
        for (const auto & j : t[i]) {
            std::cout << i << "->" << j.second << ":" << j.first << "\n";
        }
    }
    
    return 0;
}
