"""
    Make a list of the last x photos based and sorted by
    the filename
"""
# Begin customization -------------------------------------

QUANTITY = 10
SOURCE_DIR=u'~/test/photos'
YEARS = xrange(2009, 2014) #exclude last
DESTINATION_DIR=u'~/test/photos/2014/12 - Dezembro/'

# End customization ---------------------------------------
# ---------------------------------------------------------
import os
from shutil import copy2
from pprint import pprint
#__debug__ = True

years_paths = [ os.path.realpath(os.path.expanduser(os.path.join(SOURCE_DIR, str(year)))) for year in YEARS ]
years_paths.sort(reverse=True)
def fullpath(item, item2):
    return os.path.join(item, item2)

def get_last_photos(quantity):
    _LAST_X_PHOTOS = []
    for year_path in years_paths:
        for root, dirs, files in os.walk(year_path):
            dirs.sort(reverse=True)
            files.sort(reverse=True)
            already_added = len(_LAST_X_PHOTOS)
            if __debug__: print(root, len(files), len(_LAST_X_PHOTOS))
            if already_added < quantity:
                _LAST_X_PHOTOS.extend(files[:quantity-already_added])
                _path = [root]*len(_LAST_X_PHOTOS)
                _LAST_X_PHOTOS = map(fullpath, _path, _LAST_X_PHOTOS)
            else:
                break
    return _LAST_X_PHOTOS

if __name__ == '__main__':
    photos_origin = get_last_photos(QUANTITY)
    photos_destination = map(os.path.basename, photos_origin)
    photos_destination = map(os.path.join, [os.path.expanduser(DESTINATION_DIR)]*len(photos_destination), photos_destination)
    pprint(photos_destination)

    _existing_photos = os.listdir(os.path.expanduser(DESTINATION_DIR))[:10]
    existing_photos = map(os.path.join, [os.path.expanduser(DESTINATION_DIR)]*len(_existing_photos), _existing_photos)
    pprint(existing_photos)

    pprint(set(photos_destination) - set(existing_photos))
    map(copy2, photos_origin, photos_destination)