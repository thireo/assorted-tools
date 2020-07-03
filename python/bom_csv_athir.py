#
# Example python script to generate a BOM from a KiCad generic netlist
#
# Example: Ungrouped (One component per row) CSV output
#

"""
    @package
    Generate a csv list file.
    Components are sorted by ref
    One component per line
    Fields are (if exist)
    Ref, Value, Footprint, Datasheet, Type,Manufacturer, Comment

    Command line:
    python "pathToFile/bom_csv_sorted_by_ref.py" "%I" "%O.csv"
"""

from __future__ import print_function

# Import the KiCad python helper module
import kicad_netlist_reader
import csv
import sys
import re

exvals = ["TestPoint"]

def excluded(exvals,component):
    returnval = True
    #net.excluded_values
    for val in exvals:
        #print(val)
        if(re.search(val,component.getValue())):
            #print(component.getValue())
            #print(component.getRef())
            returnval = False
    #print(returnval)
    return returnval
            
    
        

def myEqu(self, other):
    """myEqu is a more advanced equivalence function for components which is
    used by component grouping. Normal operation is to group components based
    on their Value and Footprint.

    In this example of a more advanced equivalency operator we also compare the
    custom fields Voltage, Tolerance and Manufacturer as well as the assigned
    footprint. If these fields are not used in some parts they will simply be
    ignored (they will match as both will be empty strings).

    """
    result = True
    if self.getValue() != other.getValue():
        result = False
    elif self.getPartName() != other.getPartName():
        result = False
    elif self.getFootprint() != other.getFootprint():
        result = False
    elif self.getField("Tolerance") != other.getField("Tolerance"):
        result = False
    #elif self.getField("Manufacturer") != other.getField("Manufacturer"):
    #    result = False
    elif self.getField("Voltage") != other.getField("Voltage"):
        result = False

    return result

kicad_netlist_reader.comp.__eq__ = myEqu
#kicad_netlist_reader.netlist().excluded_values.append("TestPoint")
# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write to, if the file cannot be opened output to stdout
# instead
try:
    f = open(sys.argv[2], 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print( __file__, ":", e, sys.stderr )
    f = sys.stdout

# Create a new csv writer object to use as the output formatter
out = csv.writer(f, lineterminator='\n', delimiter=',', quotechar="\"", quoting=csv.QUOTE_ALL)

# override csv.writer's writerow() to support utf8 encoding:
def writerow( acsvwriter, columns ):
    utf8row = []
    for col in columns:
        utf8row.append( str(col) )
    acsvwriter.writerow( utf8row )


#net.excluded_references.append(re.compile("TP[0-9]+]"))
#net.excluded_values.append(re.compile("TestPoint"))
#print(net.excluded_references)
components = net.getInterestingComponents()
grouped = net.groupComponents()
#for c in components:
    #print(c.getFieldNames())


#F 0 "C11" H 2965 4296 50  0000 L CNN
#F 1 "100nF 10V" H 2965 4205 50  0000 L CNN
#F 2 "Capacitor_SMD:C_0603_1608Metric" H 2888 4100 50  0001 C CNN
#F 3 "~" H 2850 4250 50  0001 C CNN
#F 4 "Ceramic X7R 10V" H 5550 3050 50  0001 C CNN "Type"
#F 5 "Top" H 5550 3050 50  0001 C CNN "Mounting"
#F 6 "-" H 5550 3050 50  0001 C CNN "Manufacturer"
#F 7 "-" H 5550 3050 50  0001 C CNN "Comment"


# Output a field delimited header line
writerow( out, ['Source:', net.getSource()] )
writerow( out, ['Date:', net.getDate()] )
writerow( out, ['Tool:', net.getTool()] )
writerow( out, ['Component Count:', len(components)] )
writerow( out, ['Ref', 'Quantity', 'Value', 'Footprint', 'Type','Tolerance','Voltage Rating','Mounted','Manufacturer', 'Comment', 'Datasheet'] )

for group in grouped:
    refs = ""
    for comp in group:
        if (len(refs) > 0):
            refs += ", "
        refs += comp.getRef()
        c = comp
        #print('\''+comp.getFootprint()+'\'')
    # Output all of the component information (One component per row)
    #for c in components:
    if(excluded(exvals,c    )):
        writerow( out, [refs, len(group), c.getValue(), c.getFootprint(), c.getField("Type"), c.getField('Tolerance'), c.getField('Voltage'), c.getField("Mounted"),c.getField("Manufacturer"), c.getField("Comment"), c.getDatasheet()])
    else:
        print(c.getValue())



