

class StatusBar:

    def __init__(self, status_text):
        self.status_text = status_text
        self.status_text.set("")

    def listen(self, event):
        self.status_text.set(event)

        
