class Stock:
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def __str__(self):
        return f"{self.name} ({self.percent}%)"