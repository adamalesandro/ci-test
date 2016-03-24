from fabric.api import *

# the user to use for the remote commands
env.user = 'deployer3'
#env.password = "Favor3neat!"
# the servers where the commands are executed
env.host_string = '45.55.171.65'
env.key_filename = "/tmp/ssh/01_deploy"

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # # figure out the release name and version
    # dist = local('python setup.py --fullname', capture=True).strip()
    # # upload the source tarball to the temporary folder on the server
    # put('dist/%s.tar.gz' % dist, '/tmp/yourapplication.tar.gz')
    # # create a place where we can unzip the tarball, then enter
    # # that directory and unzip it
    #run('mkdir /var/www')
    # run('mkdir /var/www/test')
    # with cd('/var/www/test'):
    #     run('touch /var/www/test/somfile.txt')

    ##TODO: Make this agnostic, many questions about that.
    with cd('/var/www/git-test'):
        run('git pull')

    with cd('/var/www/test_bare.git'):
        run('git fetch https://github.com/adamalesandro/ci-test.git /var/www/test_bare.git')

    ##ATTEMPT AT POSSIBLY NECESSARY IF STATEMENT##
    # if run('mkdir /var/www/git-test'):
    #         with cd('/var/www/git-test'):
    #             run('git clone https://github.com/adamalesandro/ci-test.git /var/www/git-test')
    # else:
    #     with cd('/var/www/git-test'):
    #         # run('git clone https://github.com/adamalesandro/ci-test.git /var/www/git-test')
    #         run('git pull')


    ##ADDING SOME CHANGES FOR BARE INIT REPO CREATION FIRST##

    # run('mkdir /var/www/git-test-bare')
    # with cd('/var/www/git-test-bare'):
    #     run('git --bare init')
    #     run('git  https://github.com/adamalesandro/ci-test.git /var/www/git-test-bare')



def test():
    run('ls /var')

if __name__ == '__main__':
    test()
