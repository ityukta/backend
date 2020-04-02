import os

base_path = "app3"
final_count = 0
def count_lines(file_path):
	print(f"Counting lines in file: {file_path}")
	count = 0
	if(file_path.endswith(".html") or file_path.endswith(".py") or file_path.endswith(".css") or file_path.endswith(".js")):
		with open(file_path, "r") as f:
			for line in f:
				count += 1
	return count

def count_folder_lines(dir_name):
	count = 0
	if(os.path.isfile(dir_name)):
		return count_lines(dir_name)
	else:
		for files in os.listdir(dir_name):
			count += count_folder_lines(os.path.join(dir_name, files))
	return count
print("\nTotal number of lines of code = ", count_folder_lines(base_path))