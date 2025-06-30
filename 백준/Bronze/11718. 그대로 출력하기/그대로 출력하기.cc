#include <iostream>
using namespace std;

int main() {
    string s;
    getline(cin,s);
    while (!std::cin.eof()){
        std::cout<<s<<"\n";
        getline(cin,s);
    }
}