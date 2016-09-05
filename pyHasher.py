import hashlib
import errno
import os
import sys
## no output. Trying to leave bread crumbs.
def test():
    print("test")
#target directory
target = 'OS.js'
##
def hashall(folder):
  if os.path.isdir(folder):
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,f)):
            try:
                with open(os.path.join(folder, f),'rb') as i:
                #with open(f,'rb') as i:
                    buf = i.read()
                    try:
                      with open('hashlog.txt','a') as l:
                          hasher = hashlib.md5(buf)
                          l.write(os.path.join(folder,f) + ': ' + hasher.hexdigest()+'\n')
                    except IOError as exc:
                      print("error writing to log")
            except IOError as exc:
                print("error opening file")
        if os.path.isdir(os.path.join(folder,f)):
            hashall(os.path.join(folder,f))
  if os.path.isfile(folder):
    try:
      with open(folder,'rb') as i:
        buf = i.read()
        try:
          with open('hashlog.txt','a') as l:
            hasher = hashlib.md5()
            hasher.update(buf)
            l.write(folder + ': ' + hasher.hexdigest()+'\n')
        except IOError as exc:
          print("error writing log")
    except IOError as exc:
      print("error opening file")
##Execution
hashall(target)
##Previous attempt
##for name in glob.glob(os.path.walk()):
  ##  try:
    ##    with open(name) as f:
      ##      buf = f.read()
        ##    test()
          ##  try:
            ##    with open('hashlog.txt','wb') as l:
              ##      l.write(hasher.hexdigest()+'\n')
                ##    print(hasher.hexdigest())
                  ##  test()
          ##  except IOError as exc:
            ##    print("error saving file")
              ##  if exc.errno != errno.EISDIR:
                ##    raise
   ## except IOError as exc:
     ##   if exc.errno!= errno.EISDIR:
       ##     raise
