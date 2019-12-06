import os
import zipfile

#dir = '/'
#dir2 = 'gerbers/'
#output = 'BobProject'

def process(dir,output):
    TopLayer = ''
    TopSolderMask = ''
    TopPaste = ''
    TopSilkscreen = ''

    InnerLayer1 = ''
    InnerLayer2 = ''

    BottomLayer = ''
    BottomSolderMask = ''
    BottomPaste = ''
    BottomSilkscreen = ''

    EdgeCut = ''
    DrillFile = ''

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

    zipf = zipfile.ZipFile(output+'.zip','w',zipfile.ZIP_DEFLATED)

    os.chdir(dir)

    for file in os.listdir(dir):
        if("F_Paste" in file):
            #print('Top Paste')
            TopPaste = file
            temp = file.split('.gtp')
            os.rename(dir+file,dir+output+'.gtp')
            zipf.write(filename=os.path.join('',output+'.gtp'),arcname=output+'.gtp')
            gtp = True
        elif("F_Mask" in file or "F.Mask" in file):
            #print('Top Soldermask')
            TopSolderMask = file
            temp = file.split('.gts')
            os.rename(dir+file,dir+output+'.gts')
            zipf.write(os.path.join('',dir+output+'.gts'))
            gts = True
        elif("F_Cu" in file or "F.Cu" in file):
            #print('Top Layer')
            TopLayer = file
            temp = file.split('.gtl')
            os.rename(dir+file,dir+output+'.gtl')
            zipf.write(os.path.join('',dir+output+'.gtl'))
            gtl = True
        elif("F_SilkS" in file or "F.SilkS" in file):
            #print('Top Silkscreen')
            TopSilkscreen = file
            temp = file.split('.gto')
            os.rename(dir+file,dir+output+'.gto')
            zipf.write(os.path.join('',dir+output+'.gto'))
            gto = True
        elif("In1_Cu" in file or "In1.Cu" in file):
            #print('Inside Layer 2')
            InnerLayer1 = file
            temp = file.split('.gl2')
            os.rename(dir+file,dir+output+'.gl2')
            zipf.write(os.path.join('',dir+output+'.gl2'))
            gl2 = True
        elif("In2_Cu" in file or "In2.Cu" in file):
            #print('Inside Layer 3')
            InnerLayer2 = file
            temp = file.split('.gl3')
            os.rename(dir+file,dir+output+'.gl3')
            zipf.write(os.path.join('',dir+output+'.gl3'))
            gl3 = True
        elif("B_Paste" in file or "B.Paste" in file):
            #print('Bottom Paste')
            BottomPaste = file
            temp = file.split('.gbp')
            os.rename(dir+file,dir+output+'.gbp')
            zipf.write(os.path.join('',dir+output+'.gbp'))
            gbp = True
        elif("B_Mask" in file or "B.Mask" in file):
            #print('Bottom Soldermask')
            BottomSolderMask = file
            temp = file.split('.gbs')
            os.rename(dir+file,dir+output+'.gbs')
            zipf.write(os.path.join('',dir+output+'.gbs'))
            gbs = True
        elif("B_Cu" in file or "B.Cu" in file):
            #print('Bottom Layer')
            BottomLayer = file
            temp = file.split('.gbl')
            os.rename(dir+file,dir+output+'.gbl')
            zipf.write(os.path.join('',dir+output+'.gbl'))
            gbl = True
        elif("B_SilkS" in file or "B.SilkS" in file):
            #print('Bottom Silkscreen')
            BottomSilkscreen = file
            temp = file.split('.gbo')
            os.rename(dir+file,dir+output+'.gbo')
            zipf.write(os.path.join('',dir+output+'.gbo'))
            gbo = True
        elif("Edge_Cuts" in file or "Edge.Cuts" in file):
            #print('Edge Cut Layer')
            EdgeCut = file
            temp = file.split('.gko')
            os.rename(dir+file,dir+output+'.gko')
            zipf.write(os.path.join('',dir+output+'.gko'))
            gko = True
        elif(file.endswith('.drl')):
            #print('Drill File')
            DrillFile = file
            temp = file.split('.drl')
            os.rename(dir+file,dir+output+'.txt')
            zipf.write(os.path.join('',dir+output+'.txt'))
            drl = True

    print("Found:")
    print("TopLayer:\t%s"%TopLayer)
    print("TopSolderMask:\t%s"%TopSolderMask)
    print("TopPaste:\t%s"%TopPaste)
    print("TopSilkscreen:\t%s"%TopSilkscreen)

    print("InnerLayer1:\t%s"%InnerLayer1)
    print("InnerLayer2:\t%s"%InnerLayer2)

    print("BottomLayer:\t%s"%BottomLayer)
    print("BottomSolderMask:\t%s"%BottomSolderMask)
    print("BottomPaste:\t%s"%BottomPaste)
    print("BottomSilkscreen:\t%s"%BottomSilkscreen)

    print("EdgeCuts:\t%s"%EdgeCut)
    print("DrillFile:\t%s"%DrillFile)


    ''' if(not gtp):
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
        print('Edge Cut Layer MISSING!!!') '''
    zipf.close()

def main(argv):
    import argparse
    parser = argparse.ArgumentParser(description="Does stuff")
    parser.add_argument("-d", "--directory", dest='dir',default= '', required=True,help='filenamo')
    parser.add_argument("-o", "--output", dest="output", default='', required=True,help='filenamo')
    #parser.add_argument("-p","--plot", dest="plot",default=False,required=False,help='PLOOTT')
    #parser.add_argument("-v","--verbose", dest="verbose",default=False,required=False,help='print everything')
    args = parser.parse_args(argv)
    process(args.dir,args.output)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])