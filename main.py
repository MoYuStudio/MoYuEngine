
import moyu_engine
import moyu_engine.components as c

a = {'test':232}
b = {}

win = c.window.Window()
ev = c.event.Event()
save = c.save.Save(slot_name='save',write_data=a)

save.write()

save.read()

b = save.read_data
# b = b.decode()

print('=',b['test'])

while True:
    win.set()
    ev.quit()