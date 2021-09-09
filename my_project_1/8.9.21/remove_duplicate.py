reader = open("C:\\Users\\darvi\\Downloads\\employees.csv", "r")
lines = reader.read().split("\n")
reader.close()
writer = open("C:\\Users\\darvi\\Downloads\\employees.csv", "w")
for line in set(lines):
    writer.write(line + "\n")
writer.close()
