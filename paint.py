from tkinter import *
import math
from PIL import ImageTk, Image
current_x = -1
current_y = -1
current_struct_instance = None
current_struct_selected = "line"
def checkIfXYValueExists(x_coord,y_coord,points):
    global current_x,current_y
    indices = [i for i, x in enumerate(points) if (x == x_coord) and (i%2 == 0)]
    for eachIndex in indices:
        if checkIfYValueExists(y_coord,eachIndex+1,points) and (len(points) - eachIndex > 15):
            print("true ("+str(x_coord)+","+str(y_coord)+") and ("+str(points[eachIndex])+","+str(points[eachIndex+1])+") exact")
            return eachIndex
    if current_x != -1:
        x_avg = (x_coord+current_x)/2
        floor = int(math.floor(x_avg))
        ceil = int(math.ceil(x_avg))
        indices = [i for i, x in enumerate(points) if (x == (floor) and (i%2 == 0))]
        for eachIndex in indices:
            if checkIfYValueExists(y_coord,eachIndex+1,points) and (len(points) - eachIndex > 15):
                print("true ("+str(x_coord)+","+str(y_coord)+") and ("+str(points[eachIndex])+","+str(points[eachIndex+1])+") avg floor")
                return eachIndex
        indices = [i for i, x in enumerate(points) if (x == (ceil) and (i%2 == 0))]
        for eachIndex in indices:
            if checkIfYValueExists(y_coord,eachIndex+1,points) and (len(points) - eachIndex > 15):
                print("true ("+str(x_coord)+","+str(y_coord)+") and ("+str(points[eachIndex])+","+str(points[eachIndex+1])+") avg ceil")
                return eachIndex
    i = 1
    while True:
        if i <= 5:
            if x_coord-i in points and (points.index(x_coord-i) % 2) == 0:
                if checkIfYValueExists(y_coord,points.index(x_coord-i)+1,points) and (len(points) - points.index(x_coord-i)+1 > 15):
                    eachIndex = points.index(x_coord-i)+1
                    print("true ("+str(x_coord)+","+str(y_coord)+") and ("+str(points[eachIndex])+","+str(points[eachIndex+1])+") adj")
                    return points.index(x_coord-i)
            if x_coord+i in points and (points.index(x_coord+i) % 2) == 0:
                if checkIfYValueExists(y_coord,points.index(x_coord+i)+1,points) and (len(points) - points.index(x_coord+i)+1 > 15):
                    eachIndex = points.index(x_coord+i)+1
                    print("true ("+str(x_coord)+","+str(y_coord)+") and ("+str(points[eachIndex])+","+str(points[eachIndex+1])+") adj")
                    return points.index(x_coord+i)
        else:
            break
        
        i = i+1
    return -1
            

def checkIfYValueExists(y,index,points):
    if points[index] == y:
        return True

    i = 1
    while True:
        if i <= 5:
            if points[index] == y -1 or points[index] == y + 1:
                return True
        else:
            break
        i = i+1
    return False

def leftButtonClick(event):
    global current_struct_selected
    if current_struct_selected == "fillcolor":
        x_coord = event.x
        y_coord = event.y
        widget = C.find_closest(x_coord,y_coord,halo=0)
        if C.type(widget) != None:
            if C.type(widget) == "polygon":
                points = C.coords(widget)
                all_x = points[::2]
                all_y = points[1::2]
                minX = min(all_x)
                minY = min(all_y)
                maxX = max(all_x)
                maxY = max(all_y)
                if minX <= event.x and maxX >= event.x and minY <= event.y and maxY >= event.y:
                    C.itemconfigure(widget,fill="black")
            elif C.type(widget) == "rectangle" or C.type(widget) == "oval":
                points = C.coords(widget)
                if points[0] <= event.x and points[2] >= event.x and points[1] <= event.y and points[3] >= event.y:
                    C.itemconfigure(widget,fill="black")
        
# def leftButtonClickForPolygon(event):
#     #some code here
# def rightButtonClick(event):
#     #some code here

def leftButtonReleased(event):
    global current_x,current_y,current_struct_instance
    current_x = -1
    current_y = -1
    current_struct_instance = None

def changeStruct(str):
    global current_struct_selected
    current_struct_selected = str
    print(current_struct_selected)

def clickedPolygon(self,event):
    print(self)
    print(event)

def mouseMoveWithLeftClick(event):
    global current_x,current_y,current_struct_instance,current_struct_selected
    if current_struct_selected == "line":
        if current_x == -1 and current_y == -1:
            current_struct_instance = C.create_line(event.x, event.y,  event.x, event.y,  fill ="black",width=3,capstyle=ROUND)
            current_x = event.x
            current_y = event.y
        else:
            shouldCreatePolygon = False
            x_index = -1
            points = C.coords(current_struct_instance)
            index_val = checkIfXYValueExists(event.x,event.y,points)
            if index_val != -1:
                x_index = index_val
                shouldCreatePolygon = True
            points.append(event.x)
            points.append(event.y)
            C.coords(current_struct_instance,points)
            if shouldCreatePolygon and x_index != -1:
                polygon_points = points[x_index:]
                poly = C.create_polygon(polygon_points,joinstyle = ROUND,width = 3,outline="black",fill="")
            # C.create_line(current_x, current_y,  event.x, event.y,  fill ="black",width=5,capstyle=ROUND)
            current_x = event.x
            current_y = event.y
    elif current_struct_selected == "rectangle":
        if current_x == -1 and current_y == -1:
            current_struct_instance = C.create_rectangle(event.x, event.y,  event.x, event.y,outline="black",  fill ="",width=3)
            current_x = event.x
            current_y = event.y
        else:
            points = C.coords(current_struct_instance)
            x_coord = current_x
            y_coord = current_y
            if event.x >= x_coord and event.y <= y_coord:
                points[0] = x_coord
                points[1] = event.y
                points[2] = event.x
                points[3] = y_coord
            elif event.x <= x_coord and event.y >= y_coord:
                points[2] = x_coord
                points[3] = event.y
                points[0] = event.x
                points[1] = y_coord
            elif event.x <= x_coord and event.y <= y_coord:
                points[0] = event.x
                points[1] = event.y
                points[2] = x_coord
                points[3] = y_coord
            else:
                points[2] = event.x
                points[3] = event.y
            C.coords(current_struct_instance,points)
    elif current_struct_selected == "oval":
        if current_x == -1 and current_y == -1:
            current_struct_instance = C.create_oval(event.x, event.y,event.x,event.y,  fill ="",width=3)
            current_x = event.x
            current_y = event.y
        else:
            points = C.coords(current_struct_instance)
            x_coord = current_x
            y_coord = current_y
            if event.x >= x_coord and event.y <= y_coord:
                points[0] = x_coord
                points[1] = event.y
                points[2] = event.x
                points[3] = y_coord
            elif event.x <= x_coord and event.y >= y_coord:
                points[2] = x_coord
                points[3] = event.y
                points[0] = event.x
                points[1] = y_coord
            elif event.x <= x_coord and event.y <= y_coord:
                points[0] = event.x
                points[1] = event.y
                points[2] = x_coord
                points[3] = y_coord
            else:
                points[2] = event.x
                points[3] = event.y
            C.coords(current_struct_instance,points)
root = Tk()

root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))
height = root.winfo_screenheight() 
width = root.winfo_screenwidth() 
root.geometry(str(int(width*3/4))+"x"+str(int(height*3/4))+"+"+str(int(width/8))+"+"+str(int(height/8)))
root.title("Paint")
# rectImage = Image.open("rectangle.png")
# rectImage = rectImage.resize((10, 10), Image.ANTIALIAS)
# rectImage = PhotoImage(rectImage)

structures = Frame(root,bg = "#007bff")
rect = Button(structures,text = "Rect",borderwidth = 0,command = lambda: changeStruct("rectangle"))
rect.place(relx = 0.005,relwidth = 0.49,relheight = 0.1)
oval = Button(structures,text = "Oval",borderwidth = 0,command = lambda: changeStruct("oval"))
oval.place(relx = 0.505,relwidth = 0.49,relheight = 0.1)
fillColor = Button(structures,text = "Fill",borderwidth = 0,command = lambda: changeStruct("fillcolor"))
fillColor.place(relx = 0.005,rely = 0.105,relwidth = 0.49,relheight = 0.1)
pencil = Button(structures,text = "Pencil",borderwidth = 0,command = lambda: changeStruct("line"))
pencil.place(relx = 0.505,rely = 0.105,relwidth = 0.49,relheight = 0.1)
structures.place(relx = 0.0,rely = 0.0,relwidth = 0.1,relheight = 0.4)


C = Canvas(root, width = int((width*3)/4), height = height, bg = '#FFFFFF',cursor = "sizing")
C.place(relx = 0.1,rely = 0.0,relwidth = 0.9,relheight = 1)
C.bind("<Button-1>", leftButtonClick)
#C.bind("<Button-3>", rightButtonClick)
C.bind("<B1-Motion>",mouseMoveWithLeftClick)
C.bind("<ButtonRelease-1>",leftButtonReleased)
#C.tag_bind(poly,"<Button-1>", leftButtonClickForPolygon)
#print(C.coords(poly))

mainloop()
