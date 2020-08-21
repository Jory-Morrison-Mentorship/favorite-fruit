fruits = ['orange', 'acai', 'grape']
fruits = [fruit.lower() for fruit in fruits] 


def variants(myFruit):
  pluralfruits = []
  pluralfruits.append(myFruit[:-1] + "ies")
  pluralfruits.append(myFruit + "s")
  pluralfruits.append(myFruit + "es")
  pluralfruits.append(myFruit[:-3] + "y")
  pluralfruits.append(myFruit[:-1])
  pluralfruits.append(myFruit[:-2])
  return(pluralfruits)

def compareFruits(currentFruit, nextFruit, userInput):
  #print("The input provided was: " + userInput)
  #print("Comparing " + userInput + " to " + currentFruit)
  if (userInput == currentFruit):
    return currentFruit
  
  #print("Comparing " + userInput + " to " + nextFruit)
  if (userInput == nextFruit):
    return nextFruit

  for fruit in variants(currentFruit):
    #print("Comparing " + userInput + " to " + fruit)
    if (fruit == userInput):
      userInput = currentFruit
      return userInput

  for fruit in variants(nextFruit):
    #print("Comparing " + userInput + " to " + fruit)
    if (fruit == userInput):
      userInput = nextFruit
      return userInput

  else:
    #print("Unable to match")
    raise Exception("WrongFruit!")
    #exit()
    

decided = False
favorite = fruits[0] # we assume the first fruit as a favorite

while (decided is False):
  for fruit in range(len(fruits)):
      
    # We want to make sure we don't exceed the length of the list!
    if (fruit < (len(fruits)-1)):

      while True:
        try:
          answer = input("Do you prefer " + favorite + " or " +fruits[fruit+1] + "? ").lower()
          favorite = compareFruits(favorite, fruits[fruit+1], answer)
          break
        except:
          print("Not a valid selection!")
          #exit()

    else:
      decided = True
      print("Those are all the choices! Your favorite is " + favorite)
