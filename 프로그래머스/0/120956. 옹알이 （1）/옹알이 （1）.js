function solution(babbling) {
    var answer = 0;
    let can = ["aya", "ye", "woo", "ma"];
    
    for(let bab of babbling){
        let isAnswer = true
        
        if(bab.length > 10){
            continue
        } else {
            let babArr = bab.split("")
            while(babArr.length > 0){
                if(babArr.slice(0,2).join("") === "ye" || babArr.slice(0,2).join("") === "ma" ){
                    babArr.splice(0,2)
                } else if (babArr.slice(0,3).join("") === "aya" || babArr.slice(0,3).join("") === "woo") {
                    babArr.splice(0,3)
                } else {
                    isAnswer = false
                    break
                }
            }
            if (isAnswer){
                answer += 1
            } else if (!isAnswer){
                isAnswer = true
            }
        }
    }
    
    
    return answer;
}