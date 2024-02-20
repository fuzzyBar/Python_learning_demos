import shutil
import zipfile
import os

def unzip_and_rename(folder_path):
    '''
    Display thumbnails containing only pictures or single-layer
    folder compressed packages. Set the first picture as a thumbnail
    and rename the compressed package name.Work in the directory
    where the script file is located.
    '''
    #main work
    for item in os.listdir(folder_path,):
        
        item_path = os.path.join(folder_path, item)
        
        if zipfile.is_zipfile(item_path):
            # create a zipFile
            myZip = zipfile.ZipFile(item_path, metadata_encoding = 'gbk')
            # get the name of zipFile
            myZipName = os.path.splitext(item)[0]

            #extract 2 type of zipFiles
            if myZip.infolist()[0].filename[-1] == '/' :
                newfile = myZip.extract(myZip.infolist()[1].filename)
            else:
                newfile = myZip.extract(myZip.infolist()[0].filename)
            # rename them
            ends = os.path.splitext( newfile )[1]
            old_path = newfile
            new_path = os.path.join(folder_path, myZipName+ends)
            os.rename(old_path, new_path)
            myZip.close()

    
    #clear empty folders
    for item in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path, item)
        if os.path.isdir(old_file_path):
            try:
                shutil.rmtree(old_file_path)
            except OSError as e:
                print(f"Error: {e.filename} - {e.strerror}.")
    
current_dir = os.getcwd()
unzip_and_rename(current_dir)











