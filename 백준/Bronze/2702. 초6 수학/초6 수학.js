function gcd (a,b){
    while(b!=0){
        const temp=b;
        b=a%b;
        a=temp
    }
    return a;
}
function lcm(a,b){
    return(a*b)/gcd(a,b);
}

fs=require('fs');
input=fs.readFileSync('/dev/stdin').toString().trim().split('\n');
n=input[0]
for (let i =1; i<=n;i++ ){
    let  [a,b]=input[i].split(' ')
    console.log(lcm(a,b),gcd(a,b))
}
