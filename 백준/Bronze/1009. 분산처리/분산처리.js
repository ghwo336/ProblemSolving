fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let t = Number(input[0])

const sol=(a,b)=>{
    let x = 1;
    for ( let i =1 ; i<=b; i++){
        x=(x*a)%10;
    }
    if (x==0) x=10;
    console.log(x)
}

for (let i =1 ; i<=t; i++){
    let [a,b]=input[i].split(" ").map(Number);
    sol(a,b);
}
