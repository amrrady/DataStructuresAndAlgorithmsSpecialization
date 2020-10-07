#include <iostream>
#include <stack>
#include <string>
#include <cassert>

using std::cin;
using std::string;
using std::stack;
using std::cout;

class StackWithMax {
    stack<int> _stack;
    stack<int> _auxiliary_stack;


public:

    void Push(int value) {
        if(_stack.empty()) {
            _stack.push(value);
            _auxiliary_stack.push(value);
        } else {
            _stack.push(value);
            int current_max = value > _auxiliary_stack.top() ? value : _auxiliary_stack.top();
            _auxiliary_stack.push(current_max);
        }
    }

    void Pop() {
        assert(_stack.size());
        _stack.pop();
        _auxiliary_stack.pop();
    }

    int Max() const {
        assert(_stack.size());
        return _auxiliary_stack.top();
    }
};

int main() {
    int num_queries = 0;
    cin >> num_queries;

    string query;
    string value;

    StackWithMax stack;

    for (int i = 0; i < num_queries; ++i) {
        cin >> query;
        if (query == "push") {
            cin >> value;
            stack.Push(std::stoi(value));
        }
        else if (query == "pop") {
            stack.Pop();
        }
        else if (query == "max") {
            cout << stack.Max() << "\n";
        }
        else {
            assert(0);
        }
    }
    return 0;
}