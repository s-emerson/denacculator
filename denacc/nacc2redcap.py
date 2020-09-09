#!/usr/bin/env python

###############################################################################
# Copyright 2020 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

import csv
import sys

from denacc import convert_field_list
from denacc import add_fields
from denacc import add_field_values


def rename_fields(file_input, err=sys.stderr):
    """ Adds ndv_ prefix and converts field labels to lower case """
    print("Beginning header renaming...", file=err)

    header = convert_field_list.convert_fields()
    reader = csv.DictReader(file_input, fieldnames=header)

    with open('renamed.csv', 'w', newline='') as renamed:
        writer = csv.DictWriter(renamed, fieldnames=reader.fieldnames)
        writer.writeheader()
        header_mapping = next(reader)
        writer.writerows(reader)


def delete_columns(err=sys.stderr):
    """ Deletes fields not present in REDCap project """

    with open('renamed.csv', 'r', encoding='utf-8') as renamed:
        reader = csv.DictReader(renamed)
        with open('delcols.csv', 'w', newline='') as delcols:
            fieldnames = add_fields.list_fields()
            writer = csv.DictWriter(delcols, fieldnames=fieldnames)
            writer.writeheader()
            print("Deleting extra columns...", file=err)
            for row in reader:
                new = delete_values(row)
                writer.writerow(new)


def delete_values(row):
    del row['ndv_visitnum']
    del row['ndv_naccmoca']
    del row['ndv_adgcexom']
    del row['ndv_ngdsgwas']
    del row['ndv_ngdsexom']
    del row['ndv_ngdswes']
    del row['ndv_ngdswgs']
    del row['ndv_ngdsgwac']
    del row['ndv_ngdsexac']
    del row['ndv_ngdsweac']
    del row['ndv_ngdswgac']
    del row['ndv_adgcexr']
    del row['ndv_naccspnl']
    del row['ndv_naccengl']
    del row['ndv_apreflan']
    del row['ndv_ayrspan']
    del row['ndv_ayrengl']
    del row['ndv_apcspan']
    del row['ndv_apcengl']
    del row['ndv_aspkspan']
    del row['ndv_areaspan']
    del row['ndv_awrispan']
    del row['ndv_aundspan']
    del row['ndv_aspkengl']
    del row['ndv_areaengl']
    del row['ndv_awriengl']
    del row['ndv_aundengl']
    return row


def add_columns(file_output, err=sys.stderr):
    """
    Adds ptid and redcap_event_name columns to beginning
    and nacc_derived_values_complete column to end
    """
    print("Adding columns...", file=err)

    with open('delcols.csv', 'r', encoding='utf-8') as delcols:
        reader = csv.DictReader(delcols)

        fieldnames = add_fields.list_fields()
        writer = csv.DictWriter(file_output, fieldnames=fieldnames)
        writer.writeheader()
        print("Filling new columns...", file=err)
        for row in reader:
            new = fill_extra_columns(row)
            writer.writerow(new)


def fill_extra_columns(row, err=sys.stderr):
    """
    Adds redcap_event_name value based on ndv_naccvnum
    """
    new = add_field_values.add_fields(row)

    if int(new['ndv_naccvnum']) == 1:
        new['redcap_event_name'] = "initial_visit_year_arm_1"
    elif int(new['ndv_naccvnum']) == 2:
        new['redcap_event_name'] = "followup_visit_yea_arm_1"
    elif int(new['ndv_naccvnum']) == 3:
        new['redcap_event_name'] = "followup_visit_yea_arm_1b"
    elif int(new['ndv_naccvnum']) == 4:
        new['redcap_event_name'] = "followup_visit_yea_arm_1c"
    elif int(new['ndv_naccvnum']) == 5:
        new['redcap_event_name'] = "followup_visit_yea_arm_1d"
    elif int(new['ndv_naccvnum']) == 6:
        new['redcap_event_name'] = "followup_visit_yea_arm_1e"
    elif int(new['ndv_naccvnum']) == 7:
        new['redcap_event_name'] = "followup_visit_yea_arm_1f"
    elif int(new['ndv_naccvnum']) == 8:
        new['redcap_event_name'] = "followup_visit_yea_arm_1g"
    elif int(new['ndv_naccvnum']) == 9:
        new['redcap_event_name'] = "followup_visit_yea_arm_1h"
    elif int(new['ndv_naccvnum']) == 10:
        new['redcap_event_name'] = "followup_visit_yea_arm_1i"
    elif int(new['ndv_naccvnum']) == 11:
        new['redcap_event_name'] = "followup_visit_yea_arm_1j"

    return new


def main():
    """
    Accepts a csv file as input, provides output to specified location
    """

    file_input = sys.stdin
    file_output = sys.stdout

    rename_fields(file_input)
    delete_columns()
    add_columns(file_output)
    print("Done!", file=sys.stderr)


if __name__ == '__main__':
    main()
