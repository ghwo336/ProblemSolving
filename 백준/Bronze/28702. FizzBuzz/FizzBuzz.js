fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let dap=0;
for(let i=1; i<=3; i++){
    let now = input[i-1];
    if (now!=="Fizz"&&now!=="Buzz"&&now!=="FizzBuzz"){
        dap=Number(now)+4-i;
        break;
    }
}

if (dap%15==0) console.log("FizzBuzz");
else if (dap%3==0) console.log("Fizz");
else if (dap%5==0) console.log("Buzz");
else console.log(dap)
