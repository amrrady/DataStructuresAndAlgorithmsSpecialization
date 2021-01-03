#include <iostream>
#include <string>
#include <vector>
#include <random>

using namespace std;

struct Data {
    string pattern, text;
};

int get_rand_uniform(int min, int max)
{
    uniform_int_distribution<int> u(min, max);
    default_random_engine e;
    return u(e);
}

Data read_input() {
    Data data;
    cin >> data.pattern;
    cin >>  data.text;
    return data;
}

void print_occurrences(const std::vector<int>& output) {
    for (int i = 0; i < output.size(); ++i)
        std::cout << output[i] << " ";
    std::cout << "\n";
}

long long poly_hash(const string& s, int prime, int x) {
    long long hash = 0;
    for (int i = s.size() - 1; i >= 0; --i)
        hash = (hash * x + s[i]) % prime;
    return hash;
}

std::vector< long long> precomputed_Hash(string t, int sLength, int prime, int x){
    vector< long long> precomputedHash(t.size()-sLength+1, 0);
    string lastS;
    if(t.size() == sLength)
        lastS = t;
    else
        lastS = t.substr(t.size()-sLength, t.size()-1);

    precomputedHash[t.size()-sLength] = poly_hash(lastS, prime, x);
    long long y = 1;
    for(int i=0; i < sLength; i++)
        y = (y*x) % prime;

    for(int i= t.size()-sLength-1; i >= 0 ; i--){
        precomputedHash[i] = (x*precomputedHash[i+1] + t[i] - y * t[i+sLength]) % prime;
        precomputedHash[i] = (precomputedHash[i]+prime) % prime;
    }

    return precomputedHash;
}

std::vector<int> get_occurrences_Rabin_Karp(const Data& input) {
    const string& s = input.pattern, t = input.text;

    std::vector<int> ans;
    if(s.size() > t.size())
        return ans;

    const int prime = 1000000007;
    const int x = get_rand_uniform(1,prime-1);
    long long sHash = poly_hash(s,prime,x);
    vector< long long> precomputedHash = precomputed_Hash(t, s.size(), prime, x);

    for (int i = 0, m = precomputedHash.size(); i < m; ++i){
        if (sHash != precomputedHash[i])
            continue;
        string subT = t.substr(i, s.size());
        if(subT == s)
            ans.push_back(i);
    }

    return ans;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    print_occurrences(get_occurrences_Rabin_Karp(read_input()));
    return 0;
}
