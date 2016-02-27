# coding: utf-8

import os
import sys
import os.path
import zipfile
import tempfile

rootdir = sys.argv[1]  # 指明被遍历的文件夹
targetzip = 'symbols.zip'  # 指明输出的压缩包
if len(sys.argv) > 2:  # 指明输出的文件夹
    targetzip = sys.argv[2]
print "root: " + rootdir

data = []
zip = zipfile.ZipFile(targetzip, 'w', zipfile.ZIP_DEFLATED)
tf = tempfile.NamedTemporaryFile(suffix='.sym')
tempfilename = tf.name
tf.close()
for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    print "p: " + parent
    for dirname in dirnames:  # 输出文件夹信息parent
        print "d: " + dirname
    for filename in filenames:  # 输出文件信息
        print "f: " + filename
        if filename.lower().endswith('.pdb'):
            symFilename = os.path.splitext(filename)[0] + ".sym"
            cmd = 'dump_syms.exe ' + os.path.join(parent, filename) + ' > ' + tempfilename
            print 'cmd: ' + cmd
            #out = os.popen(cmd)
            #data = ''.join(out.readlines())
            #target = os.path.join(targetzip, symFilename)
            os.system(cmd)
            arcname = 'symbols\\' + symFilename
            zip.write(tempfilename, arcname)
            #zip.write(target, '.\\Out\\'+filename)
    #print "the full name of the file is:" + os.path.join(parent,filename) # 输出文件路径信息
    break
zip.close()
