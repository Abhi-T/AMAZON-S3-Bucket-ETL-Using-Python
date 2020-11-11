import requests
import csv
import json
import  boto3
from auth import ACCESS_KEY,SECRET_KEY
#refer below article to create access_key for s3 AWS
#https://medium.com/@shamnad.p.s/how-to-create-an-s3-bucket-and-aws-access-key-id-and-secret-access-key-for-accessing-it-5653b6e54337
'''  Fetch Current dateTime  '''

reqGet=requests.get("http://worldclockapi.com/api/json/est/now")

print(reqGet.text)
dict1=json.loads(reqGet.text) # converted to dictionary
print(type(dict1))

# for i,j in dict1.items():
#     # print(i)
#     if i == 'currentDateTime':
#         print(j)
#         csv_file = open('data.csv', 'w', newline='')
#         # writer = csv.writer(csv_file)
#         csv_file.write(i+","+j)
#         csv_file.close()

for i,j in dict1.items():
    # print(i)
    print(j)
    csv_file = open('data.csv', 'a', newline='')
    csv_file.write(i+","+str(j)+"\n")
    csv_file.close()

''' pushing data to S3 bucket'''
client=boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

client.create_bucket(Bucket='abhishek-data-engineering-csv-1.0')
with open("data.csv","rb") as f:
    client.upload_fileobj(f,"abhishek-data-engineering-csv-1.0","data.csv")

print("Upload Completed")



