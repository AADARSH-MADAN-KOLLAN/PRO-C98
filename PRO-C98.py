def SwapData():
    file1 = input("Enter the first file to be swapped: ")
    file2 = input("Enter the second file to be swapped: ")
    with open(file1, 'r') as f1:
        data_f1 = f1.read()
    with open(file2, 'r') as f2:
        data_f2 = f2.read()
    with open(file1, 'w') as f1:
        f1.write(data_f2)
    with open(file2, 'w') as f2:
        f2.write(data_f1)
    print("Your file has been swapped!")
 
SwapData();