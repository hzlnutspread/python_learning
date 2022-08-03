import requests
import time

# use this method if you know exactly where your information is. Take the time to find it. This is faster.
api_url = "https://api.theprawns.xyz/api/v1/projects"

def get_project_list(api_url):
    response = requests.get(api_url)
    response = response.json()
    project_list = []
    for projects in response['data']:
        if not projects['collectionObject']['twitter_username']:
            pass
        else:
            project_list.append(projects['collectionObject']['twitter_username'])
    print(set(project_list))

if __name__ == '__main__':
    start_time = time.time()
    get_project_list(api_url)
    print("--- '%.5f' seconds ---" % (time.time() - start_time))

# -------------------------------------------------------------------------------------------

# use this method if you don't know exactly where your information is. Will find anything. Slower though.
def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


if __name__ == '__main__':
    start_time = time.time()
    response = requests.get(api_url)
    response = response.json()
    output = gen_dict_extract('twitter_username', response)
    project_list = []
    for i in output:
        project_list.append(i)
    print(set(project_list))
    print("--- '%.5f' seconds ---" % (time.time() - start_time))