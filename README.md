# flask项目实践
这是一个基于flask框架实现的简单项目架构，仅利用flask的路由管理，配置管理，数据库连接管理。
## 当前项目部署方法
```
# install python pip virtualenv
# checkout code
cd CODE_PATH/PROJECT_NAME/
virtualenv --no-site-packages venv
source ./venv/bin/activate
pip install -r requirement.txt

# create config/* from config/*.sample and modify to yours
# add start.sh with follow code to rc.local if you want
# start.sh
source CODE_PATH/PROJECT_NAME/venv/bin/activate
uwsgi -d /var/log/uwsgi.log --ini CODE_PATH/PROJECT_NAME/config/uwsgi.ini

# update nginx conf
location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:5000;
}
```

