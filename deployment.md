# 首次使用 
- 安装Docker 请访问https://www.docker.com/ 下载并安装 Docker Desktop，安装完 成后启动Docker 服务。 
- 安装uv（Python 包和环境管理工具） 在命令行中执行以下命令安装uv：
            ~~~
            pip install uv
            ~~~
- 进入backend 目录，安装依赖 在命令行中进入项目的backend目录，执行依赖安装 命令： 
~~~
            cd backend  
            uv sync 
~~~
- 激活虚拟环境 激活Python虚拟环境（Windows下）： 
~~~
            .venv\Scripts\activate 
~~~
或（Linux/macOS 下）： 
source .venv/bin/activate  
# 启动过程              
- 确保已正确配置根目录下的.env文件。 
- 启动后端服务（在项目根目录下）： 
~~~
            docker compose up-d--wait backend  
~~~
-  启动前端服务（进入frontend 目录）：
~~~
            cd frontend  
            npm install  
            npm run dev  
~~~
- 在浏览器中访问http://localhost:5173 进入系统界面。 
# 停止与挂起流程 
- 停止后端服务： 
~~~
            docker compose down  
~~~
- 停止前端开发服务器，按下Ctrl+C终止命令行进程。 
- 如需挂起服务，可使用Docker的暂停命令： 
~~~
            docker compose pause  
~~~
- 恢复服务： 
~~~
            docker compose unpause
~~~