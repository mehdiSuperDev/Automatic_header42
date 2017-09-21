#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import os
import sys
from time import *
import datetime as dt

#argv check
if len(sys.argv) != 3:
    sys.exit("Usage : " + os.path.basename(sys.argv[0]) + " 1)username 2)file.c(with absolute path)")

filename = sys.argv[2]

# create date ,username, mail, username and file_name
my_date = strftime("%Y/%m/%d")
my_hour = str(dt.datetime.now().time())[:-7]
username = sys.argv[1]
name_file = os.path.basename(sys.argv[2])
user_mail = "<" + username + "@student.42.fr>"

# header_42 line by line
line_border = "/* ".ljust(77, "*") + " */"
line_empty = "/* ".ljust(77, " ") + " */"
line_after_empty = "/* ".ljust(58) + ":::      ::::::::   */"
line_name_file = "/*   " + name_file.ljust(51, " ") + ":+:      :+:    :+:   */"
line_after_nm = "/* ".ljust(54) + "+:+ +:+         +:+     */"
line_user_mail = "/*   By: " + username + " " + user_mail + (
" " * (80 - (28 + len(username) + len(user_mail) + 10))) \
                 + "+#+  +:+       +#+        */"
line_after_user_mail = "/*".ljust(50, " ") + "+#+#+#+#+#+   +#+           */"
line_created_file = "/*   Created: " + my_date + " " + my_hour + " by " + username.ljust(18, " ") \
                    + "#+#    #+#             */"
line_updated_file = "/*   Updated: " + my_date + " " + my_hour + " by " + username.ljust(17, " ") \
                    + "###   ########.fr       */"

# create list with all lines in header_42
header42_list = (line_border, line_empty, line_after_empty, line_name_file, line_after_nm, line_user_mail, \
                 line_after_user_mail, line_created_file, line_updated_file, line_empty, line_border, "\n")

#read file
data = []
data.extend(header42_list)

try:
    with open(filename,"r") as f:
        data.extend(f.readlines())
except EnvironmentError:
    print('Fichier non trouvé')
    sys.exit()

#write file
with open(filename, "r+") as f:
    for line in data:
        f.write(line)
        f.write('\n')

print("Header(s) ajouté(s) avec succes")
