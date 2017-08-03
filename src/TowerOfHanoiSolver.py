class Tower:
    __slots__ = 'rings', 'capacity'

    def __init__(self, cap: int):
        self.rings = list()
        self.capacity = cap

    def add(self, ring_size:int):
        if len(self.rings) >= self.capacity:
            raise IndexError('Tower already at max capacity')
        self.rings.append(ring_size)

    def pop(self) -> int:
        if len(self.rings) <= 0:
            raise IndexError('Tower empty')
        return self.rings.pop()

    def get(self, depth: int) -> int:
        return self.rings[-1 * (depth + 1)]


def print_towers(towers: list, size=None):
    if size is None:
        size = towers[0].capacity

    # Pad tower lists with zeros
    tower_list = list()
    for tower in towers:
        tl = list(tower.rings)
        while len(tl) < size:
            tl.append(0)
        tower_list.append(tl)

    for row in range(size):
        for tower in tower_list:
            ring_size = tower[size - row - 1]
            whitespace = padding(size - ring_size + 1)
            ring_space = padding(ring_size, '-')
            print(whitespace + ring_space + '|' + ring_space + whitespace, end=' ')
        print()

    for idx in range(len(tower_list)):
        base = padding((size + 1), character='=')
        print("%s%d%s" % (base, idx + 1, base), end=' ')

    print("\n")


def padding(width: int, character=' ') -> str:
    pad = ''
    for i in range(width):
        pad += character

    return pad


def move_tower(towers: list, size: int, src: int, dest: int):
    if size == 1:
        towers[dest].add(towers[src].pop())
        print("\nTower %d -> Tower %d" % (src + 1, dest + 1))
        print_towers(towers)
    else:
        # Determine temp peg
        all_pegs = list(range(3))
        all_pegs.remove(src)
        all_pegs.remove(dest)
        temp_peg = all_pegs[0]

        # Move top tower (size n-1) to temp peg
        move_tower(towers, size-1, src, temp_peg)

        # Move bottom ring to destination peg
        move_tower(towers, 1, src, dest)

        # Move rest of tower to destination peg
        move_tower(towers, size-1, temp_peg, dest)


def main():
    size = int(input("Input tower size... "))
    towers = list()

    for i in range(3):
        towers.append(Tower(size))
    for ring in range(size, 0, -1):
        towers[0].add(ring)

    print("\nInitial configuration")
    print_towers(towers)
    move_tower(towers, size, 0, 1)

if __name__ == '__main__':
    main()
