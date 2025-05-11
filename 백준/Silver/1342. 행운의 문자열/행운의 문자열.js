fs=require("fs")
input=fs.readFileSync("/dev/stdin").toString().trim();
n=input.length
let visit=new Array(n).fill(false)
let uniqueSet = new Set();
const dfs=(l,s)=>{
    if (l==n){
        for (let i =1 ; i<n;i++){
            if (s[i-1]==s[i]){
                return;
            }
        }
        uniqueSet.add(s);
        return;
    }
    for (let i=0; i<n; i++){
        if (!visit[i]){
            visit[i]=true;
            dfs(l+1,s+input[i]);
            visit[i]=false;
        }
    }
}
dfs(0,'')
console.log(uniqueSet.size);