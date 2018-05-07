import os



dev = open("key_dev.txt")
test = open("key_test.txt")
train = open("key_train.txt")


lines_dev = dev.readlines()
lines_test = test.readlines()
lines_train = train.readlines()

config_file = "opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf"
out_file = "out.csv"
os.system("rm out*")
"""
out_csv_file = "dev_features.csv"
#>> to continue writing
os.system("touch " + out_csv_file)
for i in range(len(lines_dev)):
	if(lines_dev[i] != '\n'):

		line = lines_dev[i].split(' ')
		wav_file = "data/dev/" + line[0] + ".wav"
		os.system("./opensmile-2.3.0/inst/bin/SMILExtract -C " + config_file + " -I " + wav_file + " -O " + out_file)
out = open(out_file, 'r')
out_lines = out.readlines()
for i in range(len(out_lines)):
	if(out_lines[i] != "\n" and not "@" in out_lines[i]):
		os.system("echo \'" + out_lines[i][10:-3] + "\' >> " + out_csv_file)



out_file = "out.txt"
os.system("rm out*")
out_csv_file = "train_features.csv"
#>> to continue writing
os.system("touch " + out_csv_file)
for i in range(len(lines_train)):
	if(lines_train[i] != '\n'):

		line = lines_train[i].split(' ')
		wav_file = "data/train/" + line[0] + ".wav"
		os.system("./opensmile-2.3.0/inst/bin/SMILExtract -C " + config_file + " -I " + wav_file + " -O " + out_file)
out = open(out_file, 'r')
out_lines = out.readlines()
for i in range(len(out_lines)):
	if(out_lines[i] != "\n" and not "@" in out_lines[i]):
		os.system("echo \'" + out_lines[i][10:-3] + "\' >> " + out_csv_file)

"""

out_file = "out.txt"
os.system("rm out*")
out_csv_file = "test_features.csv"
#>> to continue writing
os.system("touch " + out_csv_file)
for i in range(len(lines_test)):
	if(lines_test[i] != '\n'):
		line = lines_test[i].split('\n')
		wav_file = "data/test/" + line[0] + ".wav"
		os.system("./opensmile-2.3.0/inst/bin/SMILExtract -C " + config_file + " -I " + wav_file + " -O " + out_file)
out = open(out_file, 'r')
out_lines = out.readlines()
for i in range(len(out_lines)):
	if(out_lines[i] != "\n" and not "@" in out_lines[i]):
		os.system("echo \'" + out_lines[i][10:-3] + "\' >> " + out_csv_file)
