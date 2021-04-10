Welcome to NetManager
=====================

NetManager is an advanced, feature-rich, and easy-to-use web interface for managing IT Infrastructure.

**Features:**

- Built using the newest technology ``Python 3.9``\/``HTML5``\/``CSS3``\/``Django-Rest-Framework``
- Dark themed web interface
- Full powershell capabilities
- Limitless customization for all scripts and modules
- Object Oriented designed for efficiency
- Optimised for speed without compromise of reliability or security

Getting Started
---------------
First time looking at NetManager? If so, this is a good place to start.

- **First Steps:** :doc:`introduction`
- **Quick Start** :doc:`quickstart`
- **Logging** :doc:`logging`

.. toctree::
   :maxdepth: 2
   introduction

Getting Help
------------
Having issues? If so, check out the resources below:

- :doc:`faq`
- :ref:`index <genindex>` or :ref:`searching <search>`
- Report bugs in the `Issue Tracker <https://github.com/AustinRJakusz/Net-Manager/issues>`_
- Ask in our GitHub `Discussions Page <https://github.com/AustinRJakusz/TestDocs/discussions>`_


Attributes
----------
address_width: Optional[int]
    32-bit OS will result in ``32`` and 64-bit OS will result in ``64``
architecture: Optional[int]
    +---------------+--------------+
    | Integer Value | Architecture |
    +===============+==============+
    | 0             | x86          |
    +---------------+--------------+
    | 1             | MIPS         |
    +---------------+--------------+
    | 2             | Alpha        |
    +---------------+--------------+
    | 3             | PowerPC      |
    +---------------+--------------+
    | 5             | ARM          |
    +---------------+--------------+
    | 6             | ia64         |
    +---------------+--------------+
    | 9             | x64          |
    +---------------+--------------+
asset_tag: Optional[str]
    represents the asset tag of this processor
availability: Optional[int]
    +---------------+-----------------------------+
    | Integer Value | Availability                |
    +===============+=============================+
    | 1             | Other                       |
    +---------------+-----------------------------+
    | 2             | Unknown                     |
    +---------------+-----------------------------+
    | 3             | Running or Full Power       |
    +---------------+-----------------------------+
    | 4             | Warning                     |
    +---------------+-----------------------------+
    | 5             | In Test                     |
    +---------------+-----------------------------+
    | 6             | Not Applicable              |
    +---------------+-----------------------------+
    | 7             | Power Off                   |
    +---------------+-----------------------------+
    | 8             | Off Line                    |
    +---------------+-----------------------------+
    | 9             | Off Duty                    |
    +---------------+-----------------------------+
    | 10            | Degraded                    |
    +---------------+-----------------------------+
    | 11            | Not Installed               |
    +---------------+-----------------------------+
    | 12            | Install Error               |
    +---------------+-----------------------------+
    | 13            | Power Save - Unknown        |
    +---------------+-----------------------------+
    | 14            | Power Save - Low Power Mode |
    +---------------+-----------------------------+
    | 15            | Power Save - Standby        |
    +---------------+-----------------------------+
    | 16            | Power Cycle                 |
    +---------------+-----------------------------+
    | 17            | Power Save - Warning        |
    +---------------+-----------------------------+
    | 18            | Paused                      |
    +---------------+-----------------------------+
    | 19            | Not Ready                   |
    +---------------+-----------------------------+
    | 20            | Not Configured              |
    +---------------+-----------------------------+
    | 21            | Quiesced                    |
    +---------------+-----------------------------+
caption: Optional[str]
    short description of the object
characteristics: Optional[int]
    defines which functions the processor supports
config_manager_error_code: Optional[int]
    +---------------+----------------------------------------------------------------------+
    | Integer Value | Description                                                          |
    +===============+======================================================================+
    | 0             | This device is working properly                                      |
    +---------------+----------------------------------------------------------------------+
    | 1             | This device is not configured correctly                              |
    +---------------+----------------------------------------------------------------------+
    | 2             | Windows cannot load the driver for this device                       |
    +---------------+----------------------------------------------------------------------+
    | 3             | The driver for this device might be corrupted, or your system may be |
    |               | running low on memory or other resources                             |
    +---------------+----------------------------------------------------------------------+
    | 4             | This device is not working properly. One of its drivers or your      |
    |               | registry might be corrupted                                          |
    +---------------+----------------------------------------------------------------------+
    | 5             | The driver for this device needs a resource that Windows cannot      |
    |               | manage                                                               |
    +---------------+----------------------------------------------------------------------+
    | 6             | The boot configuration for this device conflicts with other devices  |
    +---------------+----------------------------------------------------------------------+
    | 7             | Cannot filter                                                        |
    +---------------+----------------------------------------------------------------------+
    | 8             | The driver loader for the device is missing                          |
    +---------------+----------------------------------------------------------------------+
    | 9             | This device is not working properly because the controlling firmware |
    |               | is reporting the resources for the device incorrectly                |
    +---------------+----------------------------------------------------------------------+
    | 10            | This device cannot start                                             |
    +---------------+----------------------------------------------------------------------+
    | 11            | This device failed                                                   |
    +---------------+----------------------------------------------------------------------+
    | 12            | This device cannot find enough free resources that it can use        |
    +---------------+----------------------------------------------------------------------+
    | 13            | Windows cannot verify this device's resources.                       |
    +---------------+----------------------------------------------------------------------+
    | 14            | This device cannot work properly until you restart your computer.    |
    +---------------+----------------------------------------------------------------------+
    | 15            | This device is not working properly because there is probably a      |
    |               | re-enumeration problem                                               |
    +---------------+----------------------------------------------------------------------+
    | 16            | Windows cannot identify all the resources this device uses           |
    +---------------+----------------------------------------------------------------------+
    | 17            | This device is asking for an unknown resource type                   |
    +---------------+----------------------------------------------------------------------+
    | 18            | Reinstall the drivers for this device                                |
    +---------------+----------------------------------------------------------------------+
    | 19            | Failure using the VxD loader                                         |
    +---------------+----------------------------------------------------------------------+
    | 20            | Your registry might be corrupted                                     |
    +---------------+----------------------------------------------------------------------+
    | 21            | System failure: Try changing the driver for this device. If that     |
    |               | does not work, see your hardware documentation. Windows is removing  |
    |               | this device                                                          |
    +---------------+----------------------------------------------------------------------+
    | 22            | This device is disabled                                              |
    +---------------+----------------------------------------------------------------------+
    | 23            | System failure: Try changing the driver for this device. If that     |
    |               | doesn't work, see your hardware documentation                        |
    +---------------+----------------------------------------------------------------------+
    | 24            | This device is not present, is not working properly, or does not     |
    |               | have all its drivers installed                                       |
    +---------------+----------------------------------------------------------------------+
    | 25            | Windows is still setting up this device                              |
    +---------------+----------------------------------------------------------------------+
    | 26            | Windows is still setting up this device                              |
    +---------------+----------------------------------------------------------------------+
    | 27            | This device does not have valid log configuration                    |
    +---------------+----------------------------------------------------------------------+
    | 28            | The drivers for this device are not installed                        |
    +---------------+----------------------------------------------------------------------+
    | 29            | This device is disabled because the firmware of the device did not   |
    |               | give it the required resources                                       |
    +---------------+----------------------------------------------------------------------+
    | 30            | This device is using an Interrupt Request (IRQ) resource that        |
    |               | another device is using                                              |
    +---------------+----------------------------------------------------------------------+
    | 31            | This device is not working properly because Windows cannot load the  |
    |               | drivers required for this device                                     |
    +---------------+----------------------------------------------------------------------+
config_manager_user_config: Optional[bool]
    If True, the device is using a configuration that the user defines.
cpu_status: Optional[bool]
    +---------------+--------------------------------------------+
    | Integer Value | Status                                     |
    +===============+============================================+
    | 0             | Unknown                                    |
    +---------------+--------------------------------------------+
    | 1             | CPU Enabled                                |
    +---------------+--------------------------------------------+
    | 2             | CPU Disabled by User via BIOS Setup        |
    +---------------+--------------------------------------------+
    | 3             | CPU Disabled by BIOS (POST ERROR)          |
    +---------------+--------------------------------------------+
    | 4             | CPU is Idle                                |
    +---------------+--------------------------------------------+
    | 5             | Reserved                                   |
    +---------------+--------------------------------------------+
    | 6             | Reserved                                   |
    +---------------+--------------------------------------------+
    | 7             | Other                                      |
    +---------------+--------------------------------------------+