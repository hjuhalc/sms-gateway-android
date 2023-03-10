"""
This type stub file was generated by pyright.
"""

'''
Storage Path
============

The StorgePath API can be used to gain access to standard storage locations
across platforms such as home directory, root directory, external storage
directory, documents, downloads, etc.

The :class:`StoragePath` provides access to public methods to access standard
storage locations.

Simple Examples
---------------

To get the path of user's home directory::

    >>> from plyer import storagepath
    >>> storagepath.get_home_dir()

To get the path of standard downloads directory::

    >>> from plyer import storagepath
    >>> storagepath.get_downloads_dir()

To get the path of directory holding application files::

    >>> from plyer import storagepath
    >>> storagepath.get_application_dir()

'''
class StoragePath:
    '''
    StoragePath facade.
    '''
    def get_home_dir(self):
        '''
        Get the path of home directory of current user.
        '''
        ...
    
    def get_external_storage_dir(self):
        '''
        Get the path of primary shared or external storage directory.
        '''
        ...
    
    def get_sdcard_dir(self):
        '''
        Get the path of external SD card.

        .. versionadded:: 1.4.0
        '''
        ...
    
    def get_root_dir(self):
        '''
        Get the path of root of the "system" partition holding the core OS.
        '''
        ...
    
    def get_documents_dir(self):
        '''
        Get the path of standard directory in which to place documents that
        have been created by the user.
        '''
        ...
    
    def get_downloads_dir(self):
        '''
        Get the path of standard directory in which to place files that have
        been downloaded by the user.
        '''
        ...
    
    def get_videos_dir(self):
        '''
        Get the path of standard directory in which to place videos that are
        available to the user.
        '''
        ...
    
    def get_music_dir(self):
        '''
        Get the path of standard directory in which to place any audio files
        that should be in the regular list of music for the user.
        '''
        ...
    
    def get_pictures_dir(self):
        '''
        Standard directory in which to place pictures that are available to
        the user.
        '''
        ...
    
    def get_application_dir(self):
        '''
        Get the path of the directory holding application files.
        '''
        ...
    


