//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<double> get_unit_values(vector<int> weights, vector<int> values) {
    long n = weights.size();
    vector<double> unit_values(n);
    for (int i = 0; i < n; i++) {
        unit_values[i] = values[i] / (double)weights[i];
    }
    return unit_values;
}

int find_highest(vector<double> unit_values, vector<int> already_picked) {
    double highest_val = 0.0;
    int highest_index = -1;
    long n = unit_values.size();
    for (int i = 0; i < n; i++) {
        if (unit_values[i] > highest_val) {
            if (find(already_picked.begin(), already_picked.end(), i) != already_picked.end()){
                continue;
            }
            highest_val = unit_values[i];
            highest_index = i;
        }
    }
    return highest_index;
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
    double value = 0.0;
    long n = weights.size();
    vector<double> unit_value(n);
    vector<int> already_picked;
    unit_value = get_unit_values(weights, values);
    while (capacity > 0) {
        int best_item = find_highest(unit_value, already_picked);
        if (capacity > weights[best_item]) {
            value += values[best_item];
            already_picked.push_back(best_item);
            capacity -= weights[best_item];
        }
        else {
            value += (double)capacity / weights[best_item] * values[best_item];
            capacity = 0;
        }
        if (already_picked.size() == weights.size()) {
            break;
        }
    }
    return value;
}

int main() {
    int n;
    int capacity;
    std::cin >> n >> capacity;
    vector<int> values(n);
    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        std::cin >> values[i] >> weights[i];
    }
    
    double optimal_value = get_optimal_value(capacity, weights, values);
    
    std::cout.precision(10);
    std::cout << optimal_value << std::endl;
    return 0;
}
