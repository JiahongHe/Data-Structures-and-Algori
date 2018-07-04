//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

string largest_number(vector<string> num) {
    vector<string> arr;
    for(auto i:num)
        arr.push_back(i);
    sort(begin(arr), end(arr), [](string &s1, string &s2){ return s1+s2>s2+s1; });
    string res;
    for(auto s:arr)
        res+=s;
    while(res[0]=='0' && res.length()>1)
        res.erase(0,1);
    return  res;
}

int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (size_t i = 0; i < a.size(); i++) {
        cin >> a[i];
    }
    cout << largest_number(a);
}

