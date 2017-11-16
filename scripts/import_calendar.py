import os, sys
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_website.settings')

# 
import csv
import re
from datetime import datetime






import django
django.setup()
from core.models import ClassPeriod, Reading, Event

NOW = datetime.today()
OLD_SITE = open('old.html', 'r')

def update_from_gcal():
	"""
	Attempts to pull from HCI gcal(ics) that was converted to csv
	"""
	with open('HCI_calendar.csv', 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			d = datetime.strptime(row['DTEND'],'%m/%d/%Y %H:%M %p')
			title = row['SUMMARY']
			if NOW.year == d.year:
				try:
					ClassPeriod.objects.create(date=d, title=title)
				except Exception as e:
					pass




def update_from_old():
	"""
	attempts to salvage reading links from old HCI website
	"""
	soup = BeautifulSoup(OLD_SITE.read(), 'html.parser')

	for h3 in soup.find(id='class_periods').find_all('h3')[1:-1]:
		d = h3.text[-11:].strip(" ()")

		# Website is horribly formatted, try to get as much as posible by filtering by date
		try:
			d = datetime.strptime(d,'%m/%d/%Y')
		except Exception as e:
			continue

		# Create a new class_period object
		cp = ClassPeriod.objects.create(
			date=d
			,title=h3.text[:-11].strip('()')
		)

		# Find the list of reading / events / 
		ul = h3.nextSibling
		while ul and ul.name != 'ul':
			ul = ul.nextSibling


		# find links inside of list
		if ul:
			for li in ul.find_all('li'):
				for a in li.find_all('a'):
					if 'slides' in a.text:
						cp.url = a.attrs['href']
					else:
						r = Reading.objects.create(class_period=cp, title=a.text, url=a.attrs['href'])
						r.save()
		cp.save()

	

