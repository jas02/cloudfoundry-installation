#!/usr/bin/env python
#
#  Copyright (C) 2017 Tieto Czech s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@tieto.com
#  http://www.tieto.com
#
#
#

import shade

shade.simple_logging()
cloud = shade.openstack_cloud(cloud='onecloud')

def get_floating_ip_address(cloud):
    """Get floating IP address"""
    cloud.create_floating_ip()

available_floating_ip = cloud.available_floating_ip()

if available_floating_ip:
    print available_floating_ip
else: 
    print "No floating IP address, getting one..."
    get_floating_ip_address(cloud)
    print available_floating_ip
