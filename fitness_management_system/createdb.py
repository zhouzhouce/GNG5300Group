import subprocess
import urllib.request


create_server_command = [
    'az', 'mysql', 'server', 'create',
    '--resource-group', 'appsvc_linux_centralus_basic',
    '--location', 'Central US',
    '--name', 'djangojjdbserver',
    '--admin-user', 'jli',
    '--admin-password', '112233Khd3',
    '--sku-name', 'GP_Gen5_2',
]

subprocess.check_call(create_server_command)

create_db_command = [
    'az', 'mysql', 'db', 'create',
    '--resource-group', 'appsvc_linux_centralus_basic',
    '--server-name', 'djangojjdbserver',
    '--name', 'djangojdb',
]

subprocess.check_call(create_db_command)


connect_detail_command = [
    'az', 'mysql', 'server', 'show',
    '--resource-group', 'appsvc_linux_centralus_basic',
    '--name', 'djangojjdbserver',
]

print("details...")
subprocess.check_call(connect_detail_command)
