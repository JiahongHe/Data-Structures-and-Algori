//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

long MaxPairwiseProduct(const vector<int>& numbers) {
    long result = 0;
    long biggest = -1;
    long second_biggest = -1;
    long n = numbers.size();
    for (int i = 0; i < n; ++i) {
        if (numbers[i] > biggest) {
            second_biggest = biggest;
            biggest = numbers[i];
        }
        else if (numbers[i] > second_biggest) {
            second_biggest = numbers[i];
        }
    }
    result = biggest * second_biggest;
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    
    long result = MaxPairwiseProduct(numbers);
    cout << result << endl;
    return 0;
}
