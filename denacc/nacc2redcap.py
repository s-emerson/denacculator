#!/usr/bin/env python

###############################################################################
# Copyright 2020 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

# import argparse
import csv
import sys
# import traceback

from denacc import field_list
from denacc import add_field_list
from denacc import add_field_values


def rename_fields(file_input, err=sys.stderr):
    """ Adds ndv_ prefix and converts field labels to lower case """
    print("Beginning header renaming...", file=err)

    header = field_list.list_fields()
    reader = csv.DictReader(file_input, fieldnames=header)

    with open('renamed.csv', 'w', newline='') as renamed:
        writer = csv.DictWriter(renamed, fieldnames=reader.fieldnames)
        writer.writeheader()
        header_mapping = next(reader)
        writer.writerows(reader)


def add_columns(file_output, err=sys.stderr):
    """
    Adds ptid and redcap_event_name columns to beginning
    and nacc_derived_values_complete column to end
    """
    print("Adding columns...", file=err)

    renamed = open('renamed.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(renamed)

    with open('output.csv', 'w', newline='') as output:
        fieldnames = add_field_list.list_fields()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        print("Filling extra columns...", file=err)
        for row in reader:
            new = fill_extra_columns(row)
            writer.writerow(new)


def fill_extra_columns(row, err=sys.stderr):
    """
    Adds redcap_event_name value based on ndv_visitnum
    """
    new = add_field_values.add_fields(row)

    if int(new['ndv_visitnum']) == 1:
        new['redcap_event_name'] = "initial_visit_year_arm_1"
    elif int(new['ndv_visitnum']) == 2:
        new['redcap_event_name'] = "followup_visit_yea_arm_1"
    elif int(new['ndv_visitnum']) == 3:
        new['redcap_event_name'] = "followup_visit_yea_arm_1b"
    elif int(new['ndv_visitnum']) == 4:
        new['redcap_event_name'] = "followup_visit_yea_arm_1c"
    elif int(new['ndv_visitnum']) == 5:
        new['redcap_event_name'] = "followup_visit_yea_arm_1d"
    elif int(new['ndv_visitnum']) == 6:
        new['redcap_event_name'] = "followup_visit_yea_arm_1e"
    elif int(new['ndv_visitnum']) == 7:
        new['redcap_event_name'] = "followup_visit_yea_arm_1f"
    elif int(new['ndv_visitnum']) == 8:
        new['redcap_event_name'] = "followup_visit_yea_arm_1g"
    elif int(new['ndv_visitnum']) == 9:
        new['redcap_event_name'] = "followup_visit_yea_arm_1h"
    elif int(new['ndv_visitnum']) == 10:
        new['redcap_event_name'] = "followup_visit_yea_arm_1i"
    elif int(new['ndv_visitnum']) == 11:
        new['redcap_event_name'] = "followup_visit_yea_arm_1j"

    return new


def main():
    """
    Accepts a csv file as input, provides output to specified location
    """

    file_input = sys.stdin
    file_output = sys.stdout

    rename_fields(file_input)
    add_columns(file_output)


if __name__ == '__main__':
    main()
