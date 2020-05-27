from datetime import date
#ask user for birthday
# print cake with number of candles being 1st digit

cake1 =     "   |:H:a:p:p:y:|"
cake2 =     " __|___________|__"
cake3 =     "|^^^^^^^^^^^^^^^^^|"
cake4 =     "|:B:i:r:t:h:d:a:y:|"
cake5 =     "|                 |"
cake6 =     "~~~~~~~~~~~~~~~~~~~"


def user_birthday():
    birthday = input("When is your birthday? (DD/MM/YYYY)? ")
    calculate_age(birthday)
    return birthday

def calculate_age(bd):
    today = date.today()
    bd_day, bd_month, bd_year = bd.split("/")
    had_birthday_already = ((today.month, today.day) > (int(bd_month), int(bd_day)))
    if(had_birthday_already):
        age = (today.year - int(bd_year))
    else:
        age = (today.year - int(bd_year) - 1)
    set_candles(age)
    return age
def set_candles(age):
    candles = age % 10
    center_candles = (10 - candles) // 2
    cake_topper = "    " + center_candles * "_" + candles * "i" + center_candles *  "_"
    if(len(cake_topper) < 10):                 #if "candles" is odd this evens it
        cake_topper = cake_topper + "_"
    bake_cake(cake_topper)
    return cake_topper
def bake_cake(top):
   print(top)
   print(cake1)
   print(cake2)
   print(cake3)
   print(cake4)
   print(cake5)
   print(cake6)


user_birthday()