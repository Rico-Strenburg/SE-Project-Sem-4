from datetime import datetime

class Strategy:
    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc
        self.modified = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    