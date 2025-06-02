
# <---------------------------------------------------------------Greeting and Main Menu------------------------------------------------------------->

print("Hello, Welcome to your Personal Assistant!")
name = input("What's your name? \n").strip().title()

# Greeting the user
def greeting():
    print (f"Nice to meet you, {name}! ")
    print("I'm here to help you with calculations and text formatting.")
    print("What would you like to do today?\n\n")

# Main Menu   
def main_menu():
    print("    📋Main menu:\n 1. 🧮 Calculator Suite\n 2. 📝 Text Formatter\n 3. 👋 Exit")
    option = input("Choose an option (1-3): \n")
    if option == "1":
        print(f"Great choice, {name}, Let's do some calculations!")
        calculator_options()
    elif option == "2":
        text_options()
    elif option == "3":
        print(f"👋 Thank you for using your Personal Assistant, {name}!")
        print("Have a wonderful day! 🌟")
        print("See you next time! 🚀")
        return
    else:
        print(f"❌ Oops! Please enter 1, 2, or 3, {name}.")
        return
    


 # <-------------------------------------------------------------- Calculator Section ---------------------------------------------------------------------->

# Allows the user to choose the calculator type
def calculator_options():
    print("🧮 CALCULATOR SUITE")
    print(f"Hi, {name}! Choose your calculator:")
    print("1. 💰 Tip Calculator")
    print("2. 🎂 Age Calculator")
    print("3. ⚡ Energy Calculator (E=mc²)")
    print("4. 💳 Budget Helper")
    print("5. 🔙 Back to Main Menu")
    option = input("What would you like to use? (1-5) \n")
    if option == "1":
        tip_calculator()
    elif option == "2":
        age_calculator()
    elif option == "3":
        energy_calculator()
    elif option == "4":
        budget_helper()
    elif option == "5":
        main_menu()
    else:
        print(f"❌ Oops! Please enter 1, 2, 3, 4 or 5, {name}.")
        return



# Tip Calculator

def tip_calculator():
    print("💰 Tip Calculator Selected!\n")

    dollars_input = input("What's your bill amount? $ \n")
    if not dollars_input.replace('.', '', 1).isdigit():
        print(f"❌ Oops! Please enter a valid number, {name}.")
        return  

    percent_input = input("What percentage would you like to tip? (15, 18, 20, or custom): ")
    if not percent_input.replace('.', '', 1).isdigit():
        print(f"❌ Oops! Please enter a valid number, {name}.")
        return

    dollars = float(dollars_input)
    percent = float(percent_input)

    tip = dollars * percent / 100
    total = dollars + tip

    print(f"📊 Bill: ${dollars:.2f}")
    print(f"📊 Tip({int(percent)}%): ${tip:.2f}")
    print(f"📊 Total: ${total:.2f}")
    print(f"\nThanks for using the tip calculator, {name}!\n")
    main_menu()
    
# Age Calculator

def age_calculator():
    print("🎂 Age Calculator Selected!\n")

    year_born_input = input("What year were you born?\n")
    if not year_born_input.isdigit():
        print(f"❌ Oops! Please enter a valid year, {name}.")
        return

    year_for_age_input = input("What year do you want to know your age for?\n")
    if not year_for_age_input.isdigit():
        print(f"❌ Oops! Please enter a valid year, {name}.")
        return

    year_born = int(year_born_input)
    year_for_age = int(year_for_age_input)

    print(f"🎉 In {year_for_age} you will be {year_for_age - year_born} years old!\nTime flies, {name}! 🚀")
    print()
    main_menu()
    

# Energy Calculator

def energy_calculator():
    print("⚡ Energy Calculator (E=mc²) Selected!\n")

    mass_input = input("Enter mass in kilograms:\n")
    if not mass_input.isdigit():
        print(f"❌ Oops! Please enter a valid number, {name}.")
        return

    m = int(mass_input)
    E = m * 300_000_000 * 300_000_000

    print("🧮 Calculating energy using E=mc²...")
    print(f"⚡ Energy released: {E:,} Joules")
    print(f"That's enough to power a city for months, {name}! 🏙️\n\n")
    main_menu()



# Budget Helper

def budget_helper():
    print("💳 Budget Helper Selected!")

    income_input = input("What's your monthly income? $\n")
    if not income_input.isdigit():
        print(f"❌ Oops! Please enter a valid number, {name}.")
        return

    percentage_input = input("What percentage do you want to save?\n")
    if not percentage_input.isdigit():
        print(f"❌ Oops! Please enter a valid number, {name}.")
        return

    income = int(income_input)
    percentage = int(percentage_input)

    savings = income * percentage / 100
    spending_money = income - savings

    print(f"💰 Monthly Income: ${income:,}")
    print(f"💰 Savings({percentage}%): ${savings:,}")
    print(f"💰 Spending Money: ${spending_money:,}")
    print(f"Great financial planning, {name}! 📈\n\n")
    main_menu()

# < ------------------------------------------------------------ Text Section ---------------------------------------------------------->

# Allows the user to choose text formatter

def text_options():
    print("📝 TEXT FORMATTER SUITE")
    print(f"Hey {name}! Choose your text tool:")
    print("1. 🔇 Indoor Voice (Fix SHOUTING)")
    print("2. ⚡ Speed Reader")
    print("3. 😊 Emoji Replacer")
    print("4. ✨ Name Formatter")
    print("5. 🔙 Back to Main Menu")
    text = input("What would you like to use? (1-5):\n")
    if text == "1":
        indoor_voice()
    elif text == "2":
        speed_reader()
    elif text == "3":
        emoji_replacer()
    elif text == "4":
        name_formatter()
    elif text == "5":
        main_menu()
    else: 
        print(f"❌ Oops! Please enter 1, 2, 3, 4 or 5, {name}.")
        return 


# Indoor Voice

def indoor_voice():
    print("🔇 Indoor Voice Selected!")
    enter_text = input("Enter the SHOUTING text you want to fix:\n").lower().strip()
    print(f"✨ Fixed text: {enter_text}")
    print(f"Much better, {name}! No more shouting! 🤫\n\n")
    main_menu()


# Speed Reader

def speed_reader():
    print("⚡ Speed Reader Selected!")
    speed = input("Enter text to make speed-readable:\n").replace(" ", "...").strip()
    print(f"speed_text: {speed}")
    print(f"Perfect for speed reading, {name}! 🏃‍♀️ \n\n")
    main_menu()


# Emoji Replacer

def emoji_replacer():
    print("😊 Emoji Replacer Selected!")
    text = input("Enter text with :) or :( to convert:\n").replace(":)", "😊").replace(":(", "😢")
    print(f"😊 Emoji text: {text}")
    print(f"Much more expressive, {name}! ✨ \n\n")
    main_menu()

# Name Formatter

def name_formatter():
    print("✨ Name Formatter Selected!")
    user_name = input("Enter a name to format properly:\n").title().strip()
    print(f"✨ Formatted name: {user_name}")
    print(f"Perfectly formatted, {name}! 👨‍💼\n\n")
    main_menu()



greeting()
main_menu()