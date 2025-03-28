class MenuItem:
    name: str
    description: str
    vegetarian: bool
    price: float

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description
    
    def get_price(self) -> float:
        return self.price
    
    def is_vegetarian(self) -> bool:
        return self.vegetarian
