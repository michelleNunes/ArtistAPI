import boto3
from services.constants import APIConstants


class DynamoLib(object):
    try:
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ArtistInformation')
        if table is None:
            # Create the DynamoDB table.
            table = dynamodb.create_table(
                TableName='ArtistInformation',
                KeySchema=[
                    {
                        'AttributeName': 'Artist_name',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'Artist_name',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )

            # Wait until the table exists.
            table.meta.client.get_waiter('table_exists').wait(TableName='users')

            # Print out some data about the table.
            print(table.item_count)
    except ():
        print("Fail in create table")

    @staticmethod
    def create_item(uuid_info, artist_name, artist_information):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ArtistInformation')
        info = artist_information[artist_name][APIConstants.SONGS]
        table.put_item(
            Item={
                'ArtistID': uuid_info,
                'Artist_name': str(artist_name),
                'Artist_songs': str(info),
            })

    @staticmethod
    def delete_item(artist_name):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ArtistInformation')
        table.delete_item(
            Key={
                'Artist_name': str(artist_name),
            }
        )