fs=require("fs")
input=fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [p,n]=input[0].split(" ").map(Number);
let li=input[1].split(" ").map(Number);
li.sort((a,b)=>a-b);

let dap=0;
if (p>=200) console.log(0);
else{
    for (let i of li){
    if (i+p<=200){
        dap++;
        p+=i
        if (p==200)break
    }
    else {
        dap++;
        break;
    }
}
console.log(dap)
    
}

