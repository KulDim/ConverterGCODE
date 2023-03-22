gcode = open("rounded-square.ngc", "r", encoding="utf-8")

json = []
Zposition = ''
Xposition = []
Yposition = []

for g in gcode:

    if g[0] == '(' and g[len(g) -2] == ')':
        continue

    if g.rstrip('\n').split(" ")[0] == 'G01':

        for line in g.rstrip('\n').split(" "):
            print(line)
            if line[0] == 'X':
                Xposition.append(line[1::])
                
            if line[0] == 'Y':
                Yposition.append(line[1::])

            if line[0] == 'Z':
                if Zposition != line.split("-")[1]:
                    Zposition = line.split("-")[1]
                    # print(line.split("-")[1])

                    json.append({'Z': Zposition, 'XY': {'X': Xposition, 'Y': Yposition}})


            
# print(json)
        # print(g.rstrip('\n').split(" "))

file = open('Failed.html', 'w')
file.write('<svg height="100%" width="100%" xmlns="http://www.w3.org/2000/svg">  \n')
for z in json:
    for i in range(len(z["XY"]["X"])): 
        file.write(f'<line x1="{z["XY"]["X"][i - 1]}" y1="{z["XY"]["Y"][i - 1]}" x2="{z["XY"]["X"][i]}" y2="{z["XY"]["Y"][i]}" stroke="black" /> \n')
file.write('</svg> \n')

file.close()