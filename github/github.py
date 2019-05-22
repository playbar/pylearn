from git import Repo

# 在文件夹里新建一个仓库，如果已存在git仓库也不报错不覆盖没问题
# repo = git.Repo.init(path='文件夹地址')
# 选择已有仓库
# repo = git.Repo( '仓库地址' )
# 克隆仓库
# repo = git.Repo.clone_from(url='git@github.com:USER/REPO.git', to_path='../new')
# 查看repo状态
# print repo.git.status()   # 返回通常的status几句信息
# print repo.is_dirty()    # 返回是否有改动（包括未add和未commit的）

# 添加文件 可以是单个文件名，也可以是`[ ]`数组，还可以是`.`代表全部
# print repo.git.add( '文件名' )
# commit提交
# print repo.git.commit( m='提交信息' )

# 创建remote：
# remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')
# 远程交互：
# remote = repo.remote()
# remote.fetch()
# remote.pull()
# remote.push()
 # 原意是返回工作区是否改变的状态
# 但是测试发现，工作区有变动它返回False，没变动却返回True
# print repo.is_dirty()
# 压缩到 tar 文件
# with open('repo.tar', 'wb') as fp:
#     repo.archive(fp)


repo = Repo("/mywork/github/pylearn")

print(repo.is_dirty())
print(repo.git.status());
# print(repo.git.stash())
print(repo.git.commit(m='modify code'))

# remote = repo.create_remote(name='github', url='https://github.com/playbar/pylearn.git ')

remo = repo.remote();
print(remo.fetch())
print(remo.pull())
print(remo.push())

print('success');

