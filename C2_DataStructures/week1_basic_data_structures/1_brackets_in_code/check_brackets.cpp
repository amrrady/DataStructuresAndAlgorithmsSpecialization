#include <iostream>
#include <stack>
#include <string>

using std::cout;
using std::endl;

struct Bracket {
    Bracket(char type, int position):
            type(type),
            position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

bool isOpenBracket(char c){
    return (c == '(' || c == '[' || c == '{');
}

bool isCloseBracket(char c){
    return (c == ')' || c == ']' || c == '}');
}

std::string checkBalancing(std::string& text){
    std::stack <Bracket> opening_brackets_stack;

    if(!text.empty()){
        for (int position = 0; position < text.length(); position++) {
            char next = text[position];
            if (isOpenBracket(next)) {
                if(opening_brackets_stack.empty() || isOpenBracket(opening_brackets_stack.top().type))
                    opening_brackets_stack.push(Bracket(next, position));
                else
                    return std::to_string(position+1);
            }

            if (isCloseBracket(next)) {
                if(!opening_brackets_stack.empty() && opening_brackets_stack.top().Matchc(next))
                        opening_brackets_stack.pop();
                else
                    return std::to_string(position+1);
            }
        }
    }

    if(opening_brackets_stack.empty())
        return "Success";

    return std::to_string(opening_brackets_stack.top().position+1);
}

int main() {
    std::string text;
    getline(std::cin, text);
    cout << checkBalancing(text) << endl;
    return 0;
}
