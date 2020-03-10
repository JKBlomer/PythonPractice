import csv
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
from urllib.parse import urlparse
from time import sleep
import calendar
import sys

test = False
stars = []
missingStars = []
f1 = open("test_star_output.txt", "w+") if test else open("star_output.txt", "w+")
f2 = open("test_stars_found.txt", "w+") if test else open("stars_found.txt", "w+")
f3 = open("test_stars_missing.txt", "w+") if test else open("stars_missing.txt", "w+")

def main():
	# import actors from csv, pass to scraper, create star
	file = 'sample_actors.csv' if test else 'female_actors_list.csv'
	with open(file) as actor_file:
		csv_reader = csv.reader(actor_file, delimiter=',')
		line_count = 0
		ourStar = True
		for row in csv_reader:
			
			if row[0] != "":
			
				
				col1 = row[0].split()
				col2 = row[1].split()
				
				
				# scraped = scrapeSite(col2)
				scraped = scrapeSite(row)
				
				if scraped != None:
					social = getSocial(scraped["social"])
					bio = getBio(scraped["bio"])
					createStar(row, social, bio)
			
			
			line_count += 1
			sleep(1) if test else sleep(3)
			


def createStar(name, social, bio):
	star = {}
	n, s, b = name, social, bio
	
	if len(n) == 2:
		f, l, two = n[0], n[1], True
	else:
		f, m, l, two = n[0], n[1], n[2], False
		
	star["name"] = f + " " + l if two else f + " " + m + " " + l
	key = star["name"].replace(" ", "-").lower()
	star["aliases"] = [f + " " + l] if two else [star["name"]]
	star["birthday"] = b["birthday"]
	star["hair_color"] = b["hair_color"]
	star["ethnicity"] = b["ethnicity"]
	star["eye_color"] = b["eye_color"]
	star["height"] = b["height"]
	star["weight"] = b["weight"]
	star["measurements"] = b["measurements"]
	star["profile_url_hd"] = "roku/stars/hd/" + key + "-856x1224.jpg"
	star["profile_url_sd"] = "roku/stars/sd/" + key + "-214x306.jpg"
	star["biography"] = {
		"twitter": s["twitter"]
	}
	star["key"] = key
	stars.append(star)
	for a in star:
		if a != "key":
			print(star[a], end=';', file=f1)
		else:
			print(star[a], end='\n', file=f1)
	f2.write(star["name"] + ",")


#scaper func
def scrapeSite(name):
	n = name
	if len(n) == 2:
		name = n[0] + "_" + n[1]
	else:
		name = n[0] + "_" + n[1] + "_" + n[2]
	
	url = 'https://www.babepedia.com/babe/' + name
	
	response = requests.get(url)
	
	if re.search("%", response.url) == None:
		sys.stdout.write(name + " found - gathering details\n")
		sys.stdout.flush()
		soup = BeautifulSoup(response.content, 'html.parser')
		if soup.find("div", id="socialicons") != None:
			social = soup.find("div", id="socialicons").find(href=re.compile("https://twitter.com"))
		else:
			return None
		if soup.find("div", id="bioarea") != None:
			bio1 = soup.find("div", id="bioarea").ul.find_all("li")
			bio = []
			for line in bio1:
				bio.append(line)
			
		else:
			return None
		return {"social": social, "bio": bio}
	else:
		missingStars.append(name)
		f3.write(name.replace("_", " ") + ",")
		sys.stdout.write(name + " not found - skipping\n")
		return None


def getSocial(social):
	if social != None:
		twitTag = urlparse(social["href"]).path.replace("/", "@")
		return {"twitter": twitTag}
	else:
		return {"twitter": ""}


def getBio(bio):
	measure = ""
	# declare default values
	
	birthday, hair_color, ethnicity, eye_color, height, weight, measurements = "","","","","","",""
	for line in bio:
		if line.contents:
			a, b = line.contents[0].string, line.contents[1]
			if a == "Born:":
				# get day
				ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
				ords = [ordinal(n) for n in range(1,32)]
				for d, o in enumerate(ords):
					if re.search(o, b) != None:
						day = d + 1
				# get month
				for v, k in enumerate(calendar.month_name):
					if re.search(k, b) != None and v != 0:
						month = v
				# get year
				year = b[len(b) - 4:len(b)]
				birthday = str(month) + "/" + str(day) + "/" + str(year)
			elif a == "Hair color:": hair_color = b[1:len(b)]
			elif a == "Ethnicity:": ethnicity = b[1:len(b)]
			elif a == "Eye color:":	eye_color = b[1:len(b)]
			elif a == "Height:":
				r = re.search('"', b).start() + 1
				height = b[1:r]
			elif a == "Weight:":
				r = re.search('lbs', b).start()
				weight = b[1:r - 1]
			elif a == "Measurements:":
				measure = b
			elif a == "Bra/cup size:":
				# if no letter in measure, add from bra/cup size
				if re.search("[A-Za-z]", measure) == None:
					r = re.search("[A-Za-z]", b).start()
					measurements = measure[1:3] + b[r] + measure[3:]
				else:
					measurements = measure[1:len(measure)]
	return {
		"birthday": birthday,
		"hair_color": hair_color,
		"ethnicity": ethnicity,
		"eye_color": eye_color,
		"height": height,
		"weight": weight,
		"measurements": measurements
	}



main()

# f1 = open("star_output.txt", "w+")

# for star in stars:
# 	for a in star:
# 		if a != "key":
# 			print(star[a], end=';', file=fo)
# 		else:
# 			print(star[a], end='\n', file=fo)



# for star in stars:
# 	for a in star:
# 		print(a, star[a])
# 		print("\n\n")

# f2 = open("stars_found.txt", "w+")
# for star in stars:
# 	f2.write(star["name"] + ",")

# f3 = open("stars_missing.txt", "w+")
# for star in missingStars:
# 	f3.write(star + ",")

f1.close()
f2.close()
f3.close()
print("COMPLETE")