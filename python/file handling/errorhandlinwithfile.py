try:
    with open("file.txt","r")as file:
        r=file.read()
        print(r)
except FileNotFoundError:
    print("file not found ")
finally:
    print("process done")