def convert_currency(amount, conversion_rate):
    return amount * conversion_rate

def main():
    print("Welcome to the Currency Converter!")
    print("Available currencies: ")
    print("1. USD to EUR (Rate: 0.85)")
    print("2. EUR to USD (Rate: 1.18)")
    
    try:
        choice = int(input("Select a conversion option (1 or 2): "))
        amount = float(input("Enter the amount to convert: "))
        
        if choice == 1:  # USD to EUR
            conversion_rate = 0.85
            converted_amount = convert_currency(amount, conversion_rate)
            print(f"{amount} USD is equal to {converted_amount:.2f} EUR.")
        elif choice == 2:  # EUR to USD
            conversion_rate = 1.18
            converted_amount = convert_currency(amount, conversion_rate)
            print(f"{amount} EUR is equal to {converted_amount:.2f} USD.")
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
