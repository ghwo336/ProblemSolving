fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let [n,m] = input[0].split(" ").map(Number)
let li = new Array(n+1).fill(0);

for (let i =1 ; i<=m; i++){
    let [a,b]=input[i].split(" ").map(Number);
    li[a]+=1;
    li[b]+=1;
}

for( let i =1 ; i<=n;i++){
    console.log(li[i])
}