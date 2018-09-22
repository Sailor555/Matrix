#彩色螺旋

import turtle as tt

colors = ['red', 'blue', 'green',
          'purple',  'yellow', 'orange']
t = tt.Pen()
tt.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%len(colors)])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
