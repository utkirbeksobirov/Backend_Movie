from django.conf import settings

# Boto3 paketini import qilib olish
import boto3

# Sizning AWS ma'lumotlaringiz
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = settings.AWS_S3_REGION_NAME

# S3 bucket nomini va regionni yaratish
s3_bucket = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

# Boto3 clientini yaratish
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME,
)

# Imzolangan URL olish uchun funksiya
# def generate_presigned_url(object_name, expiration=3600):
#     """Amazon S3 da fayl uchun imzolangan URL generatsiya qilish"""
#     url = s3_client.generate_presigned_url(
#         ClientMethod='get_object',
#         Params={'Bucket': AWS_STORAGE_BUCKET_NAME, 'Key': object_name},
#         ExpiresIn=expiration,
#     )
#     return url

# Fayl URLini generatsiya qilish
def get_file_url(object_name):
    """Amazon S3 da fayl uchun imzolangan URL generatsiya qilish"""
    url = f"https://{s3_bucket}/{object_name}"
    return url


DEFAULT_FILE_STORAGE = "core.cdn.backends.MediaRootS3Boto3Storages"
STATICFILES_STORAGE = "core.cdn.backends.StaticRootS3Boto3Storages"