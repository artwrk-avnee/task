import boto3

#using an existing table
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Test_Profile')

print(table.creation_date_time)
#creating an new item
table.put_item(
   Item={
        'Artist_Id': 1,
        'ArtwrkTitle': 'actor',
        'Artist_Name': 'Shahid Kapoor'
        
    }
)
#getting an item 
response = table.get_item(
    Key={
        'Artist_Id': 3,
        'ArtwrkTitle': 'painting'
        
    }
)
item = response['Item']
print(item)

#updating an item
table.update_item(
    Key={
        'Artist_Id': 1,
        'ArtwrkTitle': 'actor'
    },
    UpdateExpression='SET Artist_Name = :val1',
    ExpressionAttributeValues={
        ':val1': 'Salman'
    }
)

#deleting an item
table.delete_item(
    Key={
        'Artist_Id': 3,
        'ArtwrkTitle': 'painting'
    }
)