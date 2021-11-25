key = message['SourceObjectKey']
dest = message['DestinationBucket']

s3 = boto3.resource('s3')

copy_source = {
    'Bucket': source,
    'Key': key
}

dest_bucket = s3.Bucket(dest)

#if fails try dest instead of dest_bucket
s3.meta.client.copy(copy_source, dest, '1/business-operations-survey-2020-covid-19-csv.csv')
#dest_bucket.copy(copy_source, '1/business-operations-survey-2020-covid-19-csv.csv')

print('Single File is copied')

