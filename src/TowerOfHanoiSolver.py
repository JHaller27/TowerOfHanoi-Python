def move_tower(size:int, src_peg:int, dest_peg:int):
    if size == 1:
        print("  Peg %d -> Peg %d" % (src_peg, dest_peg))
    else:
        # Determine temp peg
        all_pegs = list(range(1,4))
        all_pegs.remove(src_peg)
        all_pegs.remove(dest_peg)
        temp_peg = all_pegs[0]

        # Move top tower (size n-1) to temp peg
        move_tower(size-1, src_peg, temp_peg)

        # Move bottom ring to destination peg
        move_tower(1, src_peg, dest_peg)

        # Move rest of tower to destination peg
        move_tower(size-1, temp_peg, dest_peg)


def main():
    size = int(input("Input tower size... "))
    print("Steps to solve...")
    move_tower(size, 1, 2)

if __name__ == '__main__':
    main()
