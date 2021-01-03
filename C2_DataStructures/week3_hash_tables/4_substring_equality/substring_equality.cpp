#include <iostream>
#include <vector>
#include <random>
using namespace std;

int get_rand_uniform(int min, int max)
{
    uniform_int_distribution<int> u(min, max);
    default_random_engine e;
    return u(e);
}


class Solver {
    string s;
    vector<long long>* precomputedHash_1;
    vector<long long>* precomputedHash_2;
    int prime1;
    int prime2;
    int m1;
    int m2;
    vector<long long>* y1;
    vector<long long>* y2;
public:
    Solver(string s) : s(s) {
        prime1 = 1000000007;
        prime2 = 1000000009;
        m1 = 31; //get_rand_uniform(1,prime1-1);
        m2 = 31; //get_rand_uniform(1,prime2-1);
        precomputedHash_1 = new vector<long long>(s.size()+1, 0);
        precomputedHash_2 = new vector<long long>(s.size()+1, 0);
        y1 = new vector<long long>(s.size()+1, 0);
        y2 = new vector<long long>(s.size()+1, 0);
        size_t n = s.size()+1;

        (*y1)[0] = 1;
        (*y2)[0] = 1;
        for(int i= 1; i < n ; i++){
            (*y1)[i] = ((*y1)[i-1]*m1) % prime1;
            (*y2)[i] = ((*y2)[i-1]*m2) % prime2;
            (*precomputedHash_1)[i] = ((*precomputedHash_1)[i-1] * m1 + s[i-1]) % prime1;
            (*precomputedHash_2)[i] = ((*precomputedHash_2)[i-1] * m2 + s[i-1]) % prime2;
        }
    }

    bool ask(int a, int b, int l) {
        long long h1 = ((((*precomputedHash_1)[a + l] - (*y1)[l] * (*precomputedHash_1)[a]) % prime1) + prime1) % prime1;
        long long h2 = ((((*precomputedHash_1)[b + l] - (*y1)[l] * (*precomputedHash_1)[b]) % prime1) + prime1) % prime1;
        long long h3 = ((((*precomputedHash_2)[a + l] - (*y2)[l] * (*precomputedHash_2)[a]) % prime2) + prime2) % prime2;
        long long h4 = ((((*precomputedHash_2)[b + l] - (*y2)[l] * (*precomputedHash_2)[b]) % prime2) + prime2) % prime2;
        return h1 == h2 && h3 == h4;
    }

    bool askNaive(int a, int b, int l) {
        return s.substr(a, l) == s.substr(b, l);
    }
};

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);

    string s;
    int q;
    cin >> s >> q;
    Solver solver(s);
    for (int i = 0; i < q; i++) {
        int a, b, l;
        cin >> a >> b >> l;
        cout << (solver.ask(a, b, l) ? "Yes\n" : "No\n");
    }
}
