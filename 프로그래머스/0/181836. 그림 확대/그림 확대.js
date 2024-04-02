function solution(picture, k) {
    var answer = [];
    for(let p of picture){
        let tmp = ""
        for(let pix of p){
            for(let i = 0;i<k;i++){
                tmp+=pix
            }
        }
        for(let i=0;i<k;i++){
            answer.push(tmp)    
        }
    }
    
    return answer;
}