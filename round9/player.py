class Player:
    def __init__(self,new_name):
        self.__name = new_name
        self.__no_of_games =0
        self.__total=0
        self.__record =0
    # return the list of attributes
    # return name of the player
    def get_name(self):
        return self.__name
    #return the number of games the player plays
    def get_no_of_games(self):
        return self.__no_of_games
    #return the players high score
    def get_record(self):
        return self.__record
    # adds a game's result to the player
    def add_game(self,points):
        if(points >=0):
            self.__no_of_games += 1
            self.__total += points
            if (self.__record <points):
                self.__record = points
    def average (self):
        if(self.__no_of_games>0):
            average = self.__total/self.__no_of_games
        else:
            average = 0.0
        return average        
    def is_master(self):
        #player has to score atleast 3000 and average 2000
        average_reco = self.average()
        if(self.__record >= 3000 and average_reco >= 2000):
            return True
        else:
            return False        
    def is_better(self, another_player):
        if(self.__record > another_player.get_record()):
            return True
        else:
            return False         
    def __str__(self):
        if(self.is_master()):
            str1 = self.__name + ", number of games " + str(self.__no_of_games) + \
               ", record " + str(self.__record) + \
               " points, MASTER."
        else:
            str1 = self.__name + ", number of games " + str(self.__no_of_games) + \
               ", record " + str(self.__record) + \
               " points, has not achieved master title."

        return str1
        