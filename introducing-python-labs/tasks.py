from invoke import task

@task
def mytime(any_argument):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print(time_str)