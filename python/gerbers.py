import os
import zipfile

dir = '/'
dir2 = 'gerbers/'
projectName = 'BobProject'

gtp = False
gts = False
gtl = False
gto = False
gl2 = False
gl3 = False
gbp = False
gbs = False
gbl = False
gbo = False
gko = False
drl = False

zipf = zipfile.ZipFile(dir+projectName+'.zip','w',zipfile.ZIP_DEFLATED)

os.chdir(dir2)

for file in os.listdir(dir):
    if(file.endswith('.gtp')):
        #print('Top Paste')
        temp = file.split('.gtp')
        os.rename(dir+file,dir+projectName+'.gtp')
        zipf.write(os.path.join('',dir+projectName+'.gtp'))
        gtp = True
    elif(file.endswith('.gts')):
        #print('Top Soldermask')
        temp = file.split('.gts')
        os.rename(dir+file,dir+projectName+'.gts')
        zipf.write(os.path.join('',dir+projectName+'.gts'))
        gts = True
    elif(file.endswith('.gtl')):
        #print('Top Layer')
        temp = file.split('.gtl')
        os.rename(dir+file,dir+projectName+'.gtl')
        zipf.write(os.path.join('',dir+projectName+'.gtl'))
        gtl = True
    elif(file.endswith('.gto')):
        #print('Top Silkscreen')
        temp = file.split('.gto')
        os.rename(dir+file,dir+projectName+'.gto')
        zipf.write(os.path.join('',dir+projectName+'.gto'))
        gto = True
    elif(file.endswith('.gl2')):
        #print('Inside Layer 2')
        temp = file.split('.gl2')
        os.rename(dir+file,dir+projectName+'.gl2')
        zipf.write(os.path.join('',dir+projectName+'.gl2'))
        gl2 = True
    elif(file.endswith('.gl3')):
        #print('Inside Layer 3')
        temp = file.split('.gl3')
        os.rename(dir+file,dir+projectName+'.gl3')
        zipf.write(os.path.join('',dir+projectName+'.gl3'))
        gl3 = True
    elif(file.endswith('.gbp')):
        #print('Bottom Paste')
        temp = file.split('.gbp')
        os.rename(dir+file,dir+projectName+'.gbp')
        zipf.write(os.path.join('',dir+projectName+'.gbp'))
        gbp = True
    elif(file.endswith('.gbs')):
        #print('Bottom Soldermask')
        temp = file.split('.gbs')
        os.rename(dir+file,dir+projectName+'.gbs')
        zipf.write(os.path.join('',dir+projectName+'.gbs'))
        gbs = True
    elif(file.endswith('.gbl')):
        #print('Bottom Layer')
        temp = file.split('.gbl')
        os.rename(dir+file,dir+projectName+'.gbl')
        zipf.write(os.path.join('',dir+projectName+'.gbl'))
        gbl = True
    elif(file.endswith('.gbo')):
        #print('Bottom Silkscreen')
        temp = file.split('.gbo')
        os.rename(dir+file,dir+projectName+'.gbo')
        zipf.write(os.path.join('',dir+projectName+'.gbo'))
        gbo = True
    elif(file.endswith('.gko')):
        #print('Edge Cut Layer')
        temp = file.split('.gko')
        os.rename(dir+file,dir+projectName+'.gko')
        zipf.write(os.path.join('',dir+projectName+'.gko'))
        gko = True
    elif(file.endswith('.drl')):
        #print('Drill File')
        temp = file.split('.drl')
        os.rename(dir+file,dir+projectName+'.txt')
        zipf.write(os.path.join('',dir+projectName+'.txt'))
        drl = True

if(not gtp):
    print('Top Paste MISSING!!!')
if(not gts):
    print('Top Soldermask MISSING!!!')
if(not gtl):
    print('Top Layer MISSING!!!')
if(not gl2):
    print('Inside Layer 2 MISSING!!!')
if(not gl3):
    print('Inside Layer 3 MISSING!!!')
if(not gbp):
    print('Bottom Paste MISSING!!!')
if(not gbs):
    print('Bottom Soldermask MISSING!!!')
if(not gbl):
    print('Bottom Layer MISSING!!!')
if(not gbo):
    print('Bottom Silkscreen MISSING!!!')
if(not gto):
    print('Top Silkscreen MISSING!!!')
if(not drl):
    print('Drill File MISSING!!!')
if(not gko):
    print('Edge Cut Layer MISSING!!!')


zipf.close()