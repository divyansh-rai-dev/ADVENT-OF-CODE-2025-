class car:

    def __init__(self , model , year , color , for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def start(self):
        print(f"You drive a {self.model}")

    def stop(self):
        print(f"You fucked a {self.model} {self.color}")