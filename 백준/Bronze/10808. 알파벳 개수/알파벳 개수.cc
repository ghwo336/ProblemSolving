#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    cin>>s;
    int a[26]={};
    for (char &c:s){
        a[int(c)-97]+=1;
    }
    for (int i =0 ; i<26; i++){
        cout<<a[i]<<' ';
    }
}