def main():
    ip = input("inserire l'ip: ")
    groups = ip.split(".") #slit di stringhe
    groups = [int(groups) for group in groups]
    print(groups)

if __name__ == "__main__":
    main()