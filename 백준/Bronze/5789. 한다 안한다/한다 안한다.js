fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
n=Number(input[0])
for (let i = 1 ; i<=n ; i++){
    let s = input[i]
    let start =0;
    let end=s.length-1;
    let mid = (start+end-1)/2;
    if (s[mid]==s[mid+1]) console.log("Do-it");
    else console.log("Do-it-Not");
}