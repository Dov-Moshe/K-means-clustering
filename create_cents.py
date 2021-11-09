import random
import sys

#num = sys.argv[1]

f2 = open("2.txt", "w")
for i in range(2):
    f2.write(str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + "\n")

f2.close()


f4 = open("4.txt", "w")
for i in range(4):
    f4.write(str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + "\n")

f4.close()


f8 = open("8.txt", "w")
for i in range(8):
    f8.write(str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + "\n")

f8.close()


f16 = open("16.txt", "w")
for i in range(16):
    f16.write(str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + " " + str(round(random.random(), 4)) + "\n")

f16.close()