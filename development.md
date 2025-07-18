- 配置环境变量：在项目根目录下编辑.env文件，填写数据库、邮箱、密钥等配置 信息。前端如需单独配置API地址，可编辑frontend/.env 文件。 
-  启动后端：在项目根目录下执行 
~~~
      docker compose up-d--wait backend 
~~~
  启动后端服务及相关依赖（如数据库）。 
- 启动前端：进入前端目录，安装依赖并启动开发服务器
~~~
      cd frontend  
      npm install  
      npm run dev 
~~~
  默认访问地址为http://localhost:5173。 
- 运行后端测试：激活Python虚拟环境后，在backend目录下执行
~~~
      pytest 
~~~
  查看后端单元测试结果。 
- 运行前端测试：在frontend 目录下执行 
~~~
      npx playwright test 
~~~
  可加--ui 参数进入可视化测试界面。 
- 数据备份：使用PostgreSQL 工具进行数据库备份
~~~
      pg_dump-h <服务器地址>-U <用户名>-d <数据库名> > backup.sql 
~~~
  建议定期备份并妥善保存。 
- 数据恢复：如需恢复数据库，执行 
~~~
      psql-h <服务器地址>-U <用户名>-d <数据库名> < backup.sql 
~~~
  恢复前建议先停止相关服务。 
遇到问题：如遇服务异常或无法访问，可尝试重启服务 
~~~
      docker compose restart 
~~~
  若问题仍未解决，请联系系统管理员或技术支持。 