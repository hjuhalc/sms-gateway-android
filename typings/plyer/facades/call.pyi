"""
This type stub file was generated by pyright.
"""

'''
Call
====

The :class:`Call` provides access to calling feature of your device.

.. note::
    - On Android your app needs the `CALL_PHONE` or `CALL_PRIVILEGED`
    permission in order to make calls.

    - Dialing call feature in not supported yet in iOS devices.

Simple Examples
---------------

To make call::

    >>> from plyer import call
    >>> tel = 9999222299
    >>> call.makecall(tel=tel)

To dial call::

    >>> call.dialcall()

Supported Platforms
-------------------
Android, iOS

'''
class Call:
    '''
    Call facade.
    '''
    def makecall(self, tel): # -> None:
        '''
        Make calls using your device.

        :param tel: The reciever
        :type tel: number
        '''
        ...
    
    def dialcall(self): # -> None:
        '''
        Opens dialing interface.
        '''
        ...
    


