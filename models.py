from datetime import datetime

class Patient:

    def __init__(self, name):
        self.name = name
        self.time = datetime.now()

    def get_name(self):
        return self.name
 
 

    def get_time(self):
        return self.time
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self