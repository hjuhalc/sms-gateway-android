"""
This type stub file was generated by pyright.
"""

'''
Orientation
==========

The :class:`Orientation` provides access to public methods to set orientation
of your device.

.. note::
    These settings are generally guidelines, the operating
    system may choose to ignore them, or they may be overridden by
    other system components.

.. versionadded:: 1.2.4

Simple Examples
---------------

To set landscape::

    >>> from plyer import orientation
    >>> orientation.set_landscape()

To set portrait::

    >>> orientation.set_portrait()

To set sensor::

    >>> orientation.set_sensor()

Supported Platforms
-------------------
Android, Linux

'''
class Orientation:
    '''
    Orientation facade.
    '''
    def set_landscape(self, reverse=...): # -> None:
        '''
        Rotate the app to a landscape orientation.

        :param reverse: If True, uses the opposite of the natural
                        orientation.
        '''
        ...
    
    def set_portrait(self, reverse=...): # -> None:
        '''
        Rotate the app to a portrait orientation.

        :param reverse: If True, uses the opposite of the natural
                        orientation.
        '''
        ...
    
    def set_sensor(self, mode=...): # -> None:
        '''
        Rotate freely following sensor information from the device.

        :param mode: The rotation mode, should be one of 'any' (rotate
                     to any orientation), 'landscape' (choose nearest
                     landscape mode) or 'portrait' (choose nearest
                     portrait mode). Defaults to 'any'.
        '''
        ...
    


