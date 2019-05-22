from git import Repo

repo = Repo("/mywork/github/pylearn")

print(repo.is_dirty())
print(repo.git.status());

repo.commit();

# remote = repo.create_remote(name='github', url='https://github.com/playbar/pylearn.git ')

remo = repo.remote();
remo.fetch();
remo.pull();
remo.push();

print('success');

