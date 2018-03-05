import pip
print('Import')
def install(package):
	pip.main(['install', package])

# Example
if __name__ == '__main__':

	print('main')
	install('termcolor')
	install('boto3')
	install('pymysql')