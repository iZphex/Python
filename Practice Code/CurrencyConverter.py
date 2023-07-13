def main():
    print("This is a currency converter for USD to Pounds")
    print()
    dollars = eval(input("Enter amount in USD: "))
    pounds = convert_to_pounds(dollars)
    print("That is", pounds, "Pounds")


convert_to_pounds = lambda dollars: dollars * 0.82

main()
