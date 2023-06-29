import os
import shutil
import subprocess

# ִ��cmd����
def exec(cmd):
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE  # �ض�������ֵ
    )
    proc.stdin.close()  # ��Ȼû�������д��ڣ��Ǿ͹ر�����
    result = proc.stdout.read()  # ��ȡcmdִ�е�����������byte���ͣ���Ҫdecode��
    proc.stdout.close()
    return result.decode(encoding="utf-8")

# �滻ͼ��
def replacePng(target,appName):
    # ������·���µ�ͼ��
    cmdRes = exec(f"find /home/king/android_src/mikrom12_gitlab/packages/ -name {target}")
    filePathList = cmdRes.split("\n")
    curpath=os.getcwd()
	# ���������ѵ��Ľ��
    for filepath in filePathList:
        if filepath=="":
            continue
        # Ϊ�˱�������Ӧ�õ�ͬ���ز�ͼ�꣬����ʹ��appName����һ��
        if appName not in filepath:
            continue
        print('Found file: ' + filepath)
        # �Ƚ��ļ����б���
        shutil.copy(filepath,filepath+".bak")
        # Ȼ�󽫵�ǰĿ¼׼���õ��滻�ļ����ƽ�ȥ
        replacePath=curpath+"/images/"+target
        # ������ļ������ڣ���������ļ����滻
        if os.path.exists(replacePath)==False:
            print("not found replace file:",replacePath)
            break
        shutil.copy(replacePath, filepath)

# ʹ�ñ��ݵ��ļ���ԭ��ͼ��
def unReplacePng(target):
    # ����Ŀ���ļ�
    cmdRes = exec(f"find /home/king/android_src/mikrom12_gitlab/frameworks/base/packages/ -name {target}")
    filePathList = cmdRes.split("\n")
    # �������н��
    for filepath in filePathList:
        if filepath=="":
            continue
        print('Found file: ' + filepath)
        # �����ļ�������ڣ����仹ԭ
        bakfile=filepath + ".bak"
        if os.path.exists(bakfile):
            shutil.copy(bakfile, filepath)
            print("unReplace file:",bakfile)

def main():
    # �滻Ϊ���ز�
    replacePng('ic_launcher_settings.png',"Setting")
    replacePng('ic_contacts_launcher.png',"Contacts")
    replacePng('ic_launcher_calendar.png',"Calendar")
	
    # ��ԭ�ز�
    # unReplacePng('ic_launcher_settings.png')
    # unReplacePng('ic_contacts_launcher.png')
    # unReplacePng('ic_launcher_calendar.png')

if __name__ == '__main__':
    main()
