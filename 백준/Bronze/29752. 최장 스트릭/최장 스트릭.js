fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n =Number(input[0])
let li = input[1].split(" ").map(Number);
let dap=0;
let now=0;
for (let i =0 ; i<n; i++){
    if(li[i]!=0){
        now++;
    }
    else{
        now=0
    }
    dap=Math.max(dap,now);
}
console.log(dap)