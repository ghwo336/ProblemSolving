fs=require("fs");
input=fs.readFileSync('/dev/stdin').toString().trim()
const num=Number(input)
console.log(num*(num+1)/2)