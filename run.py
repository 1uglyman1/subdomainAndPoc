import subprocess
import os

def run_dddd(domain):
    try:
        command = f'./dddd -t {domain} -ho {domain}.html'
        subprocess.run(command, shell=True, check=True)
        print("run_dddd 扫描任务执行成功")
    except subprocess.CalledProcessError as e:
        print(f"执行 run_dddd 扫描任务时出错: {e}")
        return False
    return True
def set_chmode():
    os.system("chmod +x dddd")
if __name__ == '__main__':
    set_chmode()
    with open('url.txt','r') as file:
        for f in file:
            run_dddd(f.strip())
        file.close()
    print("+++++++++++++ run over +++++++++++++")
