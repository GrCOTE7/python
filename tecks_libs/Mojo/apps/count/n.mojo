fn main():
    try:
        with open("apps/count/n.txt", "r") as file:
            var n = atol(file.read().strip()) + 1
            for i in range(1, n):
                if i < 4:
                    print(i, end=", ")
    except:
        print("Error: Could not read the file 'input.txt'")
