from git import Repo
import shutil

file=open('/root/config.txt',"r")
lines=file.readlines()


folder_list=['api','osal','usdm','inline','build_system','adf_ctl','cryptodev','adf','sal','sample_code']
branch_list=['api','osal','usdm','inline','build-system','adf-ctl','cryptodev','adf','sal','sample-code']
branch_name=[]
for line in lines:
    line= line.strip()
    spl=line.split("=")
    branch_name.append(spl[1])


base_local=input("Enter the directory path :")


i=0
for i in range(10):

    base_addr="git@github.com:intel-sandbox/applications.devops.software-core-tools.staging.qat."
    common="common."
    if i==0:
        common="api."

    githubpath=base_addr+common+branch_list[i]+".git"
    localpath=base_local+folder_list[i]
    if branch_list[i]=="inline" or branch_list[i]=="cryptodev":
        continue
    else:
        Repo.clone_from(githubpath, localpath, single_branch=True, b=branch_name[i])

