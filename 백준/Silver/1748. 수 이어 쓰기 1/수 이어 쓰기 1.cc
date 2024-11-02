#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long long min(long long a, long long b){
    if(a<b) return a;
    return b;
}

int main() {
    long long dap;
    long long N;
    cin>>N;
    dap+=min(9,N);
    if (N>=10){
        dap+=2*(min(90,N-9));
    }
    if (N>=100){
        dap+=3*(min(900,N-99));
    }
    if(N>=1000){
        dap+=4*(min(9000,N-999));
    }
    if(N>=10000){
        dap+=5*(min(90000,N-9999));
    }
    if(N>=100000){
        dap+=6*(min(900000,N-99999));
    }
    if(N>=1000000){
        dap+=7*(min(9000000,N-999999));
    }
    if(N>=10000000){
        dap+=8*(min(90000000,N-9999999));
    }
    if (N==100000000) dap+=9;

    cout<<dap;
    
    
}