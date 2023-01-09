def get(): 
    # env = ConfigParser()
    # env.read('.ini', encoding='utf8')
    Home_Cloud_Path = "C:\\Users\\MEDAC\\Desktop\\" 
    #env.get('PATH','HOME_CLOUD_STORAGE')

    import os
    from os import path

    data = {}
    data['files'] = []
    data['directories'] = []
                
    for f in os.listdir(Home_Cloud_Path):
        if path.isdir(Home_Cloud_Path+f):
            data['directories'].append(f)
        if path.isfile(Home_Cloud_Path+f):
            data['files'].append(f)
    
    return data


