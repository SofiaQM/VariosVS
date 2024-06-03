
while True:
    try:
        bricks = int(input("Height: "))
        if 1 <= bricks <= 8:
            for i in range(0, bricks, 1):
                # it creates a sequence of numbers from bricks - 1 down to i (exclusive), decrementing by 1 each time.
                for j in range(bricks - 1, i, -1):
                    print(" ", end="")
                for k in range(0, i+1, 1):
                    print("#", end="")
                print()
            break
    except ValueError:
        print("Invalid input. Please enter a number between 2 and 8.")


