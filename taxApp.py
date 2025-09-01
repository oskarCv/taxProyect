
def get_user_input():
    while True:
        try:
            year = int(input("Enter the year: "))
            break
        except ValueError:
            print("Invalid year. Please enter a valid year (valid year could be 2025).")
        
    while True:
        try:
            month = int(input("Enter the month: "))
            break
        except ValueError:
            print("Invalid month. Please enter a valid month (valid month could be 01).")
            
    return year, month

def main():
    print("This app will help on the data processing for the tax declaration")
    # get the user input
    year, month = get_user_input()
    print(f"Starting data procesing for Year: {year}, Month: {month}")
    

if __name__ == "__main__":
    main()