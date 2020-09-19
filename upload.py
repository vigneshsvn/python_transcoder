from google.cloud import storage

# Setting credentials using the downloaded JSON file
client = storage.Client.from_service_account_json(json_credentials_path='presales.json')

# Creating bucket object
bucket = client.get_bucket('viki_trans_py')

# Name of the object to be stored in the bucket
object_name_in_gcs_bucket = bucket.blob('sample.mp4')

# Name of the object in local file system
object_name_in_gcs_bucket.upload_from_filename('sample.mp4')