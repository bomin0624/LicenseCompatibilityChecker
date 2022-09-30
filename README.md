# License Compatibility Checker

This is a tool that helps you check the compatibility of the licenses in your package.

# How to use
```
pip3 install matplotlib
pip3 install fpdf
https://github.com/bomin0624/LicenseCompatibilityChecker.git
```
# Change the path 

Go into get_license.py in the foo folder

```
os.chdir('CHANGE TO YOUR PATH')
```
In generate_report.py
```
CHARTPATH = 'YOUR IMAGE PATH'
```
# Run
```
python3 get_license.py
python3 generate_report.py
```
# System Design

![systemdesign](https://imgur.com/a8Xyy98.png)

# Result
<p>
After running generate_report.py, the system will generate a licensereport.pdf in your path.<br>

<div align=center><img width="500" height="600" src="https://imgur.com/UOXlALb.png"/> </div>

<div align=center><img width="500" height="600" src="https://imgur.com/HTERkqS.png"/> </div>

<div align=center><img width="900" height="450" src="https://imgur.com/kiYWCi2.png"/> </div>

</p>

# TODO:
- Using pycodestyle & pylint to do the code check
- Adding new feature

# Reference
- [license-checker](https://github.com/davglass/license-checker)
- [osadl-matrix](https://github.com/priv-kweihmann/osadl-matrix)
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/reference/FPDF/index.html)

# license
SPDX short identifier: BSD-3-Clause

Copyright <2022> <Chuang Po-Min (appppm31012@gmail.com)>

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Data license

The raw data of the OSADL Open Source License Checklists are licensed under the Creative Commons Attribution 4.0 International license (CC-BY-4.0), https://creativecommons.org/licenses/by/4.0/.

© 2017 - 2021 Open Source Automation Development Lab (OSADL) eG and contributors, info@osadl.org

Further information can be found [here](https://www.osadl.org/Access-to-raw-data.oss-compliance-raw-data-access.0.html)
A copy of the CC-BY-4.0 text can be found [here](LICENSE.ccby40)

# Contact 
Chuang Po-Min (appppm31012@gmail.com)
