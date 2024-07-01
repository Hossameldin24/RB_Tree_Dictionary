from RedBlackTree import RB_Tree

class Dict:

    def __init__(self, filename):
            self.rb_tree = RB_Tree()

            with open(filename, 'r') as file:
                words = file.readlines()
            for word in words:
                self.rb_tree.insert(word.strip())                                                                                    
    
    def lookup_word(self, word):
           
            result = self.rb_tree.search(word)
            if result != self.rb_tree.NiL:
                print("YES")
            else:
                print("NO")

dictionary = Dict("dictionary.txt")

while True:
    option = input("Choose an option: \n 1 - Insert a word \n 2 - Look-up a word \n 3 - Quit \n Your Option: ")
    if (option == "1"):
        word = input("Emter a word: ")
        dictionary.rb_tree.insert(word)
        print("Successfully inputed")
    elif(option == "2"):
        word = input("Emter a word: ")
        dictionary.lookup_word(word)
    elif(option == "3"):
        break
    else:
         print("Invalid Option")