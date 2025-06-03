fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString()
let n = Number(input)
let dap=1;
while(dap<=n){
    dap*=2;
}
console.log(dap/2);