function solution(keyinput, board) {
    var answer = [];
    const keyMap = {"left":[-1,0], "right":[1,0], "up": [0,1], "down": [0,-1]}
    const boardLeftMax = (board[0]-1)/2
    const boardRightMax = (board[1]-1)/2
    let player = [0,0]
    for(let direction of keyinput){
        if(Math.abs(keyMap[direction][0] + player[0]) > boardLeftMax || Math.abs(keyMap[direction][1] + player[1]) > boardRightMax){
            continue
        } else {
            player[0] += keyMap[direction][0]
            player[1] += keyMap[direction][1]
        }
    }
    return player;
}