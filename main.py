def menu():
  print("1. Add to list")
  print("2. Delete from list")
  print("3. Exit")

def displayList():
  for item in shopping:
    print(item)

# main
shopping = []
fh = open("shopping.txt", "r")
for line in fh:
  shopping.append(line.strip())
fh.close()

choice = 0
while choice != 3:
  displayList()
  menu()
  choice = int(input())
  if choice == 1:
    item = input("Enter item to add: ")
    shopping.append(item)
  elif choice == 2:
    item = input("Enter item to delete: ")
    if item in shopping:
      idx = shopping.index(item)
      shopping.pop(idx)
  elif choice == 3:
    fh = open("shopping.txt", "w")
    for item in shopping:
      fh.write(item+"\n")
    fh.close()
    break
    







