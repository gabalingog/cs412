# File: models.py
# Author: Gab Alingog (galingog@bu.edu), 11/01/2026
# Description: Models of the application

from django.db import models
from datetime import datetime

# Create your models here.

class Voter(models.Model):
    '''Data from newton_voters.csv'''

    voted_id = models.TextField()
    last_name = models.TextField()
    first_name = models.TextField()
    street_num = models.TextField()
    street_name = models.TextField()
    street_apt_num = models.TextField(blank=True)
    street_zip_code = models.TextField()
    date_of_birth = models.DateField()
    date_of_regis = models.DateField()
    party_affiliation = models.CharField(max_length=2)
    precinct_num = models.CharField(max_length=4)
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    voter_score = models.IntegerField()

    def __str__(self):
        '''String representation of the attributes'''
        return f'{self.first_name} {self.last_name} ({self.street_num} {self.street_name}) Precinct: {self.precinct_num} Party: {self.party_affiliation}'
    
def load_data():
    '''Load from the cvs'''

    Voter.objects.all().delete()
    filename = '/Users/gabalingog/Downloads/newton_voters.csv'
    f = open(filename, 'r')
    f.readline()

    for line in f:
        try:
            fields = line.strip().split(',')
            voter = Voter(voted_id = fields[0],
                          last_name = fields[1],
                          first_name = fields[2],
                          street_num = fields[3],
                          street_name = fields[4],
                          street_apt_num = fields[5],
                          street_zip_code = fields[6],
                          date_of_birth = fields[7],
                          date_of_regis = fields[8],
                          party_affiliation = fields[9],
                          precinct_num = fields[10],

                          v20state = (fields[11].strip().upper() == 'TRUE'),
                          v21town = (fields[12].strip().upper() == 'TRUE'),
                          v21primary = (fields[13].strip().upper() == 'TRUE'),
                          v22general = (fields[14].strip().upper() == 'TRUE'),
                          v23town = (fields[15].strip().upper() == 'TRUE'),

                          voter_score = fields[16],
                        )
            voter.save()
            print(f'Created voter: {voter}')
        except:
            print("Wrong.")
            print(f"line={line}")
    print(f"Created {len(Voter.objects.all())} Voters")