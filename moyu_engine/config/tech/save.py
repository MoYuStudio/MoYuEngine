def text_save(content,filename,mode='a'):
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

def text_read(filename):
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]

    file.close()
    return content

#write

#save = 'save 233'
#text_save(save,'save',mode='a')

#read

save_content = text_read('save')
print(save_content)

