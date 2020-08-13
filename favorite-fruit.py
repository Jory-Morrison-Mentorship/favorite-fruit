#List of Fruits
fruits = ['Gooseberries', 'Grapes', 'Oranges', 'Tomatoes', 'Raspberries', 'Strawberries', 'Kiwis', 'Mangoes']
fruits = [fruit.lower() for fruit in fruits]

#Variables
decided = False
favorite = fruits[0]
suffixes = ["s", "ies", "es", "y", "o"]

#Function that asks questions and allows input. It figures out your favorite fruit
def processes(favorite):
        for fruit in range(len(fruits)):

                #Asks the question if the list hasn't been completely covered
                if (fruit < len(fruits)-1):
                        favorite = str(input("Do you prefer " + favorite + " or " + fruits[fruit+1] + "?"))
                #Reveals your favorite fruit if the list has been completely covered
                else:
                        decided = True
                        print("Those are all the choices! Your favorite fruit is " + favorite)
                        return decided

                #Code that makes plurality irrelevant
                if (favorite.endswith(suffixes[3]) is True):
                        print("path1")
                        favorite = favorite[:-1] + suffixes[1]
                if (favorite.endswith(suffixes[4]) is True):
                        print("path2")
                        favorite = favorite.replace(favorite, favorite + suffixes[2])
                if (favorite.endswith(suffixes[0]) is False):
                        print("path3")
                        favorite = favorite.replace(favorite, favorite + suffixes[0])

#Sets decided equal to the returned value, which is "decided?"
decided = processes(favorite)

#While Loops that determines if the function runs or not
while (decided is False):
        processes(favorite)
while (decided is True):
        break
