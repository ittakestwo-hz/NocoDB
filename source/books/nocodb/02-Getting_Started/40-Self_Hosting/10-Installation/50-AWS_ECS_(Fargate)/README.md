# AWS ECS (Fargate)

## 在 AWS ECS (Fargate) 上部署 NocoDB

本指南将指导您在 Amazon ECS 上使用 Fargate 部署 NocoDB。

### 前提条件

- 配置了适当权限的 AWS CLI
- 对 AWS ECS 和 Fargate 有基本的了解

### 部署步骤

1. 创建 ECS 集群：
   ```
   aws ecs create-cluster --cluster-name <YOUR_ECS_CLUSTER>
   ```
2. 创建日志组：
   ```
   aws logs create-log-group --log-group-name /ecs/<YOUR_APP_NAME>/<YOUR_CONTAINER_NAME>
   ```
3. 创建 ECS 任务定义：
   每次创建时，它将添加一个新版本。如果不存在，则版本将为 1。
   ```
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
   > **提示**
   > 此 JSON 文件定义了容器规范。您可以在此处定义诸如 NC_DB 的密钥和环境变量。
   示例 `task-definition.json`：
   ```
   {
       "family": "nocodb-sample-task-def",
       "networkMode": "awsvpc",
       "containerDefinitions": [
       {
           "name": "<YOUR_CONTAINER_NAME>",
           "image": "nocodb/nocodb:latest",
           "essential": true,
           "logConfiguration": {
           "logDriver": "awslogs",
           "options": {
               "awslogs-group": "/ecs/<YOUR_APP_NAME>/<YOUR_CONTAINER_NAME>",
               "awslogs-region": "<YOUR_AWS_REGION>",
               "awslogs-stream-prefix": "ecs"
           }
       },
        "secrets": [
       {
           "name": "<YOUR_SECRETS_NAME>",
           "valueFrom": "<YOUR_SECRET_ARN>"
       }
       ],
       "environment": [
           {
               "name": "<YOUR_ENV_VARIABLE_NAME>",
               "value": "<YOUR_ENV_VARIABLE_VALUE>"
           }
       ],
       "portMappings": [
           {
               "containerPort": 8080,
               "hostPort": 8080,
               "protocol": "tcp"
           }
       ]
   }
   ],
   "requiresCompatibilities": [
       "FARGATE"
   ],
   "cpu": "256",
   "memory": "512",
   "executionRoleArn": "<YOUR_ECS_EXECUTION_ROLE_ARN>",
   "taskRoleArn": "<YOUR_ECS_TASK_ROLE_ARN>"
   }
   ```
4. 创建 ECS 服务：
   ```
   aws ecs create-service \
       --cluster <YOUR_ECS_CLUSTER> \
       --service-name  <YOUR_SERVICE_NAME> \
       --task-definition <YOUR_TASK_DEF>:<YOUR_TASK_DEF_VERSION> \
       --desired-count <DESIRED_COUNT> \
       --launch-type "FARGATE" \
       --platform-version <VERSION> \
       --health-check-grace-period-seconds <GRACE_PERIOD_IN_SECOND> \
       --network-configuration "awsvpcConfiguration={subnets=["<YOUR_SUBSETS>"], securityGroups=["<YOUR_SECURITY_GROUPS>"], assignPublicIp=ENABLED}" \
       --load-balancer targetGroupArn=<TARGET_GROUP_ARN>,containerName=<CONTAINER_NAME>,containerPort=<YOUR_CONTAINER_PORT>
   ```

### 重要说明

- 确保您的安全组具有正确的入站和出站规则。
- NC_DB 环境变量应正确设置以连接到您的数据库。
- 监控 ECS 控制台和 CloudWatch 日志以查看任何部署问题。
- 您可以根据需要自定义任务定义和服务配置。