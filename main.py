import csv

with open('quarterback_fileio_example.csv', 'r') as csvfile:
    qb_data = csv.reader(csvfile, delimiter=',')
    for row_num, row in enumerate(qb_data):
        print(f'Row {row_num}: {row}')


#read csv data and calc the avg touchdowns and interceptions
with open('quarterback_fileio_example.csv', 'r') as csvfile:
    td_total = 0
    intc_total = 0
    qb_data = csv.reader(csvfile, delimiter=',')

    for row_num, row in enumerate(qb_data):
        if row_num == 0:
            continue
        else:
            td_total += int(row[1])
            intc_total += int(row[2])

    td_avg = td_total / len(qb_data)
    intc_avg = intc_total / len(qb_data)
    


#Read in file 
#print each line out
'''
with open('updated_dog_breeds.txt', 'r') as file:
    data = file.read()
    print(data)
'''
'''
with open('updated_dog_breeds.txt', 'r') as file:
    #option 3
    for line in file:
        print(line, end='')
        
    
    #option 2
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()

    
    #optional
    data = file.readlines()
    for line in data:
        print(line, end = '')


file = open('updateed_dog_breeds.txt')

data = file.read()

print(data)

file.close()




with open('updated_dog_breeds.txt', 'a') as file:
    #option 3
    file.write(str(10))

    #option 2
    file.writelines(['Sheperd\n', 'Spaniel\n'])
    
    #option 1
    file.write("\nGolden Retriever\n")




'''