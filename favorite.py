fruits = ['apple', 'banana', 'orange']
fruits = [fruit.lower() for fruit in fruits] 

decided = False
favorite = fruits[0] # we assume the first fruit as a favorite

while (decided is False):
  for fruit in range(len(fruits)):
    # debugging statement
    #print ("Iteration: " + str(fruit))
      
    # We want to make sure we don't exceed the length of the list!
    if (fruit < (len(fruits)-1)):
      
      #favorite = input("Do you prefer " + fruits[fruit] + " or " +fruits[fruit+1] + "? ")
      
      favorite = input("Do you prefer " + favorite + " or " +fruits[fruit+1] + "? ")
    else:
      decided = True
      print("Those are all the choices! Your favorite is " + favorite)        
