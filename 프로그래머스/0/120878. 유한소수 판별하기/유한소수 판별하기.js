function solution(a, b) {
    
    //기약분수 만들기
    for(let i = b;i>1; i--){
        if(a%i === 0 && b%i ===0){
            a = a/i
            b = b/i
        }
    }
    //분모 소인수 파악
    while(b % 2 === 0 || b % 5 === 0){
        if(b % 2 === 0){
            b = b/2
        } else if(b % 5 === 0){
            b = b/5
        }
    }
    
    if(b === 1){
        return 1
    } else {
        return 2
    }
}