#open the needed files
with open("integers.txt" , "r") as integers_file, open("double.txt" , "a") as double_file, open("tripple.txt" , "a") as tripple_file:
    #for loops to read the lines
    for line in integers_file:
        #convert the lines to integeers
        number = int(line)
        #check if even
        if number % 2 == 0:
            #square the number
            squared = number ** 2
            #convert to sring
            even = str(squared)
            #write to even file
            double_file.write(even + "\n")
        #check if odd
        elif number % 2 == 1:
            #cube the number
            cubed = number ** 3
            #convert to sring
            odd = str(cubed)
            #write to odd file
            tripple_file.write(odd + "\n")