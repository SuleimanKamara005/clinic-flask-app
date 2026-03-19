from datetime import datetime

class Patient:

    def __init__(self, name):
        self.name = name
        self.time = datetime.now()



    # update

    def get_name(self):
        return self.name
    # update
    def get_time(self):
        return self.time
    def __init__(self, name):
        self.name = name
    # update
    def get_name(self):
        return self