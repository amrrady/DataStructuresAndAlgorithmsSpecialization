#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

class JobQueue {
private:
    int num_workers_;
    vector<int> jobs_;

    vector<int> assigned_workers_;
    vector<long long> start_times_;

    void WriteResponse() const {
        for (int i = 0; i < jobs_.size(); ++i) {
            cout << assigned_workers_[i] << " " << start_times_[i] << "\n";
        }
    }

    void ReadData() {
        int m;
        cin >> num_workers_ >> m;
        jobs_.resize(m);
        for(int i = 0; i < m; ++i)
            cin >> jobs_[i];
    }

    void AssignJobs() {
        // TODO: replace this code with a faster algorithm.
        assigned_workers_.resize(jobs_.size());
        start_times_.resize(jobs_.size());
        priority_queue<pair<long long, int>, std::vector< pair<long long, int> >, std::greater< pair<long long, int> > > next_free_time;
        for (int i = 0; i < num_workers_; i++) {
            next_free_time.push(make_pair(0, i));
        }

        for (int i = 0; i < jobs_.size(); ++i) {
            int duration = jobs_[i];
            int next_worker = next_free_time.top().second;
            assigned_workers_[i] = next_worker;
            start_times_[i] = next_free_time.top().first;
            next_free_time.pop();
            next_free_time.push(make_pair(start_times_[i] + duration, next_worker));
        }
    }

public:
    void Solve() {
        ReadData();
        AssignJobs();
        WriteResponse();
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    JobQueue job_queue;
    job_queue.Solve();
    return 0;
}
