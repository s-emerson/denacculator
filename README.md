This program is meant to take a NACC Data Freeze .csv file and convert it into a format that can be easily uploaded into the 1Florida Alzheimer's Disease Research Center REDCap project, as the NACC Derived Values form.

NACC Data Freeze files are available at  http://www.alz.washington.edu/

-> ADCs
-> Data Cores > Submission systems > UDS • FTLD • LBD
-> Your center
-> UDS • FTLD • LBD
-> "Please click here to enter..."
-> On the left sidebar: DOWNLOAD DATA > My Center's freeze data > Download CSV File
-> Right click and select "Save as..."
-> Make sure the file is saved with the .csv extension

Usage:
`nacc/nacc2redcap <$INPUT_FILE.csv >$OUTPUT_FILE.csv`

In which the output file will be placed in the top denacculator folder, ready to be uploaded as a REDCap data import.