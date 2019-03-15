

class my_string():
def __init__(self, input_string):
self.the_string = list(input_string)

def uppercase(self):
new = " "
for j in self.the_string:
if 65 <= ord(j) <= 90:
new = new + j
else:
new = new + str(chr(ord(j) - 32))
return new

def lowercase(self):
new = ""
for j in self.the_string:
if 97 <= ord(j) <= 122:
new = new + j
else:
new = new + str(chr(ord(j) + 32))
return new

def set_string(self, my_string):
self.the_string = my_string

def get_string(self):
return self.the_string

def set_char(self, pos, letter):
self.the_string[pos] = letter


name = my_string("Matt")

print(my_string.get_string(name))

print(my_string.lowercase(name))

print(my_string.uppercase(name))
