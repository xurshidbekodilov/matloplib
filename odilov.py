
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,250])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(5 * x) + 0.5 * np.sin(15 * x) + 0.2 * np.random.normal(size=500)

plt.plot(x, y, color='red',  )
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(5 * x) + 0.5 * np.sin(15 * x) + 0.2 * np.random.normal(size=500)

plt.plot(x, y, color='blue', marker="o" )
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(5 * x) + 0.5 * np.sin(15 * x) + 0.2 * np.random.normal(size=500)

plt.plot(x, y, color='black', marker="o", ms=8)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(5 * x) + 0.5 * np.sin(15 * x) + 0.2 * np.random.normal(size=500)

plt.plot(x, y, color='blue', marker="o", ms=8, mec='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(5 * x) + 0.5 * np.sin(15 * x) + 0.2 * np.random.normal(size=500)

plt.plot(x, y, color='black', marker="o", ms=8, mfc='r')
plt.show()

import  matplotlib.pyplot as plt
import numpy as np

x = np.array([2,2,5,5])
y = np.array([2,10,10,2])

plt.scatter(x,y)
plt.show()

import  matplotlib.pyplot as plt
import numpy as np

x = np.array([2,2,5,5])
y = np.array([2,10,10,2])
mycolor = ["red","green","blue","yellow"]

plt.scatter(x,y, color=mycolor)
plt.show()

import  matplotlib.pyplot as plt
import numpy as np

x = np.array([2,2,5,5])
y = np.array([2,10,10,2])
mycolor = ["red","green","blue","yellow"]
size = [12,8,16,20]

plt.scatter(x,y, s=size)
plt.show()