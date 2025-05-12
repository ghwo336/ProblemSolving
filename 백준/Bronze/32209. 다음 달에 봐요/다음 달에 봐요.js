fs=require("fs")
input=fs.readFileSync("/dev/stdin").toString().trim().split('\n')
n=Number(input[0])
let fiv = 0;
let sol=()=>{
    for (let i =1; i<=n;i++){
        let [a,b]=input[i].split(' ').map(Number);
        if (a==1) fiv+=b;
        else fiv-=b
        if (fiv<0) {
            console.log("Adios")
            return
        }   
}
    console.log("See you next month");
    return
}
sol();