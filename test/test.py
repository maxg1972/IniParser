from IniParser import IniParser

#create object
config = IniParser()

#read INI file
config.read('./test.ini')

#get 'days' from 'Backup' section and print it
days = config.def_getint('Backup','days',0)
print "[Backup]\n\rdays=%i" % days

#increment 'days', update 'Backup' section and save file
days += 1
config.put('Backup','days',days)
config.save('./test.ini')

#re-read INI file and print 'days' from 'Backup' section
config.read('./test.ini')
print "\n\r[Backup]\n\rdays=%i" % config.def_getint('Backup','days',-1)


