//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//

#include <iostream>
using namespace std;

int get_change(int m) {
    int count_10 = 0;
    int count_5 = 0;
    int count_1 = 0;
    int n = 0;
    if (m >= 10) {
        count_10 = m / 10;
        int residule = m % 10;
        m = residule;
    }
    if (m >= 5) {
        count_5 = m / 5;
        int residule = m % 5;
        m = residule;
    }
    if (m >= 1) {
        count_1 = m / 1;
    }
    n = count_10 + count_5 + count_1;
    return n;
}

int main() {
    int m;
    cin >> m;
    cout << get_change(m) << '\n';
}
