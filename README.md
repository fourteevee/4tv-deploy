Setup information:

Config folder:
    - Contains the configuration files for the application. There are two
    special files in this folder: `__default__.toml` and `__global__.toml`. 
    - The `__default__.toml` file is used as a template to start from when
    creating a new configuration file. The `__global__.toml` file is used to
    store global configuration options that are used by all units. The
    `__default__.toml` file is not used by the application directly.
    - Any new configuration files are named after the unit they are used for. 
    For instance, `1.toml` would indicate a unit called "1". The unit names
    can be anything, but they must be unique.
    - The configuration files are in the TOML format. You can omit any values
    that are not needed. The application will either use sensible defaults or
    ignore the value if it is not needed.
    - The image generator applies the configs in this order: `__global__.toml`,
    then the unit's specific config file. This means that any values in the
    unit's config file will override the global values.

Data folder:
    - Contains the data files for the application. The folders are intended to
    be used for different types of data. Here is the breakdown:
        - `Debian Packages` - Contains any .deb files that are needed for the
        unit. These will be installed on the unit when the image is generated.
        - `Network Interfaces` - Contains any network configuration files
        that are needed for the unit. These will be copied to the unit and 
        applied when the image is generated. These files are in the standard
        format for network configuration files made for use with systemd.
        - `Services` - Contains any systemd service files that are needed for
        the unit. These will be copied to the unit and applied when the image
        is generated.
        - `Static Files` - Contains any files that are needed for the unit.
        These will be copied to the unit and applied when the image is 
        generated. The files can be loose or in folders, but the folder must
        be specified when writing the unit specific config file. For instance,
        if you have a file called `test.txt` in the `Static Files/Scripts` 
        folder, your entry in the configuration file would look like:
        `static_files = ["Scripts/test.txt": "/home/pi/Scripts/test.txt"]`.
        - `Dynamic Files` - TODO
        - `Templates` - TODO
        - `Users` - TODO
        - `Groups` - TODO
