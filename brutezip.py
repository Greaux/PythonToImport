import zipfile


def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
	zipfilename = '123.zip'
	dictionary = 'dictionary.txt'

	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
				break
			except:
				pass
	print password

if __name__ == '__main__':
	main()
