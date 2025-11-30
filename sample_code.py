# from dask import delayed
# import dask
# import time
# from dask.distributed import Client, LocalCluster
# # from dask.highlevelgraph import HighLevelGraph
#
# @delayed
# def task_a(no):
#     time.sleep(10)
#     return no
#
#
# @delayed
# def task_b(no):
#     time.sleep(10)
#     return no
#
#
# @delayed
# def task_c(no):
#     time.sleep(10)
#     return no
#
#
# @delayed
# def task_d(no):
#     time.sleep(10)
#     return no
#
#
# @delayed
# def combine(nos):
#     time.sleep(10)
#     return nos
#
#
# def run_pipe():
#     clu = LocalCluster()
#     client = Client(clu)
#     print(f"Cluster running on {clu.dashboard_link}")
#
#     with dask.annotate(task_group="Grp 1"):
#         a = task_a(3)
#         b = task_b(4)
#
#     with dask.annotate(task_group="Grp 2"):
#         c = task_c(b)
#     # d = task_d(c)
#     with dask.annotate(task_group="Final"):
#         e = combine([c,  a])
#
#     print(e.layers)
#
#     result = client.compute(e)
#     print(client.gather(result))
#
#
# if __name__ == '__main__':
#     run_pipe()


from dask import delayed
import dask
import time
from dask.distributed import Client, LocalCluster


@delayed(name="Task_a")
def task_a(no):
    time.sleep(10)
    return no

@delayed(name="Task_b")
def task_b(no):
    time.sleep(10)
    return no

@delayed(name="Task_c")
def task_c(no):
    time.sleep(10)
    return no

@delayed(name="Task_d")
def combine(nos):
    time.sleep(10)
    return nos


def run_pipe():
    clu = LocalCluster()
    client = Client(clu)
    print(f"Cluster running on {clu.dashboard_link}")

    with dask.annotate(label="Grp 1"):
        a = task_a(3)
        b = task_b(4)

    with dask.annotate(label="Grp 2"):
        c = task_c(b)

    with dask.annotate(label="Final"):
        e = combine([c, a])

    result = client.compute(e)
    print(client.gather(result))


if __name__ == '__main__':
    run_pipe()
