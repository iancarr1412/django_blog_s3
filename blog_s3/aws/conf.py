#sort out folders system - protect credentials

import datetime
AWS_ACCESS_KEY_ID = "AKIAI7DBRYA2HYID7GBQ"
AWS_SECRET_ACCESS_KEY = "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"

AWS_S3_CUSTOM_DOMAIN = 'd3b79r2ni01w5m.cloudfront.net'
AWS_S3_SECURE_URLS = True

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
DEFAULT_FILE_STORAGE = 'blog_s3.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'blog_s3.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-us-east-1-833621558754'
COMPRESS_STORAGE = 'posts.custom_storages.CachedS3BotoStorage'

AWS_IS_GZIPPED = True

S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % 'elasticbeanstalk-us-east-1-833621558754'
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % 'elasticbeanstalk-us-east-1-833621558754'
MEDIA_ROOT = MEDIA_URL
STATIC_URL = 'https://d3b79r2ni01w5m.cloudfront.net'

# COMPRESS_URL = STATIC_URL

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")
AWS_HEADERS = { 
'Expires': expires,
'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
AWS_DEFAULT_ACL = "public-read"
