with open("ww.jpg", "rb") as src:
    with open("python.jpg", "wb") as dest:
        dest.write(src.read())
