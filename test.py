# def solution(board, h, w):
#     answer = 0
#     n = len(board)
#     count = 0
#     dh = [0,1,-1,0]
#     dw = [1,0,0,-1]

#     for i in range(4):
#         h_check = h+dh[i]
#         w_check = w+dw[i]
#         if 0 <= h_check < n and 0 <= w_check < n:
#             if board[h][w] == board[h_check][w_check]:
#                 count += 1

#     return count
# a = [
#     ["blue", "red","orange", "red"],
#     ["red","red","blue","orange"],
#     ["blue","orange","red","red"],
#     ["orange","orange","red","blue"]
# ]

# print(solution(a, 1, 1))


def solution(data, ext, val_ext, sort_by):
    answer = []
    sel = ["code", "date", "max", "remain"]
    a = len(data)
    for i in range(4):
        if sel[i] == ext:
            for j in range(a):
                if data[j][i] < val_ext:
                    answer.append(data[j])
    b = len(answer)               
    for k in range(4):
        if sel[k] == sort_by:
            answer = sorted(answer, key = lambda x:x[k])
            # for l in range(b - 1):
            #     for u in range(b-l):
            #         if answer[l][k] < answer[l+1][k]:
            #             c = answer[l]
            #             answer[l] = answer[l+1]
            #             answer[l+1] = c
    
    return answer

b = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401,  10, 8]]

print(solution(b,"date", 20300501, "max"))