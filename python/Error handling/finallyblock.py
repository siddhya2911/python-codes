try:
    file=open("data.txt")
except FileNotFoundError:
    print("file not found")
finally:
    print("closing resource")