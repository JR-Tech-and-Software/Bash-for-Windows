'''
This file is under the MIT License.

Copyright 2019-2020 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
# The date command simply prints the current time and date to the screen
import time, tofile

def show(args):
    output = ""
    if((args[0] == "") or (args[0] == "-n") or (args[0] == ">") or (args[0] == ">>")):
        output = output + time.strftime("%a %d %b %Y %I:%M:%S %p %Z", time.localtime())
    elif(args[0] == "-m"):
        output = output + time.strftime("%a %d %b %Y %H:%M:%S %Z", time.localtime())
    else:
        output = output + "date: Shows the date and time\n"
        output = output + "Arguments:\n"
        output = output + "    NONE -n: Shows date and time in 12-hour format\n"
        output = output + "    -m     : Shows date and time in 24-hour format"
    tofile.write(args, output)