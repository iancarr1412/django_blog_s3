from os.path import splitext
from django. core. files. storage import get_storage_class
from storages. backends. s3boto import S3BotoStorage
 
 
class StaticToS3Storage(S3BotoStorage): 
	def __init__(self, *args, **kwargs): 
		super(StaticToS3Storage, self).__init __(*args, **kwargs) 
		self. local_storage = get_storage_class('compressor.storage .CompressorFi1eStorage) ()
		
	def save(self, name, content): 
        ext = splitext(name)[1]
        parent_dir = name.split('/')[0]
        if ext in ['css', 'js'] and not parent_dir == 'admin':
            self.local_storage._save(name, content)
        else:
            filename = super(StaticToS3Storage, self).save(name, content)
            return filename

class CachedS3BotoStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')()

    def save(self, filename, content):
        filename = super(CachedS3BotoStorage, self).save(filename, content)
        self.local_storage.save(filename, content)
        return filename