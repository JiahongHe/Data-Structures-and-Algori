//
//  main.cpp
//  EDX
//
//  Created by Jiahong He on 6/25/18.
//  Copyright © 2018 Jiahong He. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using namespace std;
struct Segment {
    int start, end;
};
bool compareByStart(const Segment &a, const Segment &b) {return a.start < b.start;}

vector<int> optimal_points(vector<Segment> &segments) {
    vector<int> points;
    std::sort(segments.begin(), segments.end(), compareByStart);
    int point = segments[0].end;
    for (size_t i = 1; i < segments.size(); ++i) {
        if (segments[i].start > point) {
            points.push_back(point);
            point = segments[i].end;
        }
        else if (segments[i].end < point) {
            point = segments[i].end;
        }
    }
    points.push_back(point);
    return points;
}

int main() {
    int n;
    std::cin >> n;
    vector<Segment> segments(n);
    for (size_t i = 0; i < segments.size(); ++i) {
        std::cin >> segments[i].start >> segments[i].end;
    }
    vector<int> points = optimal_points(segments);
    std::cout << points.size() << "\n";
    for (size_t i = 0; i < points.size(); ++i) {
        std::cout << points[i] << " ";
    }
}


