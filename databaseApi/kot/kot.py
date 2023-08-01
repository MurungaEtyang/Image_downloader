import random
import time


class KitchenControl:
    __receipt_no = 0
    __time = ""
    __waiter = ""
    __table_no = 0
    __food_type = ""
    __quantity = ""

    def __init__(self, Receipt_no, Time, Waiter, Table_no, Food_type, Quantity):
        self.__receipt_no = Receipt_no
        self.__time = Time
        self.__waiter = Waiter
        self.__table_no = Table_no
        self.__food_type = Food_type
        self.__quantity = Quantity

    def print_food_type(self):
        card = f'receipt number ==> {str(self.__waiter)}{str(self.__receipt_no)}\ndate ==> {self.__time}\n' \
               f'waiter ==> {self.__waiter}\n' \
               f'table number ==> {self.__table_no}\nfood Quantity ==> {self.__quantity}kg\n' \
               f'food type ==> {self.__food_type}'

        return card


if __name__ == '__main__':
    receipt_no = random.randint(100, 1000)
    time = time.ctime()
    waiter = input("Enter name: ")
    table_no = int(input("Table number: "))
    food_type = input("Food type: ")
    quantity = input("Food quantity: ")

    kitchen = KitchenControl(receipt_no, time, waiter, table_no, food_type, quantity)
    print(kitchen.print_food_type())
