//
//  Created by Jiahong He on 6/29/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <limits>

using namespace std;

long long eval(long long a, long long b, char op) {
    if (op == '*') {
        return a * b;
    } else if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else {
        assert(0);
    }
}

long long * get_max_min (int i,int j,vector<vector<long long>> &M, vector<vector<long long>> &m, vector<char> &ops) {
    long long Max = numeric_limits<long long>::infinity();
    long long Min = - numeric_limits<long long>::infinity();
    for (int k = i; k < j; k++) {
        long long m1 = (eval(M[i][k], M[k + 1][j], ops[k]));
        long long m2 = (eval(M[i][k], m[k + 1][j], ops[k]));
        long long m3 = (eval(m[i][k], M[k + 1][j], ops[k]));
        long long m4 = (eval(m[i][k], m[k + 1][j], ops[k]));
        Max = max(max(max(max(m1, m2), m3), m4), Max);
        Min = min(min(min(min(m1, m2), m3), m4), Min);
    }
    static long long result[2];
    result[0] = Max;
    result[1] = Min;
    return result;
}

long long get_maximum_value(const string &exp) {
    long long max = 0;
    vector<char> ops;
    vector<int> nums;
    for (int i = 0; i < exp.length(); i++) {
        if (i % 2 == 0) {
            nums.push_back(exp.at(i)-'0');
        }
        else {
            ops.push_back(exp.at(i));
        }
    }
    int n = (int)nums.size();
    vector<vector<long long >> M (n, vector<long long>(n, 0));
    vector<vector<long long >> m (n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) {
        M[i][i] = nums[i];
        m[i][i] = nums[i];
    }
    int j;
    for (int s = 1; s< n; s++) {
        for (int i = 0; i < n - s; i++) {
            j = i + s;
            long long * temp;
            temp = get_max_min(i, j, M, m, ops);
            M[i][j] = temp[0];
            m[i][j] = temp[1];
        }
    }
    return M[0][n - 1];
}

int main() {
    string s;
    std::cin >> s;
    std::cout << get_maximum_value(s) << '\n';
}
