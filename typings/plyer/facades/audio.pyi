"""
This type stub file was generated by pyright.
"""

'''
Audio
=====

The :class:`Audio` is used for recording audio.

Default path for recording is set in platform implementation.

.. note::
        On Android the `RECORD_AUDIO`, `WAKE_LOCK` permissions are needed.

Simple Examples
---------------

To get the file path::

    >>> audio.file_path
    '/sdcard/testrecorder.3gp'

To set the file path::

    >>> import os
    >>> current_list = os.listdir('.')
    ['/sdcard/testrecorder.3gp', '/sdcard/testrecorder1.3gp',
    '/sdcard/testrecorder2.3gp', '/sdcard/testrecorder3.3gp']
    >>> file_path = current_list[2]
    >>> audio.file_path = file_path

To start recording::

    >>> from plyer import audio
    >>> audio.start()

To stop recording::

    >>> audio.stop()

To play recording::

    >>> audio.play()

Supported Platforms
-------------------
Android, Windows, macOS

'''
class Audio:
    '''
    Audio facade.
    '''
    state = ...
    _file_path = ...
    def __init__(self, file_path=...) -> None:
        ...
    
    def start(self): # -> None:
        '''
        Start record.
        '''
        ...
    
    def stop(self): # -> None:
        '''
        Stop record.
        '''
        ...
    
    def play(self): # -> None:
        '''
        Play current recording.
        '''
        ...
    
    @property
    def file_path(self): # -> str:
        ...
    
    @file_path.setter
    def file_path(self, location): # -> None:
        '''
        Location of the recording.
        '''
        ...
    


