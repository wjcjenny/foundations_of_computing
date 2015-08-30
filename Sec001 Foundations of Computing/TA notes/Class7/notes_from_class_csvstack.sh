# ROW-JOINING CSV'S

# In the Terminal,
cat part1.csv part2.csv part3.csv > joined.csv

cat joined.csv
# This leaves the headers in, which we do not want.


# Google "tools for working with csv's on the command line"
# Install csvkit: # a command line tool as well as a Python library
# Install anaconda (We already did).
conda install csvkit

# https://csvkit.readthedocs.org/en/0.9.1/scripts/csvstack.html
csvstack FILES part1.csv part2.csv part3.csv > joined.csv
# or rather
csvstack FILES part* > joined.csv

cat joind.csv