def main():
    feet = int(input("Enter feet amount: "))
    inch = int(input("Enter inch amount: "))
    totalinches = feet * 12 + inch
    centimeters = totalinches * 2.54
    print("input amount eguals to " + str(centimeters) + " centimeters")


if "__name__" == "__main__":
    main()
