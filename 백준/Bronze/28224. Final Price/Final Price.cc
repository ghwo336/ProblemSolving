#include <iostream>

int main() {
    int n;
    std::cin>>n;
    int dap{0};
    for (int i=0;i<n;i++){
        int a;
        std::cin>>a;
        dap+=a;
    }
    std::cout<<dap;
    return 0;
}