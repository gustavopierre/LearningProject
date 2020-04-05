#!python3
'''
    backupToZip.py - Copia uma pasta toda e seu conteúdo para
    um arquivo ZIP cujo nome seja incrementado
'''
import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    # Cria o arquivo ZIP
    print('Creating %s...'%(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda a árvore de diretório e compacta os arquivos de cada pasta
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done!')

backupToZip('D:\\temp')