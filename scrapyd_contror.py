import requests



IP_PORT='127.0.0.1:6800'

def schedule(project_name,spider_name,job_id):
    url=f'http://{IP_PORT}/schedule.json'
    data={
        'project':project_name ,
         'job_id': job_id ,
        'spider':spider_name
    }
    r=requests.post(url, data=data)
    json_data=r.json()
    # print(json_data)


# def cancel(project_name, job_id):
#     """
#         停止 指定 项目名的 指定job id 的 项目
#     :param project_name: 项目名
#     :param job_id:  工作id
#     :return:
#     """
#     url = f'http://{ IP_PORT }/cancel.json'
#     data = {
#         'project': project_name,
#         'job': job_id
#     }
#
#     r = requests.post(url, data=data)
#
#     json_data = r.json()
#     # print(json_data)
#
#     return json_data

# def cancel_all(project_name):
#     """
#         停止当前正在运行的所有 项目
#     :return:
#     """
#
#     # 得到 当前所有 job 的json
#     json_data = listjobs(project_name)
#
#     # 得到 正在运行的 job 的列表
#     running_li = json_data['running']
#
#     # 遍历所有正在 running 的 job， 并且停止
#     for run in running_li:
#         r = cancel(project_name, run['id'])
#         print('停止：', r)

def listjobs(project_name):
    """
        获取当前所有的 job
    :param project_name: 项目名
    :return:  包含所有job的json对象
    """
    url = f'http://{ IP_PORT }/listjobs.json?project={ project_name }'

    r = requests.get(url)

    json_data = r.json()
    # print('listjobs：', json_data)
    return json_data

def daemonstatus():
    url=f'http://{IP_PORT}/daemonstatus.json'
    r=requests.get(url)
    json_data = r.json()
    print('daemonstatus：', json_data)
    return json_data

def listprojects():
    url=f'http://{IP_PORT}/listprojects.json'
    r = requests.get(url)
    json_data = r.json()
    print('listprojects：', json_data)
    return json_data

def listversions(project_name):
    url = f'http://{IP_PORT}/listversions.json?project={project_name}'
    r = requests.get(url)
    json_data = r.json()
    print('listversions：', json_data)
    return json_data

def listspiders(project_name):
    url=f'http://{IP_PORT}/listspiders.json?project={project_name}'
    r = requests.get(url)
    json_data = r.json()
    print('listspiders：', json_data)
    return json_data

def delversion(project_name,version):
    url = f'http://{IP_PORT}/delversion.json?project={project_name} -d version={version}'
    data={
        'project': project_name,
        'version':version
    }
    r = requests.post(url,data=data)
    json_data = r.json()
    print('delversion：', json_data)
    return json_data

def delproject(project_name):
    url = f'http://{IP_PORT}/delproject.json'
    data={
        'project': project_name
    }
    r = requests.post(url, data=data)
    json_data = r.json()
    print('delproject：', json_data)
    return json_data



if __name__=='__main__':
    project_name='hecanhui'
    spider_name='dingdian'
    job_id='1234'
    schedule(project_name,spider_name,job_id)
    # 停止所有正在运行的项目
    project_name = 'hecanhui'
    # cancel_all(project_name)
    daemonstatus()
    listprojects()
    listversions(project_name)
    listspiders(project_name)
    version=listversions(project_name)['version']
    #删除项目版本
    # delversion(project_name,version)
    #删除项目及版本
    # delproject(project_name)
