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


def next_moves(current, came_from, steps, max_steps, min_steps):
    if 0 < steps < min_steps:
        return [(add(current, came_from), came_from, steps + 1)]

    moves = list()
    for direction in MOVES[came_from]:
        next_steps = steps
        if direction == came_from:
            if steps == max_steps:
                continue
            next_steps += 1
        else:
            next_steps = 1
        node = add(current, direction)
        if in_grid(node, Lx, Ly):
            moves.append((node, direction, next_steps))

    return moves


def get_cost(x, y, heatmap):
    return int(heatmap[y][x])


def least_heat_loss(heatmap, max_steps, min_steps, Lx, Ly):
    start, steps, cost = (0, 0), 0, 0
    init_state = start, start, steps
    nodes_cost = {init_state: cost}
    frontier = []
    heappush(frontier, (cost, init_state))
    while frontier:
        cost, state = heappop(frontier)
        current, came_from, steps = state

        if current == (Lx, Ly) and steps >= min_steps:
            break

        for node, move, node_steps in next_moves(current, came_from, steps, max_steps, min_steps):
            if not in_grid(node, Lx, Ly):
                continue
            node_cost = get_cost(*node, heatmap) + cost
            node_state = (node, move, node_steps)
            if (node_state not in nodes_cost) or node_cost < nodes_cost[node_state]:
                nodes_cost[node_state] = node_cost
                state = (node_cost, node_state)
                heappush(frontier, state)
    return cost


with open("data") as f:
    heatmap = f.read().splitlines()
Lx = len(heatmap[0]) - 1
Ly = len(heatmap) - 1


# ==== PART 1 ====
print(least_heat_loss(heatmap, 3, 1, Lx, Ly))

# ==== PART 2 ====
print(least_heat_loss(heatmap, 10, 4, Lx, Ly))
