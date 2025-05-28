fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString()
let n = Number(input)
let fiv=10000000000000;
let dap=-1;
for (let i = 0 ; i<10000; i++){
    if (String(i).padStart(2,"0").slice(-2)=="99"){
        if (fiv>=Math.abs(n-i)){
            fiv=Math.abs(n-i);
            dap=i;
        }
    }
}
console.log(dap)