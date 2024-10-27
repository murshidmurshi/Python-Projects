#Once you opened file it's necessary to close the file
#if any Error in that, you can close the file by using finally statement
#No matter what Error its close the file


def process_file():
    try:
        f = open('D:\\pycharm_practise\\final_sment')
        x = 1 /0
    except Exception as e:
        print('inside exception')
    finally:
        print('closed file')
        f.close()

process_file()