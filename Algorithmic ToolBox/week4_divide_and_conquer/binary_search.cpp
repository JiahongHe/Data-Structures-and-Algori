//
//  main.cpp
//  Coursera
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

int binary_search(const vector<int> &a, int x) {
    int left = 0, right = (int)a.size();
    if (x < a[left]) {
        return 0;
    }
    int mid;
    
    while (left < right) {
        mid = (left + right) / 2;
        if (a[mid] == x) {
            return mid;
        }
        else if (a[mid] > x) {
            right = mid - 1;
        }
        else if (a[mid] < x) {
            left = mid + 1;
        }
    }
    return -1;
}

int linear_search(const vector<int> &a, int x) {
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] == x) {
            return (int)i;
        }
    }
    return -1;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); i++) {
        cin >> a[i];
    }
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }
    for (int i = 0; i < m; ++i) {
        //replace with the call to binary_search when implemented
        //cout << linear_search(a, b[i]) << ' ';
        cout << binary_search(a, b[i]) << ' ';
    }
}
