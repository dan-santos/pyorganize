import os


class Extensions:
    # lists of various file types
    image_exts = ['png', 'jpg', 'jpeg', 'gif', 'webp', 'tiff', 'psd', 'raw', 'bmp', 'heif', 'indd', 'svg', 'ai', 'eps']
    video_exts = ['mp4', 'mov', 'avi', 'webm', 'ogg', 'mpg', 'm4p', 'm4v', 'wmv', 'qt', 'flv', 'swf', 'avchd', 'mpeg']
    audio_exts = ['mp3', 'pcm', 'wav', 'aiff', 'acc', 'wma', 'flac', 'alac', 'axx', 'au', 'dfv', 'm4a', 'm4b', 'm4p', 'msv']
    document_exts = ['doc', 'docx', 'odt', 'txt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pps', 'pptx', 'html', 'htm', 'csv', 'xhtml']
    compressed_exts = ['zip', 'rar', 'tar.gz', '7z', 'arj', 'deb', 'pkg', 'rpm', 'z', 'tar', 'gz', 'bz2', 'apk', 'tgz', 'afa']
    code_exts = ['py', 'java', 'c', 'cpp', 'js', 'css', 'cs', 'h', 'pl', 'sh', 'swift', 'kt', 'vb', 'bat', 'php', 'rb', 'sql']

    # dictionary of extension types and their respective folders
    extensions_dict = {'Images': image_exts, 'Videos': video_exts, 'Audios': audio_exts,
                       'Documents': document_exts, 'Compressed': compressed_exts, 'Codes': code_exts, 'Other': list()}


class Organize:
    def create_folders(self, directory):
        print('---> Creating subfolders... DONE!')
        for folder in Extensions.extensions_dict.keys():
            tree = self.get_tree(directory, folder)
            if not os.path.isdir(tree):
                os.mkdir(tree)

    def get_tree(self, directory, file):
        tree = os.path.join(directory, file)
        return tree

    def get_extension(self, file):
        extension = str.lower(file.split('.')[-1])
        return extension

    def get_file_names(self, directory):
        file_names = os.listdir(directory)
        return file_names

    def get_right_folder(self, extension):
        for k, v in Extensions.extensions_dict.items():
            if extension in v:
                return k
        return 'Other'

    def move_file(self, origin_dir, destiny_dir, file):
        origin = self.get_tree(origin_dir, file)
        destiny = self.get_tree(self.get_tree(origin_dir, destiny_dir), file)
        try:
            os.rename(origin, destiny)
            print('---> Moved {} from "{}" to "{}".'.format(file, origin, destiny))
        except:
            print('---> Unexpected error when moving {} file from "{}" to "{}."\n'
                  '---> The program execution was interrupted.'.format(file, origin, destiny))
            exit()

    def verify_files_amount(self, directory):
        try:
            amount_files = len(next(os.walk(directory))[2])  # 0 = path, 1 = dirs, 2 = files
            if amount_files == 0:
                print('---> The "{}" folder has no files to organize.'.format(directory))
                exit()
            print('---> Checking files in folder "{}"... DONE!'.format(directory))
        except:
            print('---> Unexpected error when looking for the folder "{}".\n'
                  '---> The program execution was interrupted.'.format(directory))
            exit()

    def organize(self, directory):
        self.verify_files_amount(directory)
        file_names = self.get_file_names(directory)
        self.create_folders(directory)
        print('---> Moving files ...')

        for file in file_names:
            if os.path.isfile(self.get_tree(directory, file)):
                extension = self.get_extension(file)
                right_folder = self.get_right_folder(extension)
                self.move_file(directory, right_folder, file)

        return '---> Done! The "{}" folder now has all your {} files organized!'.format(directory, len(file_names))

if __name__ == '__main__':
    target_directory = str(input('Enter the folder name of that directory you want to organize: '))
    make = Organize()
    print(make.organize(target_directory))
