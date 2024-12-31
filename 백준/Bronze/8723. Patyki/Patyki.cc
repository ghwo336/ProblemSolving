#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    int a,b,c;
    cin >>a>>b>>c;
    vector<int> vec;
    vec.push_back(a);
    vec.push_back(b);
    vec.push_back(c);
    sort(vec.begin(),vec.end());
    if (a==b && b==c){
        cout<<2;
    }
    else if(
        vec[2]*vec[2]==(vec[1]*vec[1]+vec[0]*vec[0])
    ) cout<< 1;
    else{
        cout<<0;
    }
    return 0 ; 
}
