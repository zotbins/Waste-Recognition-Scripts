# Data Directory
obj_dir = input("Directory: ")

# Get Number of Files in Directory
#file_list = [file for file in os.listdir(obj_dir)]
file_list = []
for file in os.listdir(obj_dir):
  if file.endswith(".jpg"):
    file_list.append(file)
num_files = len(file_list)
print("Number of files: ", num_files)

# Percentage of images to be used for the test set
percentage = 0.25;

# Get nth image as test
n_test = round(num_files/(num_files*percentage))

# Create and/or truncate train.txt and test.txt
train = open('train.txt', 'w')  
test = open('test.txt', 'w')

for i in enumerate(file_list):
    if(i[1].endswith(".jpg")):
        file_name = obj_dir + '/' + i[1] + '\n'
        text_version = file_name.replace(".jpg\n",".txt")
        if(os.path.exists(text_version)):          
          if i[0] % n_test == 0:
              test.write(file_name)
          else:
              train.write(file_name)
        else:
          print(file_name, "not found")

train.close()
test.close()
print("DONE")
