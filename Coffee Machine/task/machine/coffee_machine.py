class CoffeeMachine:

    def __init__(self):
        self.stock_money = 550
        self.stock_water = 400
        self.stock_milk = 540
        self.stock_coffee_beans = 120
        self.stock_cups = 9



    def stock_info(self):
        print("The coffee machine has:")
        print(f"{self.stock_water} of water")
        print(f"{self.stock_milk} of milk")
        print(f"{self.stock_coffee_beans} of coffee beans")
        print(f"{self.stock_cups} of disposable cups")
        print(f"{self.stock_money} of money")



    def machine_process(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            user_input = input()
            if user_input == "buy":
                self.buy_coffee()
            elif user_input == "fill":
                self.machine_fill()
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.stock_info()
            elif user_input == "exit":
                break


    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type == "1":
            if self.stock_water < 250:
                print("Sorry, not enough water!")
            elif self.stock_coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.stock_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.stock_water -= 250
                self.stock_coffee_beans -= 16
                self.stock_cups -= 1
                self.stock_money += 4
        elif coffee_type == "2":
            if self.stock_water < 350:
                print("Sorry, not enough water!")
            elif self.stock_milk < 75:
                print("Sorry, not enough milk!")
            elif self.stock_coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.stock_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.stock_water -= 350
                self.stock_milk -= 75
                self.stock_coffee_beans -= 20
                self.stock_cups -= 1
                self.stock_money += 7
        elif coffee_type == "3":
            if self.stock_water < 200:
                print("Sorry, not enough water!")
            elif self.stock_milk < 100:
                print("Sorry, not enough milk!")
            elif self.stock_coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.stock_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.stock_water -= 200
                self.stock_milk -= 100
                self.stock_coffee_beans -= 12
                self.stock_cups -= 1
                self.stock_money += 6
        elif coffee_type == "back":
            return


    def machine_fill(self):
        print("Write how many ml of water do you want to add:")
        water_fill = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_fill = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        bean_fill = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cup_fill = int(input())
        self.stock_water += water_fill
        self.stock_milk += milk_fill
        self.stock_coffee_beans += bean_fill
        self.stock_cups += cup_fill

    def take_money(self):
        print(f"I gave you ${self.stock_money}")
        self.stock_money -= self.stock_money


test_machine = CoffeeMachine()

test_machine.machine_process()
