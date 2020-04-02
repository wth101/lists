def menu():
  print("1. Add to list")
  print("2. Delete from list")
  print("3. Exit")

def displayList():
  ###
  # Complete this function
  ###
  pass

# main
shopping = []
fh = open("shopping.txt")

###
# Write the code to open the shopping file and read it into the list shopping
###

choice = 0
while choice != 3:
  displayList()
  menu()
  choice = int(input())
  if choice == 1:
    item = input("Enter item to add: ")
    ###
    # Complete code
    ###
  elif choice == 2:
    item = input("Enter item to delete: ")
    ###
    # Complete code, overwirite file
    ###
  elif choice == 3:
    break
    







