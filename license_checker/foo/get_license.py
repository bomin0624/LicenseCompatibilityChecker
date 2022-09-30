"""License Compatibility Checker - A tool that helps checking the compatibility of the licenses."""
import subprocess
import os
import re
from urllib.request import urlopen
import json
import itertools


# OSADL-matrix json file
URL = 'https://www.osadl.org/fileadmin/checklists/matrix.json'
response = urlopen(URL)
licenses = json.loads(response.read())


# Folder path
os.chdir('/Users/bomin/Desktop/communication-project/license_checker/foo/')

TERMINALOUTPUT = subprocess.run("license-checker", capture_output=True, shell=True, check=True)
TERMINALOUTPUT = str(TERMINALOUTPUT.stdout).replace("\n"," ")


# Regular expression
LICENSEPATH = r"licenses: [\w\-\.\()\ ]+"
PACKAGEPATH = r"x80 [\w\-\.\()\ @]+"
URLPATH = r"repository: https?://(?:[\w]|[/\./-])*"

findallPackages = re.findall(PACKAGEPATH,TERMINALOUTPUT)
findall_Licenses = re.findall(LICENSEPATH,TERMINALOUTPUT)
findall_Urls = re.findall(URLPATH, TERMINALOUTPUT)

# Installed package name
package_arr = []
license_arr = []
url_arr = []

for i, package in enumerate(findallPackages):
    if '@' in package:
        package_arr.append(package[4:])
# print("package list:",package_arr)

# Set an example for the array
# package_arr = ['js-tokens@4.0.0',
# 							'loose-envify@1.4.0',
# 							'react@18.2.0',
# 							'yui-lint@0.2.0',
# 							'hubot-afl',
# 							'AGPL-3.0@0.1.0',
# 							'TEST@0.1.0']

# license_arr = ['MIT','MIT','MIT','BSD','AFL-2.0','AGPL-3.0-only','UNKNOWN']

# packageLicense = {'js-tokens@4.0.0': 'MIT',
#                   'loose-envify@1.4.0': 'MIT',
#                   'react@18.2.0': 'MIT',
#                   'yui-lint@0.2.0': 'BSD',
#                   'hubot-afl':'AFL-2.0',
#                   'AGPL-3.0@0.1.0':'AGPL-3.0-only',
#                   'TEST@0.1.0':'UNKNOWN'}

# URL example
# url_arr = ['repository: https://github.com/lydell/js-tokens',
# 					'repository: https://github.com/zertosh/loose-envify',
# 					'repository: https://github.com/facebook/react',
# 					'repository: https://github.com/yui/yui-lint',
# 					'repository: https://github.com/test/test01',
# 					'repository: https://github.com/test/test02',
# 					'repository: https://github.com/test/test03']

# Append licenses in the list
for elements in findall_Licenses:
    license_arr.append(elements[10:])
# print('package license:',license_arr)

for elements in findall_Urls:
    url_arr.append(elements)
# print(url_arr)

# Make a dict to store package name and license
packageLicense = {}
for i, value in enumerate(package_arr):
    packageLicense[value] = license_arr[i]

# Combination of the licenses' pairs
# print("The original dict is : " + str(packageLicense))
combinationResult = list(itertools.combinations(packageLicense, 2))
# print("The dictionary key pair list is : " + str(combinationResult))

def find_compatibility(combineres):
    """Finding license pairs' compatibility."""
    arr = []
    for value in combineres:
        for j in range(2):
            if j+1<2:
                first_license = packageLicense[value[j]]
                second_license = packageLicense[value[j+1]]
                first_package = value[j]
                second_package = value[j+1]
                try:
                    if first_license == 'BSD':
                        first_license = 'BSD-3-Clause'
                    if second_license == 'BSD':
                        second_license = 'BSD-3-Clause'
                    if first_license in ('Unknown','UNKNOWN'):
                        arr.append("We can't check the compatibility, because " +
                        first_package + " is unknown.")
                        break
                    if second_license in ('Unknown','UNKNOWN'):
                        arr.append("We can't check the compatibility, because " +
                        second_package + " is unknown.")
                        break
                    if licenses[first_license][second_license] == 'Yes':
                        arr.append("You can use " + first_license + '(' + first_package + ') '
                        + "and " + second_license +' (' + second_package + ').')
                    if licenses[first_license][second_license] == 'No':
                        arr.append("You can't use " + first_license +'('+ first_package + ') '
                        + "and " + second_license + ' (' + second_package + ').')
                except IOError:
                    arr.append("Can't detect the license.",
                    "The license is not the OSADL-matrix's list.")
                else:
                    print("The license detection is complete.")
    return arr
