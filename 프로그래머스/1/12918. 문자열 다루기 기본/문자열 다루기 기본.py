def solution(s):
    try:
        answer = int(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except ValueError:
        return False
    