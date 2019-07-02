from compare_lib import *
import subprocess
import yaml
import os

def exec_command(cmd, cwd=None):
    #print('[cocotb-performance {}] {}'.format(cwd, cmd))
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    if proc.returncode == 0:
        return proc.stdout.decode('utf-8').split('\n')
    else:
        print(proc.stdout.decode('utf-8'))
        raise

def clone_repo(url, path):
    exec_command('git clone {} {}'.format(url, path))

def checkout_commit(path, commit):
    exec_command('git checkout ' + commit, cwd=path)

def fetch_and_checkout(path, commit):
    exec_command('git fetch origin', cwd=path)
    exec_command('git checkout ' + commit, cwd=path)
    branches = [os.path.basename(b) for b in exec_command('git branch -a', cwd=path)]
    if commit in branches:
        exec_command('git pull origin', cwd=path)

def runtest(path):
    os.environ['COCOTB'] = path
    exec_command('make -C oc_jpegencode/tb/ clean')
    return exec_command('make -C oc_jpegencode/tb/ TESTCASE=process_image_001')

def get_commits_since(path, since):
    return exec_command('git log --pretty=format:"%H" --since=\'{}\''.format(since), cwd=path)

def clone_and_update(url, commit, path):
    if not os.path.exists(path):
        clone_repo(url, path)
    fetch_and_checkout(path, commit)

def get_result(res, stdout):
    filter = res + ' : '
    line = [s  for s in stdout if filter in s][0]
    line = line.split(filter)[1]
    return line.split(' ')[0]

def get_summary(stdout):
    sim = get_result('SIM TIME', stdout)
    real = get_result('REAL TIME', stdout)
    perf = get_result('SIM / REAL TIME', stdout)
    return sim, real, perf

def get_commit_date(path):
    return exec_command('git show -s --format=%cd', cwd=path)[0]
    
        
        
    
