function solution(arr, k) {
    let answer = [];
    let s = [...new Set(arr)]
    if(s.length < k){
        let tmp = k-s.length
        for(let i=0;i<tmp;i++){
            s.push(-1)
        }
        answer = s
    } else {
       answer = s.slice(0,k) 
    }
    
    return answer;
}