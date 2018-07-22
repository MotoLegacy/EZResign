''' Python script to easily resign PlayStation 3 .PKGs and their .RAP
    files for use with PS3Han.
    Created by MotoLegacy'''

import os
import sys
import time
import shutil


failed = 0

#for knowing what commandline arguments to run
def getOS():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'win32' : 'Windows',
    }

    if sys.platform not in platforms:
        return sys.platform
    else:
        return platforms[sys.platform]

#package all .RAP files into one super duper easy to install pkg
def package():
    global failed
    count = 0
    rappkg = 'RIF000-INSTALLER_00-0000000000000000.pkg_signed.pkg'

    #notfy that a rap pkg is being generated
    print('Generating .RAP PKG..')

    #move all raps to where resigner can find them
    for raps in os.listdir('.'):
        if raps.endswith('.rap'):
            count += 1
            shutil.move(raps, 'utils/raps/{}'.format(raps))

    #no rap files found
    if count == 0:
        print('\nERR: RAP PKG not generated! Make sure to put .rap files with EZResign.py before execution!')
        failed += 1
        return

    #package on windows
    if getOS() == 'Windows':
        os.system('utils\SilentCMD utils\\resign_all.bat')
    
    #package on linux
    elif getOS() == 'Linux':
        os.system('nohup wine utils/resign_all.bat /dev/null 2>&1 &')

    shutil.move('utils/{}'.format(rappkg), './output/{}'.format(rappkg))

    #copy signed_act.dat to output
    shutil.move('utils/signed_act.dat', 'output/act.dat')





#sign the pkg with your idps and act.dat
def resign(pkg):
    global failed
    noex = pkg.split('.')[0]
    ex = pkg.split('.')[1]

    #don't sign an already signed pkg!
    if ex == 'pkg_signed':
        return

    #notify that pkg is being resigned
    print('Resigning {}'.format(noex))

    #resign on windows
    if getOS() == 'Windows':
        os.system('utils\SilentCMD utils\\ps3xploit_rifgen_edatresign.exe {}'.format(pkg))

    #resign on linux
    elif getOS() == 'Linux':
        os.system('nohup wine utils/ps3xploit_rifgen_edatresign.exe {} /dev/null 2>&1 &'.format(pkg))

    #resigner doesn't support OSX..  
    else:
        print('\nERR: Unsupported OS!')
        wait = input('Press ENTER to continue')
        quit()
    
    #make sure the file was created
    try:
        dump = open('ps3xploit_rifgen_edatresign.exe.stackdump')

    #no dump = success   
    except IOError:
        print('{} resigned successfully!\n'.format(noex))
        shutil.move('{}.pkg_signed.pkg'.format(noex), 'output/{}.pkg_signed.pkg'.format(noex))
        return

    dump.close()
    print('ERR: Unable to resign {}, is the package corrupted?\n'.format(pkg))
    failed += 1

    os.remove('ps3xploit_rifgen_edatresign.exe.stackdump')
    os.remove('{}.pkg_signed.pkg'.format(noex))
    return


def main():
    global failed
    for files in os.listdir('.'):
        if files.endswith('.pkg'):
            resign(files)

    package()

    if failed > 0:
        print('\nResigned packages with {} error(s)'.format(failed))
    else:
        print('All packages signed successfully!')
    
    wait = input('\nPress ENTER to continue')
    quit()


if __name__ == '__main__':
    main()