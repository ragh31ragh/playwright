try:
    with open("file223.txt", "r") as f:
        content = f.read()
        print(content)

except Exception as e:
    print(e)

finally:
    print("close db connection")