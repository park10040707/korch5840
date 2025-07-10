# multiprocessing을 사용함, 물리적으로 cpu 코어를 활용하여 병렬처리
import multiprocessing
import time as t

# 작업 5초
def long_task():
    for w in range(5):
        print(f"일하는 중...{w+1}")
        t.sleep(1)

if __name__ == "__main__":
    start = t.time()
    print("=====Start=====")
    processes = []
    for n in range(5):
        p = multiprocessing.Process(target=long_task)
        processes.append(p)    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("=====End=====")
    print(f"총 소요 시간: {t.time() - start:.2f}초")