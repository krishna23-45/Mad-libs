
print("Life is like sunshine.\nLife is like rain.\nLife is like start.\nLife is like end.\n")
list_ = []
print("What do you think? How life is like? \n . Guess in reference of the above poem.")
print("Type q to exit the game.\n")
def main():
    while True:
        word = input(">>> ")
        if word == "q":
            break
        list_.append(word)

    for words in list_:
        print(f"life is a {words}")
        
main()

