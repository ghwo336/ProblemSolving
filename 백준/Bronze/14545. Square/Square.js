fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
n=Number(input[0]);
for(let i =1 ; i<=n; i++){
    let a = Number(input[i]);
    console.log(a*(a+1)*(2*a+1)/6);
}