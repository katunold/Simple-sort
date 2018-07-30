from simple_sort import simple_sort


def main():
    global run
    run = True
    while run:
        print("Please enter data or enter exit for Name to stop")
        name = input("Name : ")
        if name.lower() == "exit":
            run = False
            return
        age = input("Age : ")
        score = input("Score : ")
        print("-------------------- Data Submitted --------------------")
        print(simple_sort(name, age, score))
        print("--------------------------------------------------------")


if __name__ == "__main__":
    main()