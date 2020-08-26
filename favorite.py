import unittest

# This is our unit testing class called FruitSortTests. It inherits from one of unittest's classes, unittest.TestCase.

# There are 7 test cases below. One is functional which you can reference. I would like you to each develop the rest of the test cases. At least one of the test cases for compareFruits should test the raising of an exception by the application. Please also note that the last two test cases are for our variants method

#Please refer to https://docs.python.org/3/library/unittest.html for the assertion methods available to you, including any suitable for exception testing. Note that undeveloped tests are also being skipped with the @unittest.skip decorator. You will need to remove these as you develop the tests.

# Finally, please note that I have restructured the code such that it is either in our test class or the FavoriteFruit class. This requires me to specify methods by namespace/classname i.e. SortFruits.compareFruits.

class FruitSortTests(unittest.TestCase):

#Test1
  def test_compareFruits_1(self):
    self.assertEqual(SortFruits.compareFruits("orange", "apple", "oranges"), "orange")

#Test3
  def test_compareFruits_2(self):
    self.assertEqual(SortFruits.compareFruits("orange", "apple", "apples"), "apple")

#AttemptedTest3
  #def test_compareFruits_3(self):
  #  self.assertRaises(SortFruits.compareFruits("orange", "apple", "appleeees"), (TypeError, NameError, SyntaxError, IndentationError, ValueError))


  @unittest.skip("skipping")
  def test_compareFruits_7(self):
    self.assertEqual(True,True)

  @unittest.skip("skipping")
  def test_compareFruits_5(self):
    self.assertEqual(True,True)

  @unittest.skip("skipping")
  def test_variants_2(self):
    self.assertEqual(True,True)


class SortFruits():

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

    for fruit in SortFruits.variants(currentFruit):
      #print("Comparing " + userInput + " to " + fruit)
      if (fruit == userInput):
        userInput = currentFruit
        return userInput

    for fruit in SortFruits.variants(nextFruit):
      #print("Comparing " + userInput + " to " + fruit)
      if (fruit == userInput):
        userInput = nextFruit
        return userInput

    else:
      #print("Unable to match")
      raise Exception("WrongFruit!")
      #exit()


  def run():
    fruits = ['orange', 'acai', 'grape']
    fruits = [fruit.lower() for fruit in fruits]
    decided = False
    favorite = fruits[0] # we assume the first fruit as a favorite

    while (decided is False):
      for fruit in range(len(fruits)):

        # We want to make sure we don't exceed the length of the list!
        if (fruit < (len(fruits)-1)):

          while True:
            try:
              answer = input("Do you prefer " + favorite + " or "   +fruits[fruit+1] + "? ").lower()
              favorite = SortFruits.compareFruits(favorite, fruits[fruit+1],   answer)
              break
            except:
              print("Not a valid selection!")
              #exit()

        else:
          decided = True
          print("Those are all the choices! Your favorite is " +   favorite)


# __name__ is a built-in variable in Python. It is set by the interpreter when we run our code.
if __name__ == "__main__":
    unittest.main(exit=False) # this runs our tests
    SortFruits.run() # this runs our routine, which I have encapsulated in a "run" method.
