from conans import ConanFile, CMake
from conans.tools import download, unzip, replace_in_file
import os
import shutil

class TclapConan(ConanFile):
    name = "TCLAP"
    version = "1.2.2"
    settings = "os", "compiler", "build_type", "arch"
    license = "MIT"
    # No exports necessary

    def source(self):
        zip_name = "tclap-%s.tar.gz" % self.version
        download("http://downloads.sourceforge.net/project/tclap/" + zip_name + "?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Ftclap%2Ffiles%2F&ts=1466246416&use_mirror=tenet", zip_name)
        unzip(zip_name)
        # strip version from  folder name so it does not have to be used later
        shutil.move("tclap-%s" % self.version, "tclap")
        os.unlink(zip_name) 

    def package(self):
        self.copy("*.h", dst="include/tclap", src="tclap/include/tclap")
