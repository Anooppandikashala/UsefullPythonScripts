import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
     
f = open("listedpkg.txt","w")
f.write(str(installed_packages_list))
f.close()
