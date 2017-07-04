OpenStack Requirements
=======================

First, you have to ask your OpenStack administrator to create for you OpenStack project and credentials. Project should have at least following parameters:

Hardware Requirements
----------------------

+-----------+-------+------+---------+----------------+
| Instances | VCPUs | RAM  | Volumes | Volume Storage |
+-----------+-------+------+---------+----------------+
| 21        | 50    | 90GB | 48      | 1.2TB          |
+-----------+-------+------+---------+----------------+

Assign Floating IP and Create DNS Record
-----------------------------------------

To be allow access you Cloud Foundry instance from the outside OpenStack, you must have assigned Floating IP and create wildcard DNS record.

To get Floating IP , you can use script in ``bin/cfi-assign-floating-ip.py`` in the ``cloudfoundry-installation`` repository directory. But before you can run the script, you have to create configuration file ``clouds.yaml`` and place it into the right directory. In case that you are using Linux, the directory is ``~/.config/openstack``. So full path is ``~/.config/openstack/clouds.yaml``.

In case of macOS, the full path for ``clouds.yaml`` is ``~/Library/Application Support/openstack/clouds.yaml``.

The content of ``clouds.yaml`` should be as follows:

.. code:: yaml

   clouds:
       osinstancename:
           region_name: RegionOne
       auth:
           username: your_username
           password: XXXXXXX
           project_name: 'your_project_name'
           auth_url: 'https://openstack.yourdomain.com:5000/v2.0'

Of course, you have to change:

* **region_name**: In case that is different, than OpenStack default *RegionOne*
* **username**: OpenStack username
* **password**: OpenStack password
* **project_name**: OpenStack project name, provided by OpenStack administrator, that created project for you
* **auth_url**: URL to the OpenStack Keystone API 2.0 server



