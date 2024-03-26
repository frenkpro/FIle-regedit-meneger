import argparse
import os
import shutil
import winreg


def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            pass
    except Exception as e:
        print(f"Error creating file: {e}")
        exit(0)
    print("Succsess")


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"File {file_path} does not exist")
    except Exception as e:
        print(f"Error deleting file: {e}")
        exit(0)
    print("Succsess")


def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")
        exit(0)
    print("Succsess")


def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading from file: {e}")
        exit(0)
    print("Succsess")


def copy_file(src_path, dest_path):
    try:
        shutil.copy(src_path, dest_path)
    except Exception as e:
        print(f"Error copying file: {e}")
        exit(0)
    print("Succsess")


def rename_file(file_path, new_name):
    try:
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
    except Exception as e:
        print(f"Error renaming file: {e}")
        exit(0)
    print("Succsess")


def create_reg_key(chapter,key_path):
    try:
        if chapter=='CR':
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        elif chapter=='CU':
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        elif chapter=='LM':
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        elif chapter=='U':
            key = winreg.CreateKey(winreg.HKEY_USERS, key_path)
        elif chapter == 'CC':
            key = winreg.CreateKey(winreg.HKEY_CURRENT_CONFIG, key_path)
        else:
            print(f"Error creating registry key: Wrong chapter name")
            exit(0)
    except Exception as e:
        print(f"Error creating registry key: {e}")
        exit(0)
    print("Succsess")
    return key

def delete_reg_key(chapter,key_path):
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
    except FileNotFoundError:
        print(f"Key {key_path} does not exist")
    except Exception as e:
        print(f"Error deleting registry key: {e}")
        exit(0)
    print("Succsess")


def write_reg_value(chapter,key_path, value_name, value_data):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error writing registry value: {e}")
        exit(0)
    print("Succsess")


def parse_args():
    parser = argparse.ArgumentParser(description='File system and registry management')
    subparsers = parser.add_subparsers(dest='command')

    arg_parser = subparsers.add_parser('create_file', help='Create a file')
    arg_parser.add_argument('file_path', help='Path to the file')

    arg_parser = subparsers.add_parser('delete_file', help='Delete a file')
    arg_parser.add_argument('file_path', help='Path to the file')

    arg_parser = subparsers.add_parser('write_to_file', help='Write to a file')
    arg_parser.add_argument('file_path', help='Path to the file')
    arg_parser.add_argument('content', help='Content to write')

    arg_parser = subparsers.add_parser('read_from_file', help='Read from a file')
    arg_parser.add_argument('file_path', help='Path to the file')

    arg_parser = subparsers.add_parser('copy_file', help='Copy a file')
    arg_parser.add_argument('src_path', help='Path to the source file')
    arg_parser.add_argument('dest_path', help='Path to the destination file')

    arg_parser = subparsers.add_parser('rename_file', help='Rename a file')
    arg_parser.add_argument('file_path', help='Path to the file')
    arg_parser.add_argument('new_name', help='New name for the file')

    arg_parser = subparsers.add_parser('create_key', help='Create a registry key')
    arg_parser.add_argument('chapter', help='Сhapter of the regedit (CR/CU/LM/U/CC)')
    arg_parser.add_argument('key_path', help='Path to the key')

    arg_parser = subparsers.add_parser('delete_key', help='Delete a registry key')
    arg_parser.add_argument('chapter', help='Сhapter of the regedit (CR/CU/LM/U/CC)')
    arg_parser.add_argument('key_path', help='Path to the key')
    arg_parser.add_argument('chapter', help='Сhapter of the regedit (CR/CU/LM/U/CC)')


    arg_parser = subparsers.add_parser('write_value', help='Write a value to a registry key')
    arg_parser.add_argument('chapter', help='Сhapter of the regedit (CR/CU/LM/U/CC)')
    arg_parser.add_argument('key_path', help='Path to the key')
    arg_parser.add_argument('value_name', help='Name of the value')
    arg_parser.add_argument('value_data', help='Data to write', type= int)


    return parser.parse_args()


args = parse_args()

if args.command == 'create_file':
    create_file(args.file_path)
elif args.command == 'delete_file':
    delete_file(args.file_path)
elif args.command == 'write_to_file':
    write_to_file(args.file_path, args.content)
elif args.command == 'read_from_file':
    print(read_from_file(args.file_path))
elif args.command == 'copy_file':
    copy_file(args.src_path, args.dest_path)
elif args.command == 'rename_file':
    rename_file(args.file_path, args.new_name)
elif args.command == 'create_key':
    create_reg_key(args.chapter,args.key_path)
elif args.command == 'delete_key':
    delete_reg_key(args.chapter,args.key_path)
elif args.command == 'write_value':
    write_reg_value(args.chapter, args.key_path, args.value_name, args.value_data)