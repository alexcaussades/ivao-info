import sys
from cx_Freeze import setup, Executable
base = "Win32GUI"
basedevs = None
packages = ["module_forms"]
build_exe_options = dict(include_files=[("module_forms", "lib/module_forms"),
                                        ("module_forms/ia/class_log/data-airac.json", "lib/module_forms/ia/class_log/data-airac.json")])

setup(name='Ivao-Info',
      version='0.5.2-Alpha',
      description='IVAO Info recherche des ATCS et Pilots en ligne sur le serveur IVAO, via un logiciel',
      author='Alexandre Caussades',
      copyright="Alexandre Caussades",
      platform="windows",
      author_email='alexcaussades@gmail.com',
      url='https://github.com/alexcaussades/ivao-info',
      options = {'build_exe': build_exe_options},
      executables = [Executable("forms.py", base=basedevs, target_name='ivao-info-test', copyright="Alexandre Caussades")]
     )