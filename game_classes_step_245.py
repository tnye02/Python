

class Board_game:   #declare parent board game class
    title = '<<Game Title>>'    #declare title variable
    genre = '<<Game Genre>>'    #declare genre variable
    game_type = 'Casual'
    publisher  = '<<Game Publisher>>'   #Publisher variable
    rec_age = 'Fun for all ages'        #recommended age

    def getTitle(self):
        title = input("\nPlease enter the title of the game: ")

class Hobby_Game(Board_game): #declare more specific board game sub-type
    game_type = '<<Thematic/Euro/War/Other>>' #major types of Hobby games
    no_of_expansions = '0'  #set number of expansions available

    def getTitle(self):
        title = input("\nPlease enter the title of the game: ")
        game_type = input("\nPlease enter the type of game: ")
        print("\n{} is a {} type game".format(title, game_type))


class Mainstream(Board_game):   #another more specific board game type
    pub_date = 1900             #set publishing date
    best_seller = True          #set best seller status

    def getTitle(self):
        title = input("\nPlease enter the title of the game: ")
        pub_date = input("\nPlease enter the year this game was published: ")
        print("\n{} was published in {}.".format(title, pub_date))
    
if __name__ == "__main__":
    game = Mainstream()
    mainstream = game.getTitle()
    
    
