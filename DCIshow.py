class DCIshow:
    def __init__(self, corps, year, showname,  placement, audio):
        self.corps = corps
        self.year = year
        self.title = showname
        self.placement = placement
        self.path = "C:\\Users\\Tyler\\Projects\\DCI_quiz\\DCI_Audio\\" + audio

    def __str__(self):
        return f"{self.corps} {self.year}, {self.title} placed {self.placement} in finals with a score of {self.score:.3f}"
    
    def __gt__(self, other):
        if self.score > other.score:
            return True
        return False
    
    def get_path(self):
        return self.path
    
    def get_corps(self):
        return self.corps
    
    def get_year(self):
        return self.year
    
    def get_title(self):
        return self.title
    
    def get_placement(self):
        return self.placement


    