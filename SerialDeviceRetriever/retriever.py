
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Olivier Devauchelle 2022


from serial.tools import list_ports

def list_devices( port_name = None ) :
    '''
    devices = list_devices( port_name = None )
    '''

    if port_name is None :
        port_name = [ 'tty', 'COM', 'cu' ]

    elif type(port_name) == type('') :
        port_name = [ port_name ]

    devices = []

    for port_name in port_name :

        for port in list_ports.grep( port_name ):

            devices += [ port.__dict__ ]

    return devices


def show_devices( port_name = None ) :
    '''
    show_devices( port_name = None )
    '''

    devices = list_devices( port_name = port_name )

    for device in devices :

        for key, value in device.items() :
            print( key, ' = ', value )

        print('\n')


def find_devices( port_name = None, strict = False, **id ) :
    '''
    devices = find_devices( port_name = None, strict = False, **id )
    '''

    devices = []

    for device in list_devices( port_name = port_name ) :

        keep = True

        for key, value in id.items() :

            if value is None :
                value = ''

            try :

                if strict :
                    keep *= ( value == device[ key ] )

                else :
                    keep *= ( value in device[ key ] )

            except :
                keep = False
                break

        if keep :
            devices += [ device ]

    return devices


if __name__ == '__main__' :

    show_devices()
    print( find_devices( manufacturer = 'Arduino') )
    print( find_devices( serial_number = '85935333337351D04041', strict = True ) )
