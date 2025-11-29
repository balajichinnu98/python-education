# words = ["hello", "world"]

# def return_word():
#     for i in words:
#       print(i, end=" ")


# return_word()


# def blender(*args):
#     print("Details:", end=" ")
#     for item in args:
#         print(item, end=" ")

# blender('apple', 'banana', 'cherry')

# cars = ("BMW", "Audi", "Toyota")


# def juice_maker(car):
#     return car + " brands"

# automotive = map(juice_maker, cars)

# print("German cars=", end=" ")
# for car in automotive:
#     print(car, end=" ")


# brands = ("Ford", "Chevrolet", "Dodge")


# def cars(*car):
#     return car[0] + " is a good car"

# returnCars = map(cars, brands) 

# for products in returnCars:
#        print(products)


# brands = ("Ford", "Chevrolet", "Dodge")


# def cars(*car):
#     return car[0] + " is a good car"

# returnCars = map(cars, brands) 

# for products in returnCars:
#        print(products)


# brands = ("Ford", "Chevrolet", "Dodge")


# def cars(car):
#     return car + " is a good car"

# returnCars = list(map(cars, brands))

# # for products in returnCars:
# #        print(products)

# def filter_brands(sentence):
#       return sentence.split(" ")[0]

# filteredBrands = list(map(filter_brands, returnCars))

# for alter in filteredBrands:
#        print(alter, end=" ")



# numbers = [1, 2, 3, 4, 5,6,9,11,10,5]
# evenNumbers = list(numbers,lambda x: x % 2 == 0)
# print(evenNumbers)


# numbers = [7,1, 2, 3, 7,1,2,4,5,3,4, 5,6,9,11,10,5]
# print(set(numbers))


############### TIC TAC TOE GAME #####################

boardNumbers = [1,2,3,4,5,6,7,8,9]


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")  
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("--+---+--")

print_board(boardNumbers)



####### CHECK THE BOX IS FULL OR NOT ########

def is_board_full(board):
    for cell in board:
        if cell!= 'X' and cell!= 'O':
            return False  
          
    print("Board is full")
    return True


########  CHECK WINNER ##############


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

##### USER INPUT CODE BELOW ########

while True:
    playerPlace = int(input("Enter a number between 1-9: "))
    print(f"You entered: {playerPlace}")
    placeOnBoard = boardNumbers.index(playerPlace) 
    boardNumbers[placeOnBoard] = 'X' 
    print(print_board(boardNumbers)) 

    if check_winner(boardNumbers, 'X'):
        print("Player X wins!")
        break
    
    
    if is_board_full(boardNumbers):
        break   
    
    playerPlace = int(input("Enter a number between 1-9: "))
    print(f"You entered: {playerPlace}")
    placeOnBoard = boardNumbers.index(playerPlace) 
    boardNumbers[placeOnBoard] = 'O' 
    print(print_board(boardNumbers)) 

    if check_winner(boardNumbers, 'O'):
        print("Player O wins!")
        break
    

    if is_board_full(boardNumbers):
        break


if is_board_full(boardNumbers):
    if not check_winner(boardNumbers, 'X') and not check_winner(boardNumbers, 'O'):
        print("Draw Match!")



