"""
Introducción a Matplot
"""

#%%

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, marker = '*')
plt.show()


#%%

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 14, 29, 2])

plt.plot(ypoints, 
         marker = 'o', 
         color='#008000', 
         linestyle=':',
         linewidth = '4')
plt.show()

#%%
"""
Marker 	Description
'o' 	Circle 	
'*' 	Star 	
'.' 	Point 	
',' 	Pixel 	
'x' 	X 	
'X' 	X (filled) 	
'+' 	Plus 	
'P' 	Plus (filled) 	
's' 	Square 	
'D' 	Diamond 	
'd' 	Diamond (thin) 	
'p' 	Pentagon 	
'H' 	Hexagon 	
'h' 	Hexagon 	
'v' 	Triangle Down 	
'^' 	Triangle Up 	
'<' 	Triangle Left 	
'>' 	Triangle Right 	
'1' 	Tri Down 	
'2' 	Tri Up 	
'3' 	Tri Left 	
'4' 	Tri Right 	
'|' 	Vline 	
'_' 	Hline

"""
#%%
"""
Line Syntax 	Description
'-' 	Solid line 	
':' 	Dotted line 	
'--' 	Dashed line 	
'-.' 	Dashed/dotted line

Color Syntax 	Description
'r' 	Red 	
'g' 	Green 	
'b' 	Blue 	
'c' 	Cyan 	
'm' 	Magenta 	
'y' 	Yellow 	
'k' 	Black 	
'w' 	White

"""


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 
#          marker = 'o', #Tipo de marcador
#          ms = 20,      #Tamaño
#          mec = 'r')    #Color borde

plt.plot(ypoints,
          marker = '*',
          ms = 19,
          mec = '#4CAF50', #Color borde
          mfc = 'b') #Color relleno



plt.show()

#%%

plt.plot(ypoints, linewidth = '10')

#%%

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3=np.array([1,10,4,2,2])

plt.plot(y1,linewidth = '10')
plt.plot(y2,linewidth = '5')
plt.plot(y3,linewidth = '8')

plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 2, 10,20])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

fuente = {'family':'serif',
          'color':'darkred',
          'size':15}

fuente2 = {'family':'sans',
          'color':'blue',
          'size':15}

plt.plot(x, y)

plt.xlabel("EJE X",fontdict = fuente2)
plt.ylabel("Eje Y")


plt.title("Sports Watch Data", fontdict = fuente, loc = 'left')

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5, axis='y')

plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = [0, 1, 2, 3]
y = np.array([3, 8.2, 1, 10])

## FILAS, COLUMNAS, INDICES

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x1 = np.linspace(0,10,100) ## crea un array de 0 a 10 con 100 elementos
y1 = x1**2

plt.subplot(1, 2, 2)
plt.plot(x,y, x1,y1)

plt.show()

#%%


import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.linspace(0,10,100) ## crea un array de 0 a 10 con 100 elementos
y = x**2

plt.subplot(2, 2, 4)
plt.plot(x,y)

plt.title("INCOME")

plt.suptitle("MY SHOP")

plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors, cmap='Spectral', s=sizes, alpha=0.9)

plt.colorbar()

plt.show() 

#%%

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y,alpha=0.5,width = 0.8)
plt.show()

#%%

x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)

#%%

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

#%%

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.3, 0.5, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
# plt.legend()
plt.show() 
