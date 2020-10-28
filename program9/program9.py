'''
Write a Python program to read a text file and remove all the lines that contains the character ‘a’ in the
file and write it in another file.
'''

oldfile = open('content.txt')
lines = oldfile.readlines()
newopen = open('newfile.txt', 'w')
#print(lines)

for line in lines:
    if 'a' in line:
        #print(line)
        line = line.replace(line, '')
    else:
        newopen.write(line)

newopen.close()
oldfile.close()






