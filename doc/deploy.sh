
# 创建网络
docker network create app-network

# nginx容器
docker run -d \
  --name nginx \
  --network app-network \
  -p 8080:80 \
  -v $(pwd)/conf/nginx.conf:/etc/nginx/nginx.conf \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx:latest

# 智能审计助理
docker run -d \
  -p 5000:5000 \
  --network app-network \
  -v /root/workspace/audit/app:/app/app \
  --name audit \
  audit:1.0.0