import subprocess
from paramiko import SSHClient
import paramiko
import os
import hashlib


HOSTNAME = "hostname"
PORT = 22
USERNAME = "user"
rsa_private_key = r"\key.pem"
KEY = paramiko.RSAKey.from_private_key_file(rsa_private_key)

dirs_local = [".\\lib\\", ".\\tests\\"]
dir_remote = "/home/" + USERNAME + "/target_dir/"
glob_pattern = '*.*'




def agent_auth(transPORT, USERNAME):
    """
    Attempt to authenticate to the given transPORT using any of the private
    keys available from an SSH agent or from a local private RSA key file (assumes no pass phrase).
    """
    try:
        ki = paramiko.RSAKey.from_private_key_file(rsa_private_key)
    except Exception as mess:
        print('Failed loading {0} {1}'.format(rsa_private_key, mess))

    agent = paramiko.Agent()
    agent_keys = agent.get_keys() + (ki,)
    if len(agent_keys) == 0:
        return

    for key in agent_keys:
        print('Trying ssh-agent key %s' % str(key.get_fingerprint()), )
        try:
            transPORT.auth_publickey(USERNAME, key)
            print('... success!')
            return
        except paramiko.SSHException as e:
            print('... failed!', e)


# get host key, if we know one
hostkeytype = None
hostkey = None
files_copied = 0
try:
    host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
except IOError:
    try:
        # try ~/ssh/ too, e.g. on windows
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
    except IOError:
        print('*** Unable to open host keys file')
        host_keys = {}

# if host_keys.has_key(HOSTNAME):
#     hostkeytype = host_keys[HOSTNAME].keys()[0]
#     hostkey = host_keys[HOSTNAME][hostkeytype]
#     print('Using host key of type %s' % hostkeytype)

# now, connect and use paramiko TransPORT to negotiate SSH2 across the connection
try:
    print('Establishing SSH connection to:', HOSTNAME, PORT, '...')
    t = paramiko.Transport((HOSTNAME, PORT))
    t.start_client()

    agent_auth(t, USERNAME)

    if not t.is_authenticated():
        print('RSA key auth failed! Trying password login...')
        t.connect(username=USERNAME, hostkey=hostkey)
    else:
        sftp = t.open_session()
    sftp = paramiko.SFTPClient.from_transport(t)

    # dirlist on remote host
    #    dirlist = sftp.listdir('.')
    #    print "Dirlist:", dirlist
    for dir_local in dirs_local:
        try:
            sftp.mkdir(dir_remote)
        except IOError as mess:
            print('(assuming ', dir_remote, 'exists)', mess)

            #    print 'created ' + dir_remote +' on the HOSTNAME'

        # BETTER: use the get() and put() methods
        # for fname in os.listdir(dir_local):

        for path, dirs, files in os.walk(dir_local):
            # print(path, dirs, files)
            try:
                sftp.mkdir(dir_remote + "/" + path.replace(".", "").replace("\\", "/"))
            except IOError as mess:
                print('(assuming ', dir_remote, 'exists)', mess)
            for fi in files:
                is_up_to_date = False
                local_file = os.path.join(path + "/" + fi)
                print(local_file)
                remote_file = dir_remote + '/' + path.replace(".", "").replace("\\", "/") + "/" + fi

                # if remote file exists
                try:
                    if sftp.stat(remote_file):
                        local_file_data = open(local_file, "rb").read()
                        remote_file_data = sftp.open(remote_file).read()
                        md_hash = hashlib.md5()
                        md1 = hashlib.md5()
                        md2 = hashlib.md5()
                        md1.update(local_file_data)
                        md2.update(remote_file_data)
                        if md1.hexdigest() == md2.hexdigest():
                            is_up_to_date = True
                            print("UNCHANGED:", os.path.basename(fi))
                        else:
                            print("MODIFIED:", os.path.basename(fi), )
                except:
                    print("NEW: ", os.path.basename(fi), )

                if not is_up_to_date:
                    print('Copying', local_file, 'to ', remote_file)
                    sftp.put(local_file, remote_file)
                    files_copied += 1
    t.close()

except Exception as mess:
    print('*** Caught exception: %s:' % mess)
    try:
        t.close()
    except:
        pass
print('=' * 60)
print('Total files copied:', files_copied)
print('All operations complete!')
print('=' * 60)

