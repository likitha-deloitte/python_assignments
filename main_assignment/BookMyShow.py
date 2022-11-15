class Movie:

    def __init__(self, title, genre, length, cast, dire, aR, uR, lang, gap, capa, interval, noOfShows, firstShow):
        self.title = title
        self.genre = genre
        self.length = length
        self.lengthHour = length // 60
        self.lengthMin = length % 60
        self.cast = cast
        self.dire = dire
        self.aR = aR
        self.uR = uR
        self.lang = lang
        self.gap = gap
        self.capa = capa
        self.interval = interval
        self.noOfShows = noOfShows
        self.firstShow = firstShow
        self.seatsBooked = []
        self.time = []

    def printMovieforAdmin(self):
        print(f'Title: {self.title}')
        print(f'Genre: {self.genre}')
        print(f'Length: {self.lengthHour} hrs {self.lengthMin} mins')
        print(f'Cast: {self.cast}')
        print(f'Director: {self.dire}')
        print(f'Admin Rating: {self.aR}')
        print(f'Language: {self.lang}')
        print(f'Number of shows in a day: {self.noOfShows}')
        print(f'First Show: {self.firstShow}')
        print(f'Interval Time: {self.interval}')
        print(f'Gap Between Shows: {self.gap}')
        print(f'Capacity: {self.capa}')

    def printMovieForUser(self):
        print(f'Title: {self.title}')
        print(f'Genre: {self.genre}')
        print(f'Length: {self.lengthHour} hrs {self.lengthMin} mins')
        print(f'Cast: {self.cast}')
        print(f'Director: {self.dire}')
        print(f'Admin Rating: {self.aR}/10')
        print(f'Language: {self.lang}')
        print(f'Timing: ')
        self.printTimings()
        print(f'User Rating: {self.uR}/10')

class User:
    def __init__(self,name,age,phone,password,email):
        self.name = name
        self.age = age
        self.phone = phone
        self.password = password
        self.email = email


if __name__ == "__main__":
    usersDatabase = {}
    moviesDatabase = {}
    indexOfMovies = {}
    adminPassword = "12345678"
    while True:
        print('****** Welcome to BookMyShow ******')
        print('1.Login')
        print('2.Register New Account')
        print('3.Exit')
        userInput = (int)(input('Enter: '))

        if (userInput == 1):
            print('****** Welcome to BookMyShow ******')
            typeOfUser = input('User: ')
            password = input('Password: ')

            if(typeOfUser == "Admin"):
                if(password == adminPassword):

                    while True:
                        print(f'****** Welcome {typeOfUser} ******')
                        print('1.Add New Movie Info')
                        print('2.Edit Capacity of Movie Show')
                        print('3.Delete Movies')
                        print('4.Logout')
                        selectedInput = (int)(input('Enter: '))
                        if (selectedInput == 1):
                            title = (input('Title: '))
                            genre = (input('Genre: '))
                            length = (int)(input('Length: '))
                            cast = (input('Cast: '))
                            dire = (input('Director: '))
                            aR = (int)(input('Admin Rating: '))
                            lang = (input('Language: '))
                            nOS = (int)(input('Number of Shows in a day:'))
                            fS = (input('First Show (in 24-Hour Format):'))
                            interval = (int)(input('Interval Time: '))
                            gap = (int)(input('Gap Between Shows: '))
                            capa = (int)(input('Capacity: '))
                            movieObj = Movie(title, genre, length, cast, dire, aR, 0, lang, gap, capa, interval, nOS, fS)
                            moviesDatabase[title] = movieObj

                        elif (selectedInput == 2):
                            print('Select movie which you want to edit: ')
                            i = 1
                            for key in moviesDatabase:
                                indexOfMovies[i] = key
                                print(f'{i}.{key}')
                                i = i + 1
                            selectedIndex = (int)(input('Enter movie Index: '))
                            selectedMovie = indexOfMovies.get(selectedIndex)
                            moviesDatabase.get(selectedMovie).printMovieforAdmin()
                            number = (int)(input('Number of seats you want to increase: '))
                            moviesDatabase.get(selectedMovie).capa += number

                        elif (selectedInput == 3):
                            movieToBeDeleted = (input('Title of the movie to be deleted: '))
                            moviesDatabase.pop(movieToBeDeleted)
                        else:
                            break
                else:
                    print('Incorrect Password')

        elif (userInput == 3):
            break
        else:
            print('Wrong input . Try Again')

