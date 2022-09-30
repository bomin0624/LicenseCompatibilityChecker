"""License Compatibility Checker - Generate report function."""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from PIL import Image
from pdf import PDF
import get_license as gl

licenseCount = []
licensePrecentage = []
license_type = set(gl.license_arr)
findCompatibility = gl.find_compatibility(gl.combinationResult)

for license_element in license_type:
    MAXNUM = 0
    MAXNUM = max(gl.license_arr.count(license_element),MAXNUM)
    licenseCount.append(gl.license_arr.count(license_element))

# License number chart
x = np.arange(len(license_type))
plt.subplot(2, 2, 1)
plt.bar(x, licenseCount, color=['blue'])
plt.xticks(x, list(license_type),fontsize= 5)
plt.xlabel('License name', fontsize= 7)
plt.ylabel('License numbers',fontsize=7)
plt.title('The Numbers of the License', fontsize=7)

# Counting precentage
total = sum(licenseCount)
for i, element in enumerate(licenseCount):
    element = element/total
    licensePrecentage.append(element)

# License Precentage chart
cmap = cm.jet(np.linspace(0, 1, len(license_type)))
plt.subplot(2, 2, 2)
plt.barh(x, licensePrecentage, color=cmap)
plt.yticks(x, list(license_type),fontsize=5)
# plt.ylabel('License name', fontsize=7)
plt.xlabel('License Precentage', fontsize=7)
plt.title('The Precentage of the license', fontsize=7)
fig = plt.gcf()
fig.set_size_inches(10, 5)
plt.savefig('licenseChart.png')
# plt.show()



# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 14)
pdf.cell(0, 10, "Installed package: ", 0, 1)

for i, element in enumerate(gl.package_arr):
    pdf.cell(0, 10, str(i+1)+ ".", 0, 1)
    pdf.cell(5)
    pdf.cell(0, 10, "package name: "+ element, 0, 1)
    pdf.cell(5)
    pdf.cell(0, 10, "license name: "+ gl.license_arr[i], 0, 1)
    pdf.cell(5)
    pdf.cell(0, 10, gl.url_arr[i], 0, 1)
pdf.cell(0, 10, "Compatibility Testing Results:", 0, 1)
pdf.cell(5)
for i,element in enumerate(findCompatibility):
    pdf.cell(5)
    if 'cannot' in element:
        pdf.set_text_color(255,0,0)
    else:
        pdf.set_text_color(0,0,0)
    pdf.cell(0, 10, element, 0, 1)
    pdf.cell(5)
    pdf.set_text_color(0,0,0)

# Open the chart path
CHARTPATH = '/Users/bomin/Desktop/communication-project/license_checker/foo/licenseChart.png'
cover = Image.open(CHARTPATH)
width, height = cover.size
width, height = float(width * 0.264583), float(height * 0.264583)
imagePosition = 25+len(gl.package_arr)*60+len(findCompatibility)*20
if imagePosition > 210:
    pdf.add_page()
pdf.image('licenseChart.png', 0, 30, width-len(gl.license_arr)*6, height-10)
pdf.output('licensereport.pdf', 'F')
