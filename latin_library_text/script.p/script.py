import os

def get_dir_name(filename):
    pos1 = filename.find('_')
    #pos2 = filename.find('.')
    #return filename[pos1+1:pos2]
    return filename[:pos1]
  
  
  
for f in os.listdir('./'):
    cwd = os.getcwd()
    dir_name = cwd+'/'+get_dir_name(f)
    print(dir_name)
    if not os.path.exists(dir_name):
      os.mkdir(dir_name)
    os.rename(f, dir_name+'/'+f)
