#include <iostream>
#include <vector>
#include <deque>

using std::cin;
using std::cout;
using std::vector;
using std::deque;
using std::max;

void max_sliding_window_naive(vector<int> const & A, int w) {
    deque<int> Qi(w); // deque for indexes

    // first get candidate elements to be max from the first w elements
    // do this by remove any early element less than of equal the current element

    for (size_t i = 0; i < w; i++) {
        while (!Qi.empty() && A[i] >= A[Qi.back()])
            Qi.pop_back();

        Qi.push_back(i);
    }

    // now we have the max of the first w elements at the top of the Qi
    // we print it, replace any element out of range (<= (i - w)), then repeat the above procedure

    for (size_t i = w; i < A.size(); i++) {
        cout << A[Qi.front()] << " ";

        while (!Qi.empty() && Qi.front() <= (i - w))
            Qi.pop_front();

        while (!Qi.empty() && A[i] >= A[Qi.back()])
            Qi.pop_back();

        Qi.push_back(i);
    }

    // NOW we need to print the last Max
    cout << A[Qi.front()];

    return;
}


int main() {
    int n = 0;
    cin >> n;

    vector<int> A(n);
    for (size_t i = 0; i < n; ++i)
        cin >> A.at(i);

    int w = 0;
    cin >> w;

    max_sliding_window_naive(A, w);

    return 0;
}
