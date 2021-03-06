"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import os, sys, subprocess

APP = ['opendvdproducer.py']
NAME = str(open('debian/changelog').read()).split(' (')[0]
VERSION = str(open('debian/changelog').read()).split('(')[1].split(')')[0]
if sys.platform == 'darwin':
    OPTIONS = {'py2app':  {
                    'argv_emulation': True,
                    'iconfile':'pixmaps/opendvdproducer.icns',
                    'emulate_shell_environment':True,
                    'frameworks':[  'libs/libMagickCore-6.Q16.1.dylib',
                                    'libs/libiconv.2.dylib',
                                    'libs/libpng16.16.dylib',
                                    'libs/libfreetype.6.dylib',
                                    'libs/libintl.8.dylib',
                                    ],
                }}
    REQUIRES = ['py2app']
    share_or_resources = ''
else:
    OPTIONS = {}
    REQUIRES = []
    share_or_resources = 'share/' + NAME + '/'

DATA_FILES = []
for filename in os.listdir('graphics'):
    filepath = 'graphics' + os.sep + filename
    if os.path.isfile(filepath) and (filepath.endswith('png') or filepath.endswith('mkv')):
        DATA_FILES.append((share_or_resources + 'graphics', [filepath]))

for filename in os.listdir('resources'):
    filepath = 'resources' + os.sep + filename
    if os.path.isfile(filepath):
        if filepath.endswith('flac') or (not sys.platform.startswith('linux') and filepath.endswith('ttf')) or (sys.platform == 'darwin' and (not filepath.endswith('exe') and not filepath.endswith('dll'))):
            DATA_FILES.append((share_or_resources + '', [filepath]))

if sys.platform == 'darwin':
    DATA_FILES.append(('../PlugIns/phonon_backend', ['/Developer/Applications/Qt/plugins/phonon_backend/libphonon_qt7.dylib']))
elif sys.platform.startswith('linux'):
    DATA_FILES.append(('bin', ['bin/' + NAME]))
    DATA_FILES.append(('share/applications', ['bin/' + NAME + '.desktop']))
    DATA_FILES.append(('share/pixmaps', ['pixmaps/' + NAME + '.png']))
    DATA_FILES.append(('share/' + NAME, [NAME + '.py']))
setup(
    name='Open DVD Producer',
    version=VERSION,
    app=APP,
    data_files=DATA_FILES,
    options=OPTIONS,
    setup_requires=REQUIRES,
)

if sys.platform == 'darwin':
    #subprocess.call(['otool', '-L', 'binary'])
    #subprocess.call(['install_name_tool', '-change', '/usr/local/lib/libfreetype.6.dylib', '@executable_path/../Frameworks/libfreetype.6.dylib'])
    #subprocess.call(['rm', 'dist/Open DVD Producer.app/Contents/Resources/mkisofs'])
    #subprocess.call(['cp', 'resources/mkisofs', 'dist/Open DVD Producer.app/Contents/Resources/mkisofs'])
    subprocess.call(['chmod', '-R', '777', 'dist/Open DVD Producer.app'])
