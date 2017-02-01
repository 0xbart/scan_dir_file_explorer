from dirtools import Dir

path = '/Users/Bart/Downloads/Crimediggers/Lara/output'

d = Dir(path, exclude_file='.gitignore')

files = d.files()
for file in files:
	print file
