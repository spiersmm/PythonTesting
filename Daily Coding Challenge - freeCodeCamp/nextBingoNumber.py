B_numbers = list(range(1,16))
I_numbers = list(range(16,31))
N_numbers = list(range(31,46))
G_numbers = list(range(46,61))
O_numbers = list(range(61,76))

def getNextBingoNumber(n):
  bingo_letter = n[0]
  bingo_number = int(n[1:])

  if (bingo_number + 1) > 75:
    bingo_number = abs(75-bingo_number)

  if (bingo_number + 1) in B_numbers:
    return "B" + str(bingo_number + 1)
  elif (bingo_number + 1) in I_numbers:
    return "I" + str(bingo_number + 1)
  elif (bingo_number + 1) in N_numbers:
    return "N" + str(bingo_number + 1)
  elif (bingo_number + 1) in G_numbers:
    return "G" + str(bingo_number + 1)
  else:
    return "O" + str(bingo_number + 1)


n = input("Enter the current Bingo Number: ")

print(getNextBingoNumber(n))