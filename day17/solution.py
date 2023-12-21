from heapq import heappush, heappop

N, E, S, W = (0, -1), (1, 0), (0, 1), (-1, 0)
MOVES = {
    (0, 0): [E, S],
    N: [N, E, W],
    E: [N, E, S],
    S: [E, S, W],
    W: [N, S, W]
}


def add(p, q):
    x, y = p
    a, b, = q
    return x + a, y + b


def in_grid(p, Lx, Ly):
    x, y = p
    return True if 0 <= x <= Lx and 0 <= y <= Ly else False


def next_moves(current, go_to, fuel, Lx, Ly):
    moves = list()
    for direction in MOVES[go_to]:
        move_fuel = fuel
        if direction == go_to:
            if fuel == 0:
                continue
            move_fuel -= 1
        else:
            move_fuel = 2
        node = add(current, direction)
        if in_grid(node, Lx, Ly):
            moves.append((node, direction, move_fuel))
    return moves


def get_cost(x, y, heatmap):
    return int(heatmap[y][x])


def least_heat_loss(heatmap, Lx, Ly):
    start, fuel, cost = (0, 0), 3, 0
    init_state = start, start, fuel
    nodes_cost = {init_state: cost}
    frontier = []
    heappush(frontier, (cost, init_state))
    while frontier:
        cost, state = heappop(frontier)
        current, go_to, fuel = state

        if current == (Lx, Ly):
            return cost

        for node, move, node_fuel in next_moves(current, go_to, fuel, Lx, Ly):
            node_cost = get_cost(*node, heatmap) + cost
            node_state = (node, move, node_fuel)
            if (node_state not in nodes_cost) or node_cost < nodes_cost[node_state]:
                nodes_cost[node_state] = node_cost
                state = (node_cost, node_state)
                heappush(frontier, state)


with open("data") as f:
    heatmap = f.read().splitlines()
Lx = len(heatmap[0]) - 1
Ly = len(heatmap) - 1


# ==== PART 1 ====
print(least_heat_loss(heatmap, Lx, Ly))
