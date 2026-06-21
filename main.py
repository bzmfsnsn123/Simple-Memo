import os
File_Name="todo.txt"
def init_file():
    if not os.path.exists(File_Name):
        with open(File_Name,"w",encoding="utf-8") as f:
            pass

def get_todo_list():
    todo_list=[]
    with open(File_Name,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            item=line.strip()
            if item:
               todo_list.append(item)
    return todo_list

def add_todo():
    content=input("请输入要添加的的待办事").strip()
    if not content:
        print("内容不能为空哦")
        return
    with open(File_Name,"a",encoding="utf-8") as f:
        f.write(content+"\n")
    print("✅添加成功！")

def show_todo_list():
    todo_list=get_todo_list()
    if len(todo_list)==0:
        print("📮暂无待办事件")
        return
    print("\n=====我的备忘录=====")
    for index,item in enumerate(todo_list,start=1):
        print(f"{index}.{item}")
        print("=======================\n")

def del_todo():
    todo_list=get_todo_list()
    show_todo_list()
    if len(todo_list)==0:
        return
    try:
        num=int(input("请输入要删除的序号:"))
        if 1<=num<=len(todo_list):
            del todo_list[num-1]
            with open(File_Name,"w",encoding="utf-8") as f:
                for item in todo_list:
                    f.write(item+"\n")
            print("🗑️删除成功")
        else:
            print("序号超出范围")

    except ValueError:
        print("输入错误❌，请输入数字序号☺️")

def main():
    init_file()
    while True:
        print("""===========备忘录菜单============
 1. 添加待办事项
 2. 查看所有待办
 3. 删除待办事项
 4. 退出程序
 =================================""")
        choice=input("请输入数字选择功能：")
        if choice=="1":
            add_todo()
        elif choice=="2":
            show_todo_list()
        elif choice=="3":
            del_todo()
        elif choice=="4":
            print("👋程序退出，数据已保存，下次再见！")
            break
        else:
            print("输入无效😑，请输入1-4的数字！")

if __name__=="__main__":
    main()


