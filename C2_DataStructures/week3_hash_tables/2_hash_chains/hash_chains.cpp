#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

struct Query {
    string type, s;
    size_t ind;
};

class QueryProcessor {
    int bucket_count;
    // store all strings in one vector
    vector<list<string>>* elems;
public:

    QueryProcessor() : bucket_count(300) {
        this->elems = new vector<list<string>>(bucket_count,list<string>());
    }

    QueryProcessor(int bucket_count) : bucket_count(bucket_count) {
        this->elems = new vector<list<string>>(bucket_count,list<string>());
    }

    ~QueryProcessor(){
        delete this->elems;
        this->elems = nullptr;
    }

    size_t hash_func(const string& s) const {
        static const size_t multiplier = 263;
        static const size_t prime = 1000000007;
        unsigned long long hash = 0;
        for (int i = static_cast<int> (s.size()) - 1; i >= 0; --i)
            hash = (hash * multiplier + s[i]) % prime;
        return hash % bucket_count;
    }

    Query readQuery() const {
        Query query;
        cin >> query.type;
        if (query.type != "check")
            cin >> query.s;
        else
            cin >> query.ind;
        return query;
    }

    void writeSearchResult(bool was_found) const {
        std::cout << (was_found ? "yes\n" : "no\n");
    }

    void processQuery(const Query& query) {
        if (query.type == "check") {

            for (auto it = (*elems)[query.ind].begin(), end = (*elems)[query.ind].end(); it != end; it++)
                std::cout << *it << " ";
            std::cout << "\n";
        } else if (query.type == "find") {
            bool was_found = false;
            int index = hash_func(query.s);
            for (auto it = (*elems)[index].begin(), end = (*elems)[index].end(); it != end; it++) {
                if (*it == query.s) {
                    was_found = true;
                }
            }
            writeSearchResult(was_found);
        } else if (query.type == "add") {
            int index = hash_func(query.s);
            for (auto it = (*elems)[index].begin(), end = (*elems)[index].end(); it != end; it++) {
                if (*it == query.s) {
                    return;
                }
            }

            (*elems)[hash_func(query.s)].push_front(query.s);
        } else if (query.type == "del") {
            int index = hash_func(query.s);
            for (auto it = (*elems)[index].begin(), end = (*elems)[index].end(); it != end; it++) {
                if (*it == query.s) {
                    (*elems)[hash_func(query.s)].erase(it);
                    return;
                }
            }
        }
    }

    void processQueries() {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            processQuery(readQuery());
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    int bucket_count;
    cin >> bucket_count;
    QueryProcessor proc(bucket_count);
    proc.processQueries();
    return 0;
}
