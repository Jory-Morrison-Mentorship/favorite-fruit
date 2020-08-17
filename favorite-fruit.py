#List of Fruits
fruits = ['Gooseberries', 'Grapes', 'Oranges', 'Tomatoes', 'Raspberries', 'Strawberries', 'Kiwis', 'Mangoes']
fruits = [fruit.lower() for fruit in fruits]

#Variables
decided = False
favorite = fruits[0]
suffix1 = "s"
suffix2 = "ies"
suffix3 = "es"
suffix4 = "y"
suffix5 = "o"

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
                if (favorite.endswith(suffix4) is True):
                        print("path1")
                        favorite = favorite.replace(suffix4, suffix2)
                if (favorite.endswith(suffix5) is True):
                        print("path2")
                        favorite = favorite.replace(favorite, favorite + suffix3)
                if (favorite.endswith(suffix2) is False):
                        print("path3")
                        favorite = favorite.replace(favorite, favorite + suffix1)

#Sets decided equal to the returned value, which is "decided?"
decided = processes(favorite)

#While Loops that determines if the function runs or not
while (decided is False):
        processes(favorite)
while (decided is True):
        break
