function solution(M, N) {
    
    if(M===1){
        if(N===1){
            return 0
        } else {
            return N-1
        }
    } else {
        if(N===1){
            return M-1
        }else{
            return (M-1) + M * (N-1)
        }
    }
}