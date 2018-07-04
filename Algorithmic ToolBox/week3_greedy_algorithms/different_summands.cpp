//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <iostream>
#include <iterator>
#include <vector>
#include <cmath>

using namespace std;
int progression(int num) {
    return (num + 1) * num / 2;
}

int find_num (int n) {
    int max_num = (int)sqrt(2 * n) ;
    if (progression(max_num) > n){
        while (progression(max_num) > n) {
            max_num --;
        }
    }
    else if (progression(max_num) < n) {
        while (progression(max_num) < n) {
            max_num ++;
        }
        max_num --;
    }
    return max_num;
}

vector<int> optimal_summands(int n) {
    vector<int> summands;
    int max_num = find_num(n);
    int total = progression(max_num);
    for (int i = 1; i < max_num; ++i) {
        summands.push_back(i);
    }
    summands.push_back(max_num + (n - total));
    return summands;
}

int main() {
    int n;
    cin >> n;
    vector<int> summands = optimal_summands(n);
    cout << summands.size() << '\n';
    for (size_t i = 0; i < summands.size(); ++i) {
        cout << summands[i] << ' ';
    }
}


