import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Check if the file 'add_item.json' exists, and load its content if it does
if path.exists('add_item.json'):
    my_list = load_from_json_file('add_item.json')
else:
    my_list = []

# Add command-line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to 'add_item.json'
save_to_json_file(my_list, 'add_item.json')
