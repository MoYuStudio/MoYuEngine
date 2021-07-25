def write(filename,data):
    write_data = open(filename,'w')
    write_data.write(data)
    
def read(filename):
    read_data = open(filename,'r')
    data = read_data.read()
    print(data)
    
read('save_self')
