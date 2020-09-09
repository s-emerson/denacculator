This program is meant to take a NACC Data Freeze .csv file and convert it into
a format that can be easily uploaded into the 1Florida Alzheimer's Disease
Research Center REDCap project, as the NACC Derived Values form.

NACC Data Freeze files are available at  http://www.alz.washington.edu/

To collect the csv file
---------------------
    -> ADCs
    -> Data Cores > Submission systems > UDS • FTLD • LBD
    -> Your center
    -> UDS • FTLD • LBD
    -> "Please click here to enter..."
    -> On the left sidebar: DOWNLOAD DATA > My Center's freeze data > Download CSV File
    -> Right click and select "Save as..."
    -> Make sure the file is saved with the .csv extension

Usage:

`$ denacc/nacc2redcap <$INPUT_FILE.csv >$OUTPUT_FILE.csv`

In which the output file will be placed in the specified filepath (default is
the denacculator top directory), ready to be uploaded as a REDCap data import.

The program's functionality is to:

 1) rename the header fields from the NACC format to REDCap's format,
 2) delete columns that 1Florida ADRC is not using in our NACC-Derived Values
   form,
 3) add columns to make the csv immediately REDCap importable ('ptid',
   'redcap_event_name', 'nacc_derived_values_complete')