fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim();
let num=Number(input);
let fiv =0;
let dap=0;
for (let i=1;i<1000;i+=2){
    fiv+=(i*i);
    if (fiv>num) break;
    dap++;
    
}
console.log(dap)