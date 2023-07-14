import os, signal, sys, json
from time import time

#variables
subfolders = []
files = []
inaccesable_folders = []
cnt = 0
tardir = False
tarfile = False
update_database = False
searchin = "."
exit = False

if(len(sys.argv) == 1):
	tardir = "any"
else:
	for i in sys.argv[1:]:
		if(i == "-update"):
			update_database = True
		elif(i[0:2] == "s-"):
			searchin = i[2:]
		elif(i[0:2] == "d-"):
			if(len(i) > 2):
				tardir = i[2:]
			else:
				tardir = "any"
		if(i[0:2] == "f-"):
			if(len(i) > 2):
				tarfile = i[2:]
			else:
				tarfile = "any"

# extract file/folder name
def extract(path, return_path=False):
	record_until = len(path)
	for i in range(len(path)-1, 0, -1):
		if(path[i] == "/"):
			if(return_path):
				return path[:record_until]
			else:
				return path[record_until:]
		else:
			record_until -= 1
	return "."

# handle intrupt
def handle_intrrupt(signum, frame):
	global exit
	exit = True

signal.signal(signal.SIGINT, handle_intrrupt)

# replace unsupported character with _us_
def replace_unsupported_char(S):
	newS = ""
	unsupported_char = "$;()&`-@_#^[]{}'~,!=+ "
	for i in S:
		if(i in unsupported_char):
			newS += "_us_"
		else:
			newS += i
	return newS

# search folder
def List_Folders(target, path="."):
	global cnt, exit
	for f in os.listdir(path):
		if(exit):
			return
		d = os.path.join(path, f)
		if(os.access(d, os.R_OK)):
			if(os.path.isdir(d)):
				if(d.endswith(target) or target == "any"):
					cnt += 1
					print(str(cnt)+": "+d[1:])	
					subfolders.append(d[2:])
				tempd = replace_unsupported_char(d)
				msg = "Searching_for: "+target+" Found: "+str(cnt)+" Inaccesable_Folders: "+str(len(inaccesable_folders))+" Searching_in: "+tempd
				os.system("~/findit/./run.sh display "+msg)
				List_Folders(target, d)
		else:
			inaccesable_folders.append(d)

# search file
def List_Files(target, path="."):
	global cnt, exit
	for f in os.listdir(path):
		if(exit):
			return
		d = os.path.join(path, f)
		if(os.path.isfile(d)):
			if(d.endswith(target) or target == "any"):
				cnt += 1
				print(str(cnt)+":", d[1:])
				files.append(d[2:])
		tempd = replace_unsupported_char(d)
		msg = "Searching_for: "+target+" Found: "+str(cnt)+" Inaccesable_Folders: "+str(len(inaccesable_folders))+" Searching_in: "+tempd
		os.system("~/findit/./run.sh display "+msg)
		if(os.path.isdir(d)):
			List_Files(target, d)

# data base update
def update(target, path="."):
	pass

# Initialize folder search
if(tardir):
	os.system("~/findit/./run.sh display Searching_for: dir-"+tardir+" Found: 0 Inaccesable_Folders: 0 Searching_in: ")
	start_time = time()
	List_Folders(target=tardir, path=searchin)
	print("\n\nFound:", len(subfolders))
	total_time = time()-start_time
	unit = ":S"
	print(total_time)
	if(total_time < 0.001):
		total_time *= 1000
		unit = ":MS"
	elif(total_time > 59):
		total_time /= 60
		unit = ":M"
	print("\nTotal time:", str(total_time)+unit)
	os.system("tput cnorm")
	if(len(subfolders)):
		navdir = int(input("\nEnter a number to navigate to the dir or 0 to exit:"))
		if(navdir > 0):
			os.chdir(subfolders[navdir-1])
	os.system("~/findit/./run.sh clear")

# Initialize file search
cnt = 0
if(tarfile):
	os.system("~/findit/./run.sh display Searching_for: file-"+tarfile+" Found: 0 Inaccesable_Folders: 0 Searching_in: ")
	start_time = time()
	List_Files(target=tarfile, path=searchin)
	print("\n\nFound:", len(files))
	total_time = time()-start_time
	unit = ":S"
	print(total_time)
	if(total_time < 0.001):
		total_time *= 1000
		unit = ":MS"
	elif(total_time > 59):
		total_time /= 60
		unit = ":M"
	print("\nTotal time:", str(total_time)+unit)
	os.system("tput cnorm")
	if(len(files)):
		navfile = int(input("\nEnter a number to navigate to the file dir or 0 to exit:"))
		if(navfile != "" and navfile > 0):
			while(navfile > len(files) or navfile <= 0):
				navfile = int(input("Enter a valid number to navigate:"))
				if(navfile == ""):
					os.system("~/findit/.run.sh clear")
			os.chdir(extract(files[navfile-1], True))
	os.system("~/findit/./run.sh clear")

# initalize data base update
if(update_database):
	pass
