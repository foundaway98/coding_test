function solution(board) {
    const n = board.length
    let answer = 0
    const dirs = [[-1,-1], [-1,0], [-1, 1], [0,-1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for(let i = 0; i<n; i++){
        for(let j = 0; j<n;j++){
            if (board[i][j] === 1){
                for(let dir of dirs){
                    if(i+dir[0] < 0 || i + dir[0] >= n || j + dir[1] < 0 || j + dir[1] >= n){
                        continue
                    } else {
                        if(board[i+dir[0]][j+dir[1]] === 1){
                            continue
                        } else {
                            board[i+dir[0]][j+dir[1]] = 2
                        }
                    }
                }
            }
        }
    }
    for(let i = 0; i<n;i++){
        for(let j = 0; j<n ; j++){
            if(board[i][j] === 0){
                answer += 1
            }
        }
    }
    return answer;
}