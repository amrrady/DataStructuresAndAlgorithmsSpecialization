#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;

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

    int getParent(int i){
        if(i > 0)
            return (i-1)/2;
        return 0;
    }

    int getLeftChild(int i){
        return (2*i + 1);
    }

    int getRightChild(int i){
        return (2*i + 2);
    }

    void SiftDown(int i){
        int maxIndex = i;
        int left  = getLeftChild(i);
        int right = getRightChild(i);

        if(left < this->data_.size() && this->data_[left] < this->data_[maxIndex])
            maxIndex = left;

        if(right < this->data_.size() && this->data_[right] < this->data_[maxIndex])
            maxIndex = right;

        if(maxIndex != i){
            swap(data_[i], data_[maxIndex]);
            swaps_.push_back(make_pair(i, maxIndex));
            SiftDown(maxIndex);
        }
    }

    void GenerateSwaps() {
        swaps_.clear();
        for (int i = data_.size()/2; i >= 0; i--)
            SiftDown(i);
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
