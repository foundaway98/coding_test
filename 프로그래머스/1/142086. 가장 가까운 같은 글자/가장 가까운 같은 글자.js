function solution(s) {
    let answer = [];
    let word = []
    for(let i = 0; i<s.length; i++){
        if(word.lastIndexOf(s[i]) === -1 ){
            answer.push(-1);
            word.push(s[i])
        }
        
        else{
            answer.push(i - word.lastIndexOf(s[i]))
            word.push(s[i])
        }
    }
    return answer
}