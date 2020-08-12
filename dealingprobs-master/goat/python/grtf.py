def eval(n, solutions, triad, tiles):
    if n == 9:
        if (min(triad[:3]) == (min(triad[3:6]) + min(triad[6:]))/2 and
            max(triad[6:]) == max(triad[:3]) + max(triad[3:6])):
            if sum(triad[:3]) not in solutions:
                print(triad)
                solutions.append(sum(triad[:3]))
            return
    else:
        for tile in list(tiles):
            triad[n] = tile
            if n == 3:
                if min(triad[:3]) <= 3 or min(triad[:3]) >= 5:
                    # enhances speed by escaping impossible permutations
                    continue
            tiles.remove(tile)
            eval(n+1, solutions, triad, tiles)
            tiles.add(tile)
    return solutions

print(eval(0, [], list(range(0, 9)), set(range(1, 10))))