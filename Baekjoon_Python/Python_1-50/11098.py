N = int(input())
for i in range(N):
    P = int(input())
    player_list = {}
    check = []
    for j in range(P):
        player_cost, player_name = input().split()
        player_cost = int(player_cost)
        player_list[player_cost] = player_name
    for k in player_list.keys():
        check.append(k)
    check.sort(reverse=True)
    print(player_list.get(check[0]))