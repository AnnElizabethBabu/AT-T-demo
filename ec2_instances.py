#!/usr/bin/python
import boto3
import csv
import os

f = open('ec2_instances.csv', 'a')
print("------*** List of EC2 instances ***-------", file=f)

ec2client = boto3.client('ec2')
ec2_instance = ec2client.describe_instances()
for reservations in ec2_instance["Reservations"]:
	for instances in reservations["Instances"]:
		print ("Instance_ID:" + instances['InstanceId'], file=f)
		try:
			for tags in instances['Tags']:
				print (tags, file=f)
					
		except Exception as e:
			continue