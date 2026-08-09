def main():
    print ("Hello World")
    number = int(input("Enter a the range of the multiplication table (e.g., 5 for a 5x5 table): "))
    print (f"Multiplication Table up to {number}x{number}:")

    print("        ", end="")
    for i in range (1, number + 1):
        print (f"{i}\t", end = "")
    print()
    for i in range (1, number + 1):
        print (f"{i} | \t", end = "")
        for j in range (1, number + 1):
            print (f"{i * j}\t", end = "")
        print()


if __name__ == "__main__":
    main()