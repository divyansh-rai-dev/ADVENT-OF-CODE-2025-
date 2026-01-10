class Microwave:

    product = "Microwave"

    def __init__(self , color , year , model , price):
        self.color = color 
        self.year = year
        self.model = model
        self.price = price


gooergae = Microwave("red" , 2024 , "xyz" , 2000)

lg = Microwave("blue" , 2023 , "abs" , 1999)

print(f"welcome to microwave section we have {gooergae.color} gooergae of year {gooergae.year} and its model is {gooergae.model}")

print(f"welcome to microwave section we have {lg.color} {"lg"} of year {lg.year} and its model is {lg.model}")
