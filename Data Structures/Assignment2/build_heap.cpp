#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;
using std::max;

class HeapBuilder {
private:
    vector<int> data_;
    vector< pair<int, int> > swaps_;
    
    void WriteResponse() const {
        cout << swaps_.size() << "\n";
        for (int i = 0; i < swaps_.size(); ++i) {
            cout << swaps_[i].first << " " << swaps_[i].second << "\n";
        }
    }
    
    void ReadData() {
        int n;
        cin >> n;
        data_.resize(n);
        for(int i = 0; i < n; ++i)
            cin >> data_[i];
    }
    
    int parent(int i) {
        if (i >0) {
            return (i - 1) / 2;
        }
        else {
            return i;
        }
    }
    
    int left_child(int i) { return 2 * i + 1; }
    
    int right_child(int i) { return 2 * i + 2; }
    
    void shit_up(int i) {
        while (i > 0 && data_[parent(i)] > data_[i]) {
            swap(data_[i], data_[parent(i)]);
            swaps_.push_back(make_pair(i, parent(i)));
            i = parent(i);
        }
    }
    
    void shift_down(int i) {
        int l = left_child(i);
        int r = right_child(i);
        int minIndex = i;
        if (l < data_.size() && data_[l] < data_[minIndex]) {
            minIndex = l;
        }
        if (r < data_.size() && data_[r] < data_[minIndex]) {
            minIndex = r;
        }
        if (i != minIndex) {
            swap(data_[i], data_[minIndex]);
            swaps_.push_back(make_pair(i, minIndex));
            shift_down(minIndex);
        }
    }
    
    void GenerateSwaps() {
        swaps_.clear();
        int size = (int)data_.size();
        for (int i = size/2; i >= 0; i--)  {
            shift_down(i);
        }
        
    }
    
public:
    void Solve() {
        ReadData();
        GenerateSwaps();
        WriteResponse();
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    HeapBuilder heap_builder;
    heap_builder.Solve();
    return 0;
}
