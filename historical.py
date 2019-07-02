from compare_lib import *

if __name__ == '__main__':
    with open('historical.yml') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    url = config['url']
    path = config['path']
    since = config['since']

    if not os.path.exists(path):
        clone_repo(url, path)

    fetch_and_checkout(path, 'master')
    commits = get_commits_since(path, since)
    for c in commits:
        checkout_commit(path, c)
        date = get_commit_date(path)
        try:
            stdout = runtest(path)
            simtime, realtime, performance = get_summary(stdout)
            print("{},{},{},{},{}".format(date, c, simtime, realtime, performance))
        except:
            pass


    
    


