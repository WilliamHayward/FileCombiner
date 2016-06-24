print("Start file build")
config = open('config.txt','r')
#config.txt expected format:
#OUT
#output.txt
#IN
#input1.txt
#input2.txt

mode = "INIT"
command = False
text = ""
filename = ""
for line in config.readlines():
    command = False
    line = line.rstrip()
    if (line == "IN") or (line == "OUT") :
        command = True
    if command:
        mode = line;
    else:
        if mode == "IN":
            infile = open(line,'r')
            text += infile.read() + '\n'
            infile.close()
        elif mode == "OUT":
            filename = line
file = open(filename,'w')
file.write(text)
file.close()
print("Build complete")
