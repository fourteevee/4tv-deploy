from sys import argv
from os import mkdir, walk
from tomli import load as toml_load
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
from pycdlib import PyCdlib

unit_objects = {}


class UnitConfiguration:
    def __init__(self, unit_number):
        self.unit_number = unit_number
        self.file_additions = []
        self.file_removals = []
        self.username = ""
        self.password = ""
        self.flags = {}

        self.generate_ssh_token()

    def generate_ssh_token(self):
        # Generate an ssh token for user here!
        pass

    def parse_global_configuration(self):
        # Check if config file provided matches the required format
        with open("./Data/global.toml", "rb") as config_file:
            config_data = toml_load(config_file)
            # Load data into instance vars here, looping for values with multiple items?

    def parse_unit_specific_configuration(self):
        # Check if config file provided matches the required format
        with open("./Data/unit-specific.toml", "rb") as config_file:
            config_data = toml_load(config_file)[self.unit_number]
            # Load data into instance vars here, looping for values with multiple items?

    def get_unit_number(self):
        return self.unit_number

    def get_file_additions(self):
        return self.file_additions

    def get_file_removals(self):
        return self.file_removals

    def get_credentials(self):
        return self.username, self.password

    def get_flags(self):
        return self.flags


with open("./Data/unit-specifc.toml", "rb") as config_file:
    units = toml_load(config_file).keys()
    for unit in units:
        unit_objects[unit] = UnitConfiguration(unit)


def main():
    try:
        extract_image(argv[1], "./Data/ImageContents")
    except FileNotFoundError:
        print("Error, file provided does not exist!")
        exit(1)
    except IndexError:
        print("Error, no file name provided!")
        exit(1)


def extract_image(image_name, output_location):
    image = PyCdlib()
    image.open(image_name)
    directories_to_create = []
    files_to_create = []
    for path, directory_list, file_list in image.walk(iso_path="/"):
        for directory in directory_list:
            directories_to_create.append(str(path + directory))
        for file in file_list:
            files_to_create.append(str(path + file))
    for directory in directories_to_create:
        mkdir(output_location + directory)
    for file in files_to_create:
        image.get_file_from_iso(output_location + file, iso_path=file)
    image.close()


def create_image(image_name: str, input_location):
    image_name = image_name.rstrip(".iso")
    for unit in unit_objects:
        image = PyCdlib()
        image.new()

        for path, directory_list, file_list in walk(input_location):
            for directory in directory_list:
                image.add_directory(path+directory)
            for file in file_list:
                image.add_file(file, path)

        # Do unit specific configurations here (i.e. for file in unit.get_file_removals())

        image.write(image_name + str(unit.get_unit_number()) + ".iso")
