//
//  main.cpp
//  Coursera
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
/*
void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void merge(vector<int> &a, int low ,int high, int mid) {
    int i, j, k, temp[high-low+1];
    i = low;
    k = 0;
    j = mid + 1;
    while (i <= mid && j <= high) {
        if (a[i] < a[j]) {
            temp[k] = a[i];
            k++;
            i++;
        }
        else {
            temp[k] = a[j];
            k++;
            j++;
        }
    }
    
    while (i <= mid){
        temp[k] = a[i];
        k++;
        i++;
    }
    
    while (j <= high) {
        temp[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i <= high; i++) {
        a[i] = temp[i-low];
    }
}

void mergeSort(vector<int> &a, int low, int high) {
    int mid;
    if (low < high) {
        mid=(low+high)/2;
        mergeSort(a, low, mid);
        mergeSort(a, mid+1, high);
        merge(a, low, high, mid);
    }
}
 */
int get_majority_element(vector<int> &a, int left, int right) {
    if (left == right) return -1;
    if (left + 1 == right) return a[left];
    sort (a.begin(), a.begin() + a.size());
    int curr_num = -1;
    int count = 0;
    for (int i = 0; i < a.size(); ++i) {
        if (curr_num != a[i]) {
            if (count * 2 > a.size()) {
                return 1;
            }
            else {
                curr_num = a[i];
                count = 1;
            }
        }
        else {
            count ++;
        }
    }
    if (count * 2 > a.size()) {
        return 1;
    }
    return 0;
}
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i) {
        cin >> a[i];
    }
    cout << get_majority_element(a, 0, (int)a.size()) << '\n';
}

